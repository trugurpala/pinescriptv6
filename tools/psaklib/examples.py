from __future__ import annotations

from datetime import date
import hashlib
from pathlib import Path, PurePosixPath
import re
import subprocess

from .validation import EVIDENCE_LEVELS, Issue


STRUCTURAL_LIMITATION = "Not compiled in TradingView during this repository audit."


def sha256_file(path: Path) -> str:
    content = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(content).hexdigest()


def discover_pine_files(root: Path) -> list[Path]:
    tracked = subprocess.run(
        ["git", "-C", str(root), "ls-files", "-z", "--", "*.pine"],
        check=False,
        capture_output=True,
    )
    if tracked.returncode == 0:
        relative_paths = [
            Path(value.decode("utf-8"))
            for value in tracked.stdout.split(b"\0")
            if value
        ]
        return [root / path for path in sorted(relative_paths, key=lambda item: item.as_posix())]
    paths = [
        path
        for path in root.rglob("*.pine")
        if ".git" not in path.relative_to(root).parts
    ]
    return sorted(paths, key=lambda path: path.relative_to(root).as_posix())


def build_manifest(root: Path, checked_on: str | None = None) -> dict[str, object]:
    check_date = checked_on or date.today().isoformat()
    examples = []
    for path in discover_pine_files(root):
        examples.append(
            {
                "path": path.relative_to(root).as_posix(),
                "sha256": sha256_file(path),
                "evidence": "structural-only",
                "checked_on": check_date,
                "tradingview_record": None,
                "limitations": [STRUCTURAL_LIMITATION],
            }
        )
    return {"schema_version": 1, "examples": examples}


def validate_examples(
    root: Path, manifest: object, records: object
) -> list[Issue]:
    issues: list[Issue] = []
    if not isinstance(manifest, dict) or manifest.get("schema_version") != 1:
        return [Issue("invalid-schema", "examples/manifest.json", "schema_version must be 1")]
    entries = manifest.get("examples")
    if not isinstance(entries, list):
        return [Issue("invalid-examples", "examples/manifest.json", "examples must be a list")]
    discovered = {
        path.relative_to(root).as_posix(): path for path in discover_pine_files(root)
    }
    manifest_paths: set[str] = set()
    entry_by_path: dict[str, dict[str, object]] = {}
    for index, entry in enumerate(entries):
        location = f"examples/manifest.json#/examples/{index}"
        if not isinstance(entry, dict):
            issues.append(Issue("invalid-example-entry", location, "entry must be an object"))
            continue
        required_entry_fields = {
            "path",
            "sha256",
            "evidence",
            "checked_on",
            "tradingview_record",
            "limitations",
        }
        missing_entry_fields = sorted(required_entry_fields - entry.keys())
        if missing_entry_fields:
            issues.append(
                Issue(
                    "missing-example-field",
                    location,
                    f"missing fields: {', '.join(missing_entry_fields)}",
                )
            )
        path_value = entry.get("path")
        if not isinstance(path_value, str) or not path_value.endswith(".pine"):
            issues.append(Issue("invalid-example-path", location, "path must identify a Pine file"))
            continue
        manifest_path = PurePosixPath(path_value)
        resolved = (root / Path(*manifest_path.parts)).resolve()
        if (
            manifest_path.is_absolute()
            or ".." in manifest_path.parts
            or "\\" in path_value
            or not resolved.is_relative_to(root.resolve())
        ):
            issues.append(Issue("invalid-example-path", location, "path must stay inside the repository"))
            continue
        if path_value in manifest_paths:
            issues.append(Issue("duplicate-example", location, f"duplicate path: {path_value}"))
        manifest_paths.add(path_value)
        entry_by_path[path_value] = entry
        file_path = root / path_value
        if not file_path.is_file():
            issues.append(Issue("missing-example-file", path_value, "manifested file is missing"))
            continue
        actual_hash = sha256_file(file_path)
        declared_hash = entry.get("sha256")
        if not isinstance(declared_hash, str) or not re.fullmatch(r"[0-9a-f]{64}", declared_hash):
            issues.append(Issue("invalid-example-metadata", path_value, "sha256 must be lowercase hexadecimal"))
        elif declared_hash != actual_hash:
            issues.append(Issue("stale-example-hash", path_value, "manifest hash does not match file"))
        if entry.get("evidence") not in EVIDENCE_LEVELS:
            issues.append(Issue("invalid-example-evidence", path_value, "unsupported evidence level"))
        checked_on = entry.get("checked_on")
        try:
            valid_checked_on = (
                isinstance(checked_on, str)
                and date.fromisoformat(checked_on).isoformat() == checked_on
            )
        except ValueError:
            valid_checked_on = False
        limitations = entry.get("limitations")
        record_id = entry.get("tradingview_record")
        metadata_valid = (
            valid_checked_on
            and isinstance(limitations, list)
            and bool(limitations)
            and all(isinstance(item, str) and item.strip() for item in limitations)
            and (record_id is None or (isinstance(record_id, str) and bool(record_id.strip())))
        )
        if entry.get("evidence") == "structural-only" and record_id is not None:
            metadata_valid = False
        if entry.get("evidence") == "tradingview-verified" and not isinstance(record_id, str):
            metadata_valid = False
        if not metadata_valid:
            issues.append(Issue("invalid-example-metadata", path_value, "checked_on, limitations, or verification reference is invalid"))
    for relative, file_path in discovered.items():
        if relative not in manifest_paths:
            issues.append(Issue("unmanifested-example", relative, "Pine file is not in the manifest"))
        if not file_path.is_file():
            if relative not in manifest_paths:
                issues.append(Issue("missing-example-file", relative, "tracked Pine file is missing"))
            continue
        if file_path.stat().st_size == 0:
            issues.append(Issue("empty-example", relative, "Pine file is empty"))
            continue
        first_line = file_path.read_text(encoding="utf-8-sig").splitlines()[0].strip()
        if first_line != "//@version=6":
            issues.append(Issue("non-v6-example", relative, "first line must be //@version=6"))
    record_by_id: dict[str, dict[str, object]] = {}
    referenced_record_ids = {
        str(entry.get("tradingview_record"))
        for entry in entry_by_path.values()
        if entry.get("tradingview_record") is not None
    }
    if not isinstance(records, dict) or records.get("schema_version") != 1 or not isinstance(records.get("records"), list):
        issues.append(Issue("invalid-verification", "verification/tradingview.json", "records schema is invalid"))
    else:
        required_record_fields = {
            "id",
            "path",
            "sha256",
            "pine_version",
            "tested_on",
            "result",
            "environment",
            "reviewer",
            "notes",
        }
        for index, record in enumerate(records["records"]):
            location = f"verification/tradingview.json#/records/{index}"
            if not isinstance(record, dict):
                issues.append(Issue("invalid-verification-record", location, "record must be an object"))
                continue
            missing = sorted(required_record_fields - record.keys())
            record_id = record.get("id")
            fields_valid = (
                not missing
                and isinstance(record_id, str)
                and bool(record_id.strip())
                and isinstance(record.get("path"), str)
                and isinstance(record.get("sha256"), str)
                and bool(re.fullmatch(r"[0-9a-f]{64}", str(record.get("sha256"))))
                and record.get("pine_version") == "6"
                and isinstance(record.get("tested_on"), str)
                and record.get("result") in {"pass", "fail"}
                and isinstance(record.get("environment"), str)
                and bool(str(record.get("environment")).strip())
                and isinstance(record.get("reviewer"), str)
                and bool(str(record.get("reviewer")).strip())
                and isinstance(record.get("notes"), str)
            )
            if fields_valid:
                try:
                    date.fromisoformat(str(record["tested_on"]))
                except ValueError:
                    fields_valid = False
            if not fields_valid:
                detail = f"missing fields: {', '.join(missing)}" if missing else "record metadata is invalid"
                issues.append(Issue("invalid-verification-record", location, detail))
            if isinstance(record_id, str):
                if record_id in record_by_id:
                    issues.append(Issue("duplicate-verification-id", location, f"duplicate id: {record_id}"))
                else:
                    record_by_id[record_id] = record
                if record_id not in referenced_record_ids:
                    issues.append(Issue("orphan-verification-record", location, f"unreferenced id: {record_id}"))
    for path_value, entry in entry_by_path.items():
        record_id = entry.get("tradingview_record")
        if entry.get("evidence") == "tradingview-verified":
            record = record_by_id.get(str(record_id))
            if record is None:
                issues.append(Issue("missing-verification-record", path_value, "TradingView record is missing"))
            else:
                file_path = root / path_value
                if record.get("result") != "pass":
                    issues.append(Issue("verification-not-passing", path_value, "TradingView record result must be pass"))
                if not file_path.is_file() or record.get("path") != path_value or record.get("sha256") != sha256_file(file_path):
                    issues.append(Issue("stale-verification", path_value, "verification does not match current file"))
    return sorted(issues)
