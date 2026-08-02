from pathlib import Path
from tempfile import TemporaryDirectory
from urllib.error import URLError
import json
import re
import unittest

from tools.psaklib.links import check_source_links, validate_source_url
from tools.psaklib.validation import validate_critical_files


ROOT = Path(__file__).resolve().parents[1]


class RepositoryTests(unittest.TestCase):
    def test_codex_skill_bundle_json_is_not_ignored(self):
        ignore = (ROOT / ".gitignore").read_text(encoding="utf-8")

        self.assertIn("!.agents/skills/**/*.json", ignore)

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

    def test_source_link_workflow_is_advisory_network_gate(self):
        workflow = (ROOT / ".github/workflows/source-links.yml").read_text(encoding="utf-8")
        quality = (ROOT / ".github/workflows/quality.yml").read_text(encoding="utf-8")

        self.assertIn("workflow_dispatch:", workflow)
        self.assertIn("schedule:", workflow)
        self.assertIn("python tools/psak.py links", workflow)
        self.assertNotIn("python -m unittest discover -s tests -v", workflow)
        self.assertNotIn("python tools/psak.py check", workflow)
        self.assertNotIn("python tools/psak.py links", quality)

    def test_action_references_are_sha_pinned_and_dependabot_tracks_them(self):
        workflow_paths = (
            ".github/workflows/quality.yml",
            ".github/workflows/source-links.yml",
            "docs/ci-workflow.yml",
        )

        for relative_path in workflow_paths:
            workflow = (ROOT / relative_path).read_text(encoding="utf-8")
            references = re.findall(r"^\s*-?\s*uses:\s+([^\s@]+)@([^\s#]+)", workflow, re.MULTILINE)

            self.assertTrue(references, relative_path)
            for action, revision in references:
                self.assertRegex(
                    revision,
                    r"^[0-9a-f]{40}$",
                    f"{relative_path} must pin {action} to an immutable commit SHA",
                )

        dependabot = (ROOT / ".github/dependabot.yml").read_text(encoding="utf-8")
        self.assertIn('package-ecosystem: "github-actions"', dependabot)
        self.assertIn('directory: "/"', dependabot)
        self.assertIn('interval: "monthly"', dependabot)

    def test_pull_request_template_keeps_tradingview_evidence_hash_bound(self):
        template = (ROOT / ".github/pull_request_template.md").read_text(encoding="utf-8")

        self.assertNotIn("TradingView'da test edildi / Tested in TradingView", template)
        self.assertIn("structural-only", template)
        self.assertIn("verification/tradingview.json", template)
        self.assertIn("examples/manifest.json", template)

    def test_issue_and_question_forms_request_reproducible_context(self):
        bug = (ROOT / ".github/ISSUE_TEMPLATE/bug_report.yml").read_text(encoding="utf-8")
        question = (ROOT / ".github/DISCUSSION_TEMPLATE/questions.yml").read_text(encoding="utf-8")

        for content in (bug, question):
            self.assertIn("timeframe", content.lower())
            self.assertIn("symbol", content.lower())
            self.assertIn("sanitized", content.lower())


if __name__ == "__main__":
    unittest.main()
