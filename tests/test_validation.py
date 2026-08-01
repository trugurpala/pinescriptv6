from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from tools.psaklib.validation import load_json, validate_decisions, validate_repository


class ValidationTests(unittest.TestCase):
    def test_load_json_rejects_duplicate_keys(self):
        with TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.json"
            path.write_text('{"id": "one", "id": "two"}', encoding="utf-8")

            with self.assertRaisesRegex(ValueError, "duplicate JSON key: id"):
                load_json(path)

    def test_missing_required_catalogs_are_reported(self):
        with TemporaryDirectory() as directory:
            codes = {issue.code for issue in validate_repository(Path(directory))}

            self.assertEqual(
                codes,
                {
                    "missing-catalog",
                    "missing-decisions",
                    "missing-examples",
                    "missing-sources",
                    "missing-verification",
                },
            )

    def test_malformed_catalog_is_reported_without_exception(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "knowledge").mkdir()
            (root / "knowledge/catalog.json").write_text("{broken", encoding="utf-8")

            issues = validate_repository(root)

            self.assertIn("invalid-json", {issue.code for issue in issues})

    def test_decision_register_requires_supported_disposition_and_source_refs(self):
        root = Path(__file__).resolve().parents[1]
        data = {
            "schema_version": 1,
            "decisions": [
                {
                    "id": "PSAK-GOV-001",
                    "title": "Unsupported sample",
                    "disposition": "maybe",
                    "status": "active",
                    "decided_on": "2026-08-01",
                    "summary": "Sample decision.",
                    "rationale": "Exercises validation.",
                    "user_impact": "Keeps unsupported choices out.",
                    "source_refs": [],
                    "implementation_refs": ["README.md"],
                }
            ],
        }

        codes = {issue.code for issue in validate_decisions(root, data)}

        self.assertIn("invalid-decision-disposition", codes)
        self.assertIn("missing-decision-source", codes)

    def test_decision_register_rejects_unknown_implementation_refs(self):
        root = Path(__file__).resolve().parents[1]
        data = {
            "schema_version": 1,
            "decisions": [
                {
                    "id": "PSAK-GOV-001",
                    "title": "Valid shape with bad path",
                    "disposition": "adopt",
                    "status": "active",
                    "decided_on": "2026-08-01",
                    "summary": "Sample decision.",
                    "rationale": "Exercises validation.",
                    "user_impact": "Keeps references reviewable.",
                    "source_refs": ["knowledge/sources.json"],
                    "implementation_refs": ["missing.md"],
                }
            ],
        }

        codes = {issue.code for issue in validate_decisions(root, data)}

        self.assertIn("invalid-decision-implementation", codes)


if __name__ == "__main__":
    unittest.main()
