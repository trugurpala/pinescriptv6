from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from tools.psaklib.validation import load_json, validate_repository


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


if __name__ == "__main__":
    unittest.main()
