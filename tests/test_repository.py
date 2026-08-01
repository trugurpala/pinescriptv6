from pathlib import Path
from tempfile import TemporaryDirectory
from urllib.error import URLError
import json
import unittest

from tools.psaklib.links import check_source_links, validate_source_url
from tools.psaklib.validation import validate_critical_files


ROOT = Path(__file__).resolve().parents[1]


class RepositoryTests(unittest.TestCase):
    def test_critical_files_must_exist_and_be_nonempty(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "README.md").write_text("", encoding="utf-8")

            issues = validate_critical_files(root, ("README.md", "LICENSE"))

            self.assertEqual(
                {issue.code for issue in issues},
                {"empty-critical-file", "missing-critical-file"},
            )

    def test_source_url_rejects_credentials_and_sensitive_query(self):
        self.assertIsNotNone(validate_source_url("http://example.com/docs"))
        self.assertIsNotNone(validate_source_url("https://user@example.com/docs"))
        self.assertIsNotNone(validate_source_url("https://example.com/docs?token=secret"))
        self.assertIsNone(validate_source_url("https://example.com/docs?lang=en"))

    def test_link_failure_is_not_reported_as_success(self):
        sources = {
            "schema_version": 1,
            "sources": [{"id": "offline", "url": "https://example.com/docs"}],
        }

        def unavailable(url: str, timeout: int):
            raise URLError(f"offline for {url} after {timeout}")

        results = check_source_links(sources, fetch=unavailable, timeout=1)

        self.assertEqual(results[0].status, "not-verified")

    def test_repository_manifest_matches_discovered_pine_files(self):
        manifest = json.loads((ROOT / "examples/manifest.json").read_text(encoding="utf-8"))
        manifested = {entry["path"] for entry in manifest["examples"]}
        discovered = {
            path.relative_to(ROOT).as_posix()
            for path in ROOT.rglob("*.pine")
            if ".git" not in path.relative_to(ROOT).parts
        }

        self.assertEqual(manifested, discovered)

    def test_quality_workflow_matches_local_offline_gates(self):
        workflow = (ROOT / ".github/workflows/quality.yml").read_text(encoding="utf-8")

        self.assertIn("permissions:\n  contents: read", workflow)
        self.assertIn("python -m unittest discover -s tests -v", workflow)
        self.assertIn("python tools/psak.py check", workflow)
        self.assertNotIn("python tools/psak.py links", workflow)


if __name__ == "__main__":
    unittest.main()
