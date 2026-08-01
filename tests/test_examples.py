from pathlib import Path
from tempfile import TemporaryDirectory
import json
import subprocess
import sys
import unittest

from tools.psaklib.examples import (
    build_manifest,
    discover_pine_files,
    sha256_file,
    validate_examples,
)


VALID_PINE = '//@version=6\nindicator("Structural fixture")\nplot(close)\n'


class ExampleTests(unittest.TestCase):
    def test_pine_hash_is_stable_across_line_endings(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            lf_path = root / "lf.pine"
            crlf_path = root / "crlf.pine"
            lf_path.write_bytes(VALID_PINE.encode("utf-8"))
            crlf_path.write_bytes(VALID_PINE.replace("\n", "\r\n").encode("utf-8"))

            self.assertEqual(sha256_file(lf_path), sha256_file(crlf_path))

    def test_manifest_command_prints_complete_json_without_writing(self):
        manifest_path = Path("examples/manifest.json")
        existed_before = manifest_path.exists()

        result = subprocess.run(
            [sys.executable, "tools/psak.py", "manifest"],
            check=False,
            capture_output=True,
            text=True,
        )

        self.assertEqual(result.returncode, 0, result.stderr or result.stdout)
        data = json.loads(result.stdout)
        self.assertEqual(data["schema_version"], 1)
        self.assertEqual(len(data["examples"]), 56)
        self.assertEqual(manifest_path.exists(), existed_before)

    def test_discovery_is_sorted_and_ignores_git_objects(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "z.pine").write_text(VALID_PINE, encoding="utf-8")
            (root / "a").mkdir()
            (root / "a/example.pine").write_text(VALID_PINE, encoding="utf-8")
            (root / ".git/objects").mkdir(parents=True)
            (root / ".git/objects/hidden.pine").write_text(VALID_PINE, encoding="utf-8")

            paths = [path.relative_to(root).as_posix() for path in discover_pine_files(root)]

            self.assertEqual(paths, ["a/example.pine", "z.pine"])

    def test_git_repository_discovers_only_tracked_pine_files(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            subprocess.run(["git", "init", "-q", str(root)], check=True)
            (root / ".gitignore").write_text("ignored.pine\n", encoding="utf-8")
            (root / "tracked.pine").write_text(VALID_PINE, encoding="utf-8")
            (root / "untracked.pine").write_text(VALID_PINE, encoding="utf-8")
            (root / "ignored.pine").write_text(VALID_PINE, encoding="utf-8")
            subprocess.run(
                ["git", "-C", str(root), "add", ".gitignore", "tracked.pine"],
                check=True,
            )

            paths = [path.relative_to(root).as_posix() for path in discover_pine_files(root)]

            self.assertEqual(paths, ["tracked.pine"])

    def test_deleted_tracked_pine_is_reported_without_crashing(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            subprocess.run(["git", "init", "-q", str(root)], check=True)
            path = root / "tracked.pine"
            path.write_text(VALID_PINE, encoding="utf-8")
            old_hash = sha256_file(path)
            subprocess.run(["git", "-C", str(root), "add", "tracked.pine"], check=True)
            path.unlink()
            manifest = {
                "schema_version": 1,
                "examples": [
                    {
                        "path": "tracked.pine",
                        "sha256": old_hash,
                        "evidence": "structural-only",
                        "checked_on": "2026-07-31",
                        "tradingview_record": None,
                        "limitations": ["Deleted tracked fixture."],
                    }
                ],
            }

            issues = validate_examples(root, manifest, {"schema_version": 1, "records": []})

            self.assertIn("missing-example-file", {issue.code for issue in issues})

    def test_manifest_uses_hash_and_structural_only_label(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "example.pine"
            path.write_text(VALID_PINE, encoding="utf-8")

            manifest = build_manifest(root, checked_on="2026-07-31")
            entry = manifest["examples"][0]

            self.assertEqual(entry["path"], "example.pine")
            self.assertEqual(entry["sha256"], sha256_file(path))
            self.assertEqual(entry["evidence"], "structural-only")
            self.assertIsNone(entry["tradingview_record"])

    def test_missing_empty_and_non_v6_examples_are_rejected(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "valid.pine").write_text(VALID_PINE, encoding="utf-8")
            (root / "empty.pine").write_text("", encoding="utf-8")
            (root / "old.pine").write_text("//@version=5\nindicator('Old')\n", encoding="utf-8")
            manifest = {
                "schema_version": 1,
                "examples": [
                    {
                        "path": "valid.pine",
                        "sha256": sha256_file(root / "valid.pine"),
                        "evidence": "structural-only",
                        "checked_on": "2026-07-31",
                        "tradingview_record": None,
                        "limitations": ["Not compiled in TradingView during this repository audit."],
                    }
                ],
            }

            issues = validate_examples(root, manifest, {"schema_version": 1, "records": []})
            codes = {issue.code for issue in issues}

            self.assertIn("unmanifested-example", codes)
            self.assertIn("empty-example", codes)
            self.assertIn("non-v6-example", codes)

    def test_changed_file_invalidates_tradingview_record(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "verified.pine"
            path.write_text(VALID_PINE, encoding="utf-8")
            manifest = build_manifest(root, checked_on="2026-07-31")
            manifest["examples"][0]["evidence"] = "tradingview-verified"
            manifest["examples"][0]["tradingview_record"] = "TV-001"
            records = {
                "schema_version": 1,
                "records": [
                    {
                        "id": "TV-001",
                        "path": "verified.pine",
                        "sha256": "0" * 64,
                        "pine_version": "6",
                        "tested_on": "2026-07-31",
                        "result": "pass",
                        "environment": "TradingView Pine Editor",
                        "reviewer": "Uğur Pala",
                        "notes": "Manual fixture",
                    }
                ],
            }

            issues = validate_examples(root, manifest, records)

            self.assertIn("stale-verification", {issue.code for issue in issues})

    def test_manifest_path_cannot_escape_repository(self):
        with TemporaryDirectory() as parent:
            parent_path = Path(parent)
            root = parent_path / "repo"
            root.mkdir()
            outside = parent_path / "outside.pine"
            outside.write_text(VALID_PINE, encoding="utf-8")
            manifest = {
                "schema_version": 1,
                "examples": [
                    {
                        "path": "../outside.pine",
                        "sha256": sha256_file(outside),
                        "evidence": "structural-only",
                        "checked_on": "2026-07-31",
                        "tradingview_record": None,
                        "limitations": ["Outside path fixture."],
                    }
                ],
            }

            issues = validate_examples(root, manifest, {"schema_version": 1, "records": []})

            self.assertIn("invalid-example-path", {issue.code for issue in issues})

    def test_verification_records_require_complete_unique_referenced_metadata(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "verified.pine"
            path.write_text(VALID_PINE, encoding="utf-8")
            manifest = build_manifest(root, checked_on="2026-07-31")
            manifest["examples"][0]["evidence"] = "tradingview-verified"
            manifest["examples"][0]["tradingview_record"] = "TV-001"
            records = {
                "schema_version": 1,
                "records": [
                    {"id": "TV-001", "path": "verified.pine", "sha256": sha256_file(path)},
                    {"id": "TV-001", "path": "verified.pine", "sha256": sha256_file(path)},
                    {
                        "id": "TV-ORPHAN",
                        "path": "verified.pine",
                        "sha256": sha256_file(path),
                        "pine_version": "6",
                        "tested_on": "2026-07-31",
                        "result": "pass",
                        "environment": "TradingView Pine Editor",
                        "reviewer": "Reviewer",
                        "notes": "Orphan fixture",
                    },
                ],
            }

            issues = validate_examples(root, manifest, records)
            codes = {issue.code for issue in issues}

            self.assertIn("invalid-verification-record", codes)
            self.assertIn("duplicate-verification-id", codes)
            self.assertIn("orphan-verification-record", codes)

    def test_failed_manual_result_cannot_mark_example_verified(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "verified.pine"
            path.write_text(VALID_PINE, encoding="utf-8")
            manifest = build_manifest(root, checked_on="2026-07-31")
            manifest["examples"][0]["evidence"] = "tradingview-verified"
            manifest["examples"][0]["tradingview_record"] = "TV-FAIL"
            records = {
                "schema_version": 1,
                "records": [
                    {
                        "id": "TV-FAIL",
                        "path": "verified.pine",
                        "sha256": sha256_file(path),
                        "pine_version": "6",
                        "tested_on": "2026-07-31",
                        "result": "fail",
                        "environment": "TradingView Pine Editor",
                        "reviewer": "Reviewer",
                        "notes": "Compilation failed.",
                    }
                ],
            }

            issues = validate_examples(root, manifest, records)

            self.assertIn("verification-not-passing", {issue.code for issue in issues})

    def test_manifest_requires_complete_semantic_metadata(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "example.pine"
            path.write_text(VALID_PINE, encoding="utf-8")
            minimal = {
                "schema_version": 1,
                "examples": [
                    {
                        "path": "example.pine",
                        "sha256": sha256_file(path),
                        "evidence": "structural-only",
                    }
                ],
            }
            wrong_types = build_manifest(root, checked_on="2026-07-31")
            wrong_types["examples"][0]["checked_on"] = "31-07-2026"
            wrong_types["examples"][0]["limitations"] = "none"
            wrong_types["examples"][0]["tradingview_record"] = 42

            minimal_issues = validate_examples(
                root, minimal, {"schema_version": 1, "records": []}
            )
            typed_issues = validate_examples(
                root, wrong_types, {"schema_version": 1, "records": []}
            )

            self.assertIn("missing-example-field", {issue.code for issue in minimal_issues})
            self.assertIn("invalid-example-metadata", {issue.code for issue in typed_issues})


if __name__ == "__main__":
    unittest.main()
