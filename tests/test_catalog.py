from pathlib import Path
from tempfile import TemporaryDirectory
import json
import unittest

from tools.psaklib.validation import validate_catalog, validate_sources


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.source = {
            "id": "tv-reference-v6",
            "title": "Pine Script v6 reference",
            "url": "https://www.tradingview.com/pine-script-reference/v6/",
            "publisher": "TradingView",
            "kind": "official-reference",
            "accessed": "2026-07-31",
            "applies_to": "Pine Script v6",
            "locator": "Reference manual",
        }

    def _valid_rule(self, body: str = "knowledge/rules/rule.md"):
        return {
            "id": "PSAK-CORE-001",
            "title": "Scoped rule",
            "claim": "Use typed inputs when their constraints improve clarity.",
            "rationale": "Typed inputs expose type-specific parameters.",
            "scope": "User-configurable values with type-specific constraints.",
            "exceptions": ["Generic input() remains valid."],
            "sources": ["tv-reference-v6"],
            "evidence": "official",
            "verified_on": "2026-07-31",
            "status": "active",
            "body": body,
            "tags": ["inputs"],
            "conflict_key": "input-function-choice",
            "claim_value": "typed-when-useful",
        }

    def test_valid_scoped_rule_passes(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            body = root / "knowledge/rules/rule.md"
            body.parent.mkdir(parents=True)
            body.write_text("# Scoped rule\n", encoding="utf-8")

            source_issues, source_ids = validate_sources(
                root, {"schema_version": 1, "sources": [self.source]}
            )
            issues = validate_catalog(
                root,
                {"schema_version": 1, "rules": [self._valid_rule()]},
                source_ids,
            )

            self.assertEqual(source_issues, [])
            self.assertEqual(issues, [])

    def test_unknown_source_and_missing_body_are_rejected(self):
        with TemporaryDirectory() as directory:
            rule = self._valid_rule()
            rule["sources"] = ["missing-source"]

            codes = {
                issue.code
                for issue in validate_catalog(
                    Path(directory), {"schema_version": 1, "rules": [rule]}, {}
                )
            }

            self.assertIn("missing-rule-body", codes)
            self.assertIn("unknown-source", codes)
            self.assertIn("evidence-source-mismatch", codes)

    def test_rule_body_path_must_stay_inside_repository(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            outside = root.parent / "outside-rule.md"
            outside.write_text("# Outside\n", encoding="utf-8")
            source_index = {"tv-reference-v6": "official-reference"}

            for body in (
                "../outside-rule.md",
                str(outside),
                "knowledge\\rules\\rule.md",
            ):
                rule = self._valid_rule(body=body)

                issues = validate_catalog(
                    root,
                    {"schema_version": 1, "rules": [rule]},
                    source_index,
                )

                self.assertIn("invalid-rule-body", {issue.code for issue in issues})

    def test_active_unverified_rule_is_not_distributable(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            body = root / "knowledge/rules/rule.md"
            body.parent.mkdir(parents=True)
            body.write_text("# Rule\n", encoding="utf-8")
            rule = self._valid_rule()
            rule["evidence"] = "unverified"

            codes = {
                issue.code
                for issue in validate_catalog(
                    root,
                    {"schema_version": 1, "rules": [rule]},
                    {"tv-reference-v6": "official-reference"},
                )
            }

            self.assertIn("undistributable-rule", codes)

    def test_stale_absolute_claims_require_scope_and_exceptions(self):
        fixture = Path("tests/fixtures/invalid/stale-absolutes.json")
        rules = json.loads(fixture.read_text(encoding="utf-8"))["rules"]
        with TemporaryDirectory() as directory:
            root = Path(directory)
            for rule in rules:
                candidate = self._valid_rule()
                candidate.update(rule)
                candidate["scope"] = ""
                candidate["exceptions"] = []
                issues = validate_catalog(
                    root,
                    {"schema_version": 1, "rules": [candidate]},
                    {"tv-reference-v6": "official-reference"},
                )
                self.assertIn("unscoped-absolute", {issue.code for issue in issues})

    def test_conflicting_active_claims_are_rejected(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            body = root / "knowledge/rules/rule.md"
            body.parent.mkdir(parents=True)
            body.write_text("# Rule\n", encoding="utf-8")
            first = self._valid_rule()
            second = self._valid_rule()
            second["id"] = "PSAK-CORE-002"
            second["claim_value"] = "never-typed"

            issues = validate_catalog(
                root,
                {"schema_version": 1, "rules": [first, second]},
                {"tv-reference-v6": "official-reference"},
            )

            self.assertIn("conflicting-rules", {issue.code for issue in issues})

    def test_invalid_status_and_empty_active_scope_are_rejected(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            body = root / "knowledge/rules/rule.md"
            body.parent.mkdir(parents=True)
            body.write_text("# Rule\n", encoding="utf-8")
            rule = self._valid_rule()
            rule["status"] = "published"
            rule["scope"] = ""

            issues = validate_catalog(
                root,
                {"schema_version": 1, "rules": [rule]},
                {"tv-reference-v6": "official-reference"},
            )
            codes = {issue.code for issue in issues}

            self.assertIn("invalid-rule-status", codes)
            self.assertIn("missing-rule-scope", codes)

    def test_official_evidence_requires_an_official_source_kind(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            body = root / "knowledge/rules/rule.md"
            body.parent.mkdir(parents=True)
            body.write_text("# Rule\n", encoding="utf-8")
            rule = self._valid_rule()
            rule["sources"] = ["community-post"]

            issues = validate_catalog(
                root,
                {"schema_version": 1, "rules": [rule]},
                {"community-post": "community-lead"},
            )

            self.assertIn("evidence-source-mismatch", {issue.code for issue in issues})

    def test_source_and_rule_fields_require_semantic_types(self):
        with TemporaryDirectory() as directory:
            root = Path(directory)
            body = root / "knowledge/rules/rule.md"
            body.parent.mkdir(parents=True)
            body.write_text("# Rule\n", encoding="utf-8")
            source = dict(self.source)
            source["title"] = ""
            source["publisher"] = None
            source_issues, source_index = validate_sources(
                root, {"schema_version": 1, "sources": [source]}
            )
            rule = self._valid_rule()
            rule["title"] = None
            rule["claim"] = ""
            rule["rationale"] = None
            rule["exceptions"] = "not-a-list"
            rule["tags"] = [""]
            rule_issues = validate_catalog(
                root,
                {"schema_version": 1, "rules": [rule]},
                source_index,
            )

            self.assertIn("invalid-source-field", {issue.code for issue in source_issues})
            self.assertIn("invalid-rule-field", {issue.code for issue in rule_issues})
            self.assertIn("invalid-rule-list", {issue.code for issue in rule_issues})

    def test_reliability_sources_and_rules_are_registered(self):
        root = Path(__file__).resolve().parents[1]
        sources = {
            source["id"]: source
            for source in json.loads(
                (root / "knowledge/sources.json").read_text(encoding="utf-8")
            )["sources"]
        }
        expected_source_urls = {
            "tv-alerts": "https://www.tradingview.com/pine-script-docs/concepts/alerts/",
            "tv-repainting": "https://www.tradingview.com/pine-script-docs/concepts/repainting/",
            "tv-execution-model": "https://www.tradingview.com/pine-script-docs/language/execution-model/",
        }
        for source_id, url in expected_source_urls.items():
            self.assertIn(source_id, sources)
            self.assertEqual(sources[source_id]["url"], url)
            self.assertEqual(sources[source_id]["kind"], "official-guide")
        self.assertEqual(
            sources["tv-execution-model"]["locator"],
            "Executions on historical bars; Executions on realtime bars; Rollback; "
            "Events that trigger script executions",
        )

        rules = {
            rule["id"]: rule
            for rule in json.loads(
                (root / "knowledge/catalog.json").read_text(encoding="utf-8")
            )["rules"]
        }
        expected_rule_sources = {
            "PSAK-ALERT-001": ["tv-alerts"],
            "PSAK-ALERT-002": ["tv-alerts", "tv-execution-model"],
            "PSAK-ALERT-003": ["tv-alerts"],
            "PSAK-ALERT-004": ["tv-alerts"],
            "PSAK-ALERT-005": ["tv-alerts", "tv-repainting"],
            "PSAK-STRATEGY-003": ["tv-strategies", "tv-execution-model"],
            "PSAK-STRATEGY-004": ["tv-strategies"],
            "PSAK-STRATEGY-005": ["tv-strategies"],
            "PSAK-REPAINT-001": ["tv-repainting", "tv-execution-model"],
            "PSAK-REPAINT-002": ["tv-repainting", "tv-bar-states"],
        }
        for rule_id, source_ids in expected_rule_sources.items():
            self.assertIn(rule_id, rules)
            rule = rules[rule_id]
            self.assertEqual(rule["status"], "active")
            self.assertEqual(rule["evidence"], "official")
            self.assertTrue(rule["scope"])
            self.assertTrue(rule["exceptions"])
            self.assertEqual(rule["sources"], source_ids)
            self.assertTrue(rule["conflict_key"])
            self.assertTrue(rule["claim_value"])
            self.assertTrue((root / rule["body"]).is_file())

        self.assertEqual(
            rules["PSAK-STRATEGY-003"]["exceptions"],
            [
                "process_orders_on_close, the immediately parameter on strategy.close() "
                "and strategy.close_all(), intrabar execution, post-fill execution, "
                "historical-tick execution, and user property overrides can change timing."
            ],
        )


if __name__ == "__main__":
    unittest.main()
