from __future__ import annotations

from dataclasses import dataclass
from datetime import date
import json
from pathlib import Path, PurePosixPath
import re
from typing import Any


SOURCE_KINDS = {
    "official-reference",
    "official-guide",
    "official-release-note",
    "manual-verification",
    "sanitized-error",
    "community-lead",
}
EVIDENCE_LEVELS = {
    "official",
    "tradingview-verified",
    "structural-only",
    "unverified",
}
DISTRIBUTABLE_EVIDENCE = {
    "official",
    "tradingview-verified",
    "structural-only",
}
ABSOLUTE_WORDS = {"always", "never", "guaranteed", "must"}
RULE_STATUSES = {"active", "needs-review", "superseded"}
ID_PATTERN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")

DEFAULT_CRITICAL_FILES = (
    "README.md",
    "README.tr.md",
    "LICENSE",
    "SECURITY.md",
    "CONTRIBUTING.md",
    "CHANGELOG.md",
    "CITATION.cff",
    "AGENTS.md",
    "knowledge/catalog.json",
    "knowledge/sources.json",
    "examples/manifest.json",
)


@dataclass(frozen=True, order=True)
class Issue:
    code: str
    path: str
    message: str
    severity: str = "error"


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def load_json(path: Path) -> Any:
    return json.loads(
        path.read_text(encoding="utf-8"), object_pairs_hook=_unique_object
    )


def _valid_date(value: object) -> bool:
    if not isinstance(value, str):
        return False
    try:
        return date.fromisoformat(value).isoformat() == value
    except ValueError:
        return False


def _valid_repo_relative_path(root: Path, value: object) -> bool:
    if not isinstance(value, str) or not value.strip() or "\\" in value:
        return False
    relative = PurePosixPath(value)
    if relative.is_absolute() or ".." in relative.parts:
        return False
    resolved = (root / Path(*relative.parts)).resolve()
    return resolved.is_relative_to(root.resolve())


def validate_sources(
    root: Path, data: object
) -> tuple[list[Issue], dict[str, str]]:
    del root
    issues: list[Issue] = []
    source_index: dict[str, str] = {}
    if not isinstance(data, dict) or data.get("schema_version") != 1:
        return [Issue("invalid-schema", "knowledge/sources.json", "schema_version must be 1")], source_index
    sources = data.get("sources")
    if not isinstance(sources, list):
        return [Issue("invalid-sources", "knowledge/sources.json", "sources must be a list")], source_index
    required = {
        "id",
        "title",
        "url",
        "publisher",
        "kind",
        "accessed",
        "applies_to",
        "locator",
    }
    for index, source in enumerate(sources):
        path = f"knowledge/sources.json#/sources/{index}"
        if not isinstance(source, dict):
            issues.append(Issue("invalid-source", path, "source must be an object"))
            continue
        missing = sorted(required - source.keys())
        if missing:
            issues.append(Issue("missing-source-field", path, f"missing fields: {', '.join(missing)}"))
        for field in ("title", "publisher", "applies_to", "locator"):
            value = source.get(field)
            if not isinstance(value, str) or not value.strip():
                issues.append(Issue("invalid-source-field", path, f"{field} must be non-empty text"))
        source_id = source.get("id")
        if not isinstance(source_id, str) or not ID_PATTERN.fullmatch(source_id):
            issues.append(Issue("invalid-source-id", path, "id must be stable ASCII text"))
        elif source_id in source_index:
            issues.append(Issue("duplicate-source-id", path, f"duplicate id: {source_id}"))
        else:
            source_index[source_id] = str(source.get("kind", ""))
        if source.get("kind") not in SOURCE_KINDS:
            issues.append(Issue("invalid-source-kind", path, "unsupported source kind"))
        from .links import validate_source_url

        url_problem = validate_source_url(source.get("url"))
        if url_problem:
            issues.append(Issue("invalid-source-url", path, url_problem))
        if not _valid_date(source.get("accessed")):
            issues.append(Issue("invalid-source-date", path, "accessed must be an ISO date"))
    return sorted(issues), source_index


def validate_catalog(
    root: Path, data: object, source_index: dict[str, str]
) -> list[Issue]:
    issues: list[Issue] = []
    if not isinstance(data, dict) or data.get("schema_version") != 1:
        return [Issue("invalid-schema", "knowledge/catalog.json", "schema_version must be 1")]
    rules = data.get("rules")
    if not isinstance(rules, list):
        return [Issue("invalid-rules", "knowledge/catalog.json", "rules must be a list")]
    required = {
        "id",
        "title",
        "claim",
        "rationale",
        "scope",
        "exceptions",
        "sources",
        "evidence",
        "verified_on",
        "status",
        "body",
        "tags",
    }
    rule_ids: set[str] = set()
    conflicts: dict[str, set[str]] = {}
    for index, rule in enumerate(rules):
        path = f"knowledge/catalog.json#/rules/{index}"
        if not isinstance(rule, dict):
            issues.append(Issue("invalid-rule", path, "rule must be an object"))
            continue
        missing = sorted(required - rule.keys())
        if missing:
            issues.append(Issue("missing-rule-field", path, f"missing fields: {', '.join(missing)}"))
        rule_id = rule.get("id")
        if not isinstance(rule_id, str) or not ID_PATTERN.fullmatch(rule_id):
            issues.append(Issue("invalid-rule-id", path, "id must be stable ASCII text"))
        elif rule_id in rule_ids:
            issues.append(Issue("duplicate-rule-id", path, f"duplicate id: {rule_id}"))
        else:
            rule_ids.add(rule_id)
        for field in ("title", "claim", "rationale", "scope", "body"):
            value = rule.get(field)
            if not isinstance(value, str) or not value.strip():
                issues.append(Issue("invalid-rule-field", path, f"{field} must be non-empty text"))
        list_values: dict[str, list[str]] = {}
        for field in ("exceptions", "sources", "tags"):
            value = rule.get(field)
            if (
                not isinstance(value, list)
                or not value
                or any(not isinstance(item, str) or not item.strip() for item in value)
            ):
                issues.append(Issue("invalid-rule-list", path, f"{field} must contain non-empty text values"))
                list_values[field] = []
            else:
                list_values[field] = value
        for source_id in list_values["sources"]:
            if source_id not in source_index:
                issues.append(Issue("unknown-source", path, f"unknown source: {source_id}"))
        if not list_values["sources"]:
            issues.append(Issue("missing-rule-source", path, "rule must reference a source"))
        body = rule.get("body")
        if not _valid_repo_relative_path(root, body):
            issues.append(Issue("invalid-rule-body", path, "body path must stay inside the repository"))
        elif not (root / str(body)).is_file():
            issues.append(Issue("missing-rule-body", path, f"missing rule body: {body}"))
        evidence = rule.get("evidence")
        if evidence not in EVIDENCE_LEVELS:
            issues.append(Issue("invalid-evidence", path, "unsupported evidence level"))
        if rule.get("status") == "active" and evidence not in DISTRIBUTABLE_EVIDENCE:
            issues.append(Issue("undistributable-rule", path, "active rule lacks distributable evidence"))
        known_source_kinds = {
            source_index[source_id]
            for source_id in list_values["sources"]
            if source_id in source_index
        }
        official_kinds = {
            "official-guide",
            "official-reference",
            "official-release-note",
        }
        if evidence == "official" and not (known_source_kinds & official_kinds):
            issues.append(Issue("evidence-source-mismatch", path, "official evidence requires an official source"))
        if evidence == "tradingview-verified" and "manual-verification" not in known_source_kinds:
            issues.append(Issue("evidence-source-mismatch", path, "TradingView evidence requires a manual-verification source"))
        if rule.get("status") == "active" and known_source_kinds == {"community-lead"}:
            issues.append(Issue("community-only-rule", path, "community-only evidence cannot activate guidance"))
        if rule.get("status") not in RULE_STATUSES:
            issues.append(Issue("invalid-rule-status", path, "unsupported rule status"))
        if not isinstance(rule.get("scope"), str) or not rule.get("scope", "").strip():
            issues.append(Issue("missing-rule-scope", path, "rule scope must be non-empty"))
        if not _valid_date(rule.get("verified_on")):
            issues.append(Issue("invalid-rule-date", path, "verified_on must be an ISO date"))
        claim = rule.get("claim")
        words = set(re.findall(r"[a-z]+", claim.lower())) if isinstance(claim, str) else set()
        if words & ABSOLUTE_WORDS:
            if not isinstance(rule.get("scope"), str) or not rule.get("scope", "").strip() or not isinstance(rule.get("exceptions"), list) or not rule.get("exceptions"):
                issues.append(Issue("unscoped-absolute", path, "absolute claim requires scope and exceptions"))
        if rule.get("status") == "active" and rule.get("conflict_key") and rule.get("claim_value"):
            conflicts.setdefault(str(rule["conflict_key"]), set()).add(str(rule["claim_value"]))
    for conflict_key, values in conflicts.items():
        if len(values) > 1:
            issues.append(Issue("conflicting-rules", "knowledge/catalog.json", f"conflicting active values for {conflict_key}"))
    return sorted(issues)


def validate_critical_files(
    root: Path, paths: tuple[str, ...] = DEFAULT_CRITICAL_FILES
) -> list[Issue]:
    issues: list[Issue] = []
    for relative in paths:
        path = root / relative
        if not path.is_file():
            issues.append(Issue("missing-critical-file", relative, "critical file is missing"))
        elif path.stat().st_size == 0:
            issues.append(Issue("empty-critical-file", relative, "critical file is empty"))
    return sorted(issues)


def validate_repository(root: Path) -> list[Issue]:
    required = {
        "knowledge/catalog.json": "missing-catalog",
        "knowledge/sources.json": "missing-sources",
        "examples/manifest.json": "missing-examples",
        "verification/tradingview.json": "missing-verification",
    }
    issues = [
        Issue(code, path, "required canonical data file is missing")
        for path, code in required.items()
        if not (root / path).is_file()
    ]
    if (root / "knowledge/sources.json").is_file():
        try:
            source_data = load_json(root / "knowledge/sources.json")
        except (OSError, ValueError) as error:
            issues.append(Issue("invalid-json", "knowledge/sources.json", str(error)))
            source_ids = {}
        else:
            source_issues, source_ids = validate_sources(root, source_data)
            issues.extend(source_issues)
    else:
        source_ids = {}
    if (root / "knowledge/catalog.json").is_file():
        try:
            catalog_data = load_json(root / "knowledge/catalog.json")
        except (OSError, ValueError) as error:
            issues.append(Issue("invalid-json", "knowledge/catalog.json", str(error)))
        else:
            issues.extend(validate_catalog(root, catalog_data, source_ids))
    if (root / "examples/manifest.json").is_file() and (root / "verification/tradingview.json").is_file():
        from .examples import validate_examples

        try:
            manifest_data = load_json(root / "examples/manifest.json")
            verification_data = load_json(root / "verification/tradingview.json")
        except (OSError, ValueError) as error:
            issues.append(Issue("invalid-json", "examples or verification data", str(error)))
        else:
            issues.extend(validate_examples(root, manifest_data, verification_data))
    return sorted(issues)
