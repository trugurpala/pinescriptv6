from pathlib import Path
from tempfile import TemporaryDirectory
import json
import shutil
import subprocess
import sys
import unittest

from tools.psaklib.rendering import (
    GENERATED_NOTICE,
    check_outputs,
    render_outputs,
    render_rule_section,
    write_outputs,
)


class RenderingTests(unittest.TestCase):
    def _rule(self, rule_id: str, evidence: str, claim: str):
        return {
            "id": rule_id,
            "title": rule_id,
            "claim": claim,
            "rationale": "Rationale.",
            "scope": "Scoped behavior.",
            "exceptions": ["Exception."],
            "sources": ["source"],
            "evidence": evidence,
            "verified_on": "2026-07-31",
            "status": "active",
            "body": "knowledge/rules/rule.md",
            "tags": ["test"],
        }

    def _repository(self, root: Path):
        (root / "knowledge").mkdir()
        (root / "knowledge/rules").mkdir()
        (root / "agents").mkdir()
        (root / "adapters").mkdir()
        catalog = {
            "schema_version": 1,
            "rules": [self._rule("PSAK-Z", "official", "Later rule.")],
        }
        (root / "knowledge/catalog.json").write_text(
            json.dumps(catalog), encoding="utf-8"
        )
        sources = {
            "schema_version": 1,
            "sources": [
                {
                    "id": "source",
                    "title": "Official source",
                    "url": "https://example.com/reference",
                    "publisher": "Example",
                    "kind": "official-reference",
                    "accessed": "2026-07-31",
                    "applies_to": "Pine Script v6",
                    "locator": "Reference",
                }
            ],
        }
        (root / "knowledge/sources.json").write_text(
            json.dumps(sources), encoding="utf-8"
        )
        (root / "knowledge/rules/rule.md").write_text("# Rule\n", encoding="utf-8")
        (root / "agents/protocol.md").write_text("Protocol body.\n", encoding="utf-8")
        for name in (
            "codex.md",
            "claude.md",
            "gemini.md",
            "cursor.mdc",
            "cline.md",
            "windsurf.md",
            "copilot.md",
            "zed.md",
            "custom-gpt-instructions.md",
            "custom-gpt-knowledge.md",
        ):
            (root / "adapters" / name).write_text(
                "{{NOTICE}}\n# Host\n\n{{PROTOCOL}}\n\n{{RULES}}\n",
                encoding="utf-8",
            )

    def test_rule_section_filters_unverified_and_sorts(self):
        rules = [
            self._rule("PSAK-Z", "official", "Official rule."),
            self._rule("PSAK-X", "unverified", "Hidden rule."),
            self._rule("PSAK-A", "structural-only", "Structural rule."),
        ]

        rendered = render_rule_section(rules)

        self.assertNotIn("Hidden rule", rendered)
        self.assertIn("[structural-only]", rendered)
        self.assertLess(rendered.index("PSAK-A"), rendered.index("PSAK-Z"))

    def test_outputs_are_deterministic_and_include_notice(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            self._repository(root)

            first = render_outputs(root)
            second = render_outputs(root)

            self.assertEqual(first, second)
            self.assertTrue(first)
            self.assertTrue(all(GENERATED_NOTICE in content for content in first.values()))

    def test_check_reports_changed_generated_file(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            self._repository(root)
            written = write_outputs(root)
            written[0].write_text("manual drift\n", encoding="utf-8")

            issues = check_outputs(root)

            self.assertIn("generated-drift", {issue.code for issue in issues})

    def test_renderer_rejects_active_unverified_catalog(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            self._repository(root)
            catalog_path = root / "knowledge/catalog.json"
            catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
            catalog["rules"][0]["evidence"] = "unverified"
            catalog_path.write_text(json.dumps(catalog), encoding="utf-8")

            with self.assertRaisesRegex(ValueError, "undistributable-rule"):
                render_outputs(root)

    def test_rendered_paths_match_golden_adapter_index(self):
        root = Path(__file__).resolve().parents[1]
        index = json.loads(
            (root / "tests/golden/adapter-index.json").read_text(encoding="utf-8")
        )

        actual = [path.as_posix() for path in render_outputs(root)]

        self.assertEqual(actual, index["outputs"])

    def test_render_cli_writes_then_reports_no_drift(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            self._repository(root)
            source_tools = Path(__file__).resolve().parents[1] / "tools"
            shutil.copytree(source_tools, root / "tools", ignore=shutil.ignore_patterns("__pycache__"))

            write = subprocess.run(
                [sys.executable, "tools/psak.py", "render"],
                cwd=root,
                check=False,
                capture_output=True,
                text=True,
            )
            check = subprocess.run(
                [sys.executable, "tools/psak.py", "render", "--check"],
                cwd=root,
                check=False,
                capture_output=True,
                text=True,
            )

            self.assertEqual(write.returncode, 0, write.stderr or write.stdout)
            self.assertEqual(check.returncode, 0, check.stderr or check.stdout)
            self.assertIn("OK: generated outputs are current", check.stdout)


if __name__ == "__main__":
    unittest.main()
