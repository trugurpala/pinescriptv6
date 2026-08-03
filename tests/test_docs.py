from pathlib import Path
import re
import struct
import unittest


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_README_COMMANDS = (
    "python tools/psak.py validate",
    "python tools/psak.py render --check",
    "python tools/psak.py check",
)
REQUIRED_STATUS_PHRASES = ("v1.1.0",)
FORBIDDEN_CLAIMS = (
    "all examples are tested in tradingview",
    "production-ready",
    "guaranteed non-repainting",
)
REQUIRED_LINKS = (
    "LICENSE",
    "SECURITY.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "CHANGELOG.md",
    "SKILL.md",
    "docs/provenance.md",
    "docs/tradingview-manual-verification.md",
)

RELIABILITY_DOCS = (
    "docs/alerts.md",
    "docs/strategy-execution.md",
    "docs/repainting-taxonomy.md",
    "docs/backtesting-realism.md",
)

NEW_PUBLIC_DOCS = (
    "ADOPTION.md",
    "COVERAGE.md",
    "ROADMAP.md",
    "docs/rule-contribution-template.md",
    *RELIABILITY_DOCS,
)

NOT_CHECKED_LABELS = (
    "NOT CHECKED: TradingView compilation",
    "NOT CHECKED: Runtime/chart behavior",
    "NOT CHECKED: Repaint behavior",
    "NOT CHECKED: Alert delivery",
    "NOT CHECKED: Market data",
    "NOT CHECKED: Profitability",
)

PUBLIC_HISTORY_DOCS = (
    "README.md",
    "README.tr.md",
    "CHANGELOG.md",
    "SECURITY.md",
    "LESSONS_LEARNED.md",
    "LLM_MANIFEST.md",
    "docs/provenance.md",
    "docs/custom-gpt/PINE_SCRIPT_V6_KNOWLEDGE_PACK.md",
    "docs/custom-gpt/PINE_SCRIPT_V6_HATA_HAFIZASI_GPT.md",
    "knowledge/lessons/stale-absolutes.md",
)

REQUIRED_README_BADGES = (
    "actions/workflows/quality.yml/badge.svg",
    "img.shields.io/github/v/release/trugurpala/pinescriptv6",
    "License-MIT",
)

EXPLANATORY_ASSETS = (
    ("assets/agent-journey.png", (1280, 720)),
    ("assets/source-provenance.png", (1280, 720)),
)

SUB_READMES = (
    "examples/README.md",
    "global-markets/README.md",
    "global-markets/STRATEGIES_README.md",
    "tradingview-publish/README.md",
    "v5-to-v6-migration/README.md",
    "webhook-templates/README.md",
)

PUBLISH_DESCRIPTIONS = (
    "tradingview-publish/01_fakeout_filter_description.md",
    "tradingview-publish/02_viop_session_description.md",
    "tradingview-publish/03_fakeout_confirmed_strategy_description.md",
)


class DocumentationTests(unittest.TestCase):
    def test_public_reliability_guides_exist_and_readmes_link_them(self):
        english = (ROOT / "README.md").read_text(encoding="utf-8")
        turkish = (ROOT / "README.tr.md").read_text(encoding="utf-8")

        for relative_path in NEW_PUBLIC_DOCS:
            self.assertTrue((ROOT / relative_path).is_file(), relative_path)
        for relative_path in (*RELIABILITY_DOCS, "ADOPTION.md", "COVERAGE.md", "ROADMAP.md"):
            self.assertIn(relative_path, english)
            self.assertIn(relative_path, turkish)

    def test_readmes_show_the_complete_offline_check_boundary(self):
        for relative_path in ("README.md", "README.tr.md"):
            content = (ROOT / relative_path).read_text(encoding="utf-8")
            self.assertIn("OK: all offline checks passed", content, relative_path)
            for label in NOT_CHECKED_LABELS:
                self.assertIn(label, content, relative_path)

    def test_readmes_explain_the_standard_codex_skill_install_path(self):
        english = (ROOT / "README.md").read_text(encoding="utf-8")
        turkish = (ROOT / "README.tr.md").read_text(encoding="utf-8")

        installer_url = (
            "$skill-installer https://github.com/trugurpala/pinescriptv6/"
            "tree/main/.agents/skills/pine-script-agent-kit"
        )
        for content in (english, turkish):
            self.assertIn(".agents/skills/pine-script-agent-kit/SKILL.md", content)
            self.assertIn(installer_url, content)
            self.assertIn("$pine-script-agent-kit", content)

        self.assertIn("does not prove that a host loaded", english)
        self.assertIn("hostun bu beceriyi yüklediğini", turkish)
        self.assertIn("kanıtlamaz", turkish)

    def test_adoption_covers_supported_surfaces_and_local_evidence_boundary(self):
        path = ROOT / "ADOPTION.md"
        self.assertTrue(path.is_file(), "ADOPTION.md")
        content = path.read_text(encoding="utf-8")
        expected_paths = {
            "Portable Agent Skill": ("SKILL.md",),
            "Codex Desktop skill": (
                ".agents/skills/pine-script-agent-kit/SKILL.md",
                ".agents/skills/pine-script-agent-kit/agents/openai.yaml",
            ),
            "Codex": ("AGENTS.md",),
            "Claude Code": ("CLAUDE.md",),
            "Gemini CLI": ("GEMINI.md",),
            "Cursor": (".cursor/rules/pinescriptv6.mdc", ".cursorrules"),
            "Cline": ("AGENTS.md",),
            "Devin": ("AGENTS.md",),
            "Windsurf": (
                "AGENTS.md",
                ".windsurf/rules/pine-script-agent-kit.md",
                ".windsurfrules",
            ),
            "GitHub Copilot": (
                ".github/copilot-instructions.md",
                ".github/instructions/pine-script.instructions.md",
            ),
            "Zed": (".cursorrules",),
            "ChatGPT Custom GPT": (
                "generated/custom-gpt/INSTRUCTIONS.md",
                "generated/custom-gpt/KNOWLEDGE.md",
                "knowledge/catalog.json",
                "knowledge/sources.json",
                "examples/manifest.json",
                "verification/tradingview.json",
            ),
        }
        table_lines = [line for line in content.splitlines() if line.startswith("|")]
        data_rows = []
        for line in table_lines:
            cells = [cell.strip() for cell in line.strip("|").split("|")]
            if len(cells) != 5 or cells[0] in ("Surface", "---"):
                continue
            data_rows.append(cells)

        self.assertEqual(len(data_rows), 12)
        rows_by_surface = {row[0]: row for row in data_rows}
        self.assertEqual(set(rows_by_surface), set(expected_paths))
        for surface, paths in expected_paths.items():
            source, placement, verification, starter_prompt = rows_by_surface[surface][1:]
            for canonical_path in paths:
                self.assertIn(canonical_path, source, surface)
            self.assertTrue(placement, surface)
            self.assertTrue(verification, surface)
            self.assertTrue(starter_prompt, surface)

        portable_placement = rows_by_surface["Portable Agent Skill"][2]
        for phrase in (
            "complete repository tree",
            "parent directory named `pine-script-agent-kit`",
            "name must match the directory",
            "agents/protocol.md",
            "knowledge/catalog.json",
            "knowledge/sources.json",
            "examples/manifest.json",
            "verification/tradingview.json",
            "tools/psak.py",
        ):
            self.assertIn(phrase, portable_placement)

        codex_skill_source, codex_skill_placement, codex_skill_verification, codex_skill_prompt = rows_by_surface["Codex Desktop skill"][1:]
        self.assertIn(
            "$skill-installer https://github.com/trugurpala/pinescriptv6/"
            "tree/main/.agents/skills/pine-script-agent-kit",
            codex_skill_placement,
        )
        self.assertIn("restart Codex", codex_skill_placement)
        self.assertIn("pine-script-agent-kit", codex_skill_source)
        self.assertIn("loaded skill", codex_skill_verification)
        self.assertIn("Pine Script v6", codex_skill_prompt)

        cline_source, cline_placement, cline_verification, _ = rows_by_surface["Cline"][1:]
        self.assertIn("AGENTS.md", cline_source)
        self.assertIn("project root", cline_placement)
        self.assertIn("Rules panel", cline_verification)
        self.assertIn("smoke prompt", cline_verification)

        devin_source, devin_placement, devin_verification, devin_prompt = (
            rows_by_surface["Devin"][1:]
        )
        self.assertEqual(devin_source, "`AGENTS.md`")
        self.assertIn("project root", devin_placement)
        self.assertIn("Accessed Knowledge", devin_verification)
        self.assertIn("repo knowledge", devin_verification)
        self.assertIn("smoke prompt", devin_verification)
        self.assertIn("Devin", devin_prompt)

        windsurf_source, windsurf_placement, _, _ = rows_by_surface["Windsurf"][1:]
        self.assertIn("primary", windsurf_source)
        self.assertIn("fallback workspace-rule bridge", windsurf_source)
        self.assertNotIn("modern", windsurf_source)
        self.assertIn("legacy", windsurf_source)
        self.assertIn("root", windsurf_placement)

        zed_source, zed_placement, _, _ = rows_by_surface["Zed"][1:]
        self.assertEqual(zed_source, "`.cursorrules`")
        self.assertIn("project root", zed_placement)
        self.assertIn("first matching", zed_placement)
        self.assertIn("precedes `AGENTS.md`", zed_placement)
        self.assertIn("selected supported surface", zed_placement)
        self.assertNotIn("AGENTS.md", zed_source)
        self.assertNotIn(".zed/rules", " | ".join(rows_by_surface["Zed"]))
        for command in REQUIRED_README_COMMANDS:
            self.assertIn(command, content)
        normalized_content = " ".join(content.split())
        for phrase in (
            "assumptions",
            "exact PSAK rule IDs",
            "exact source IDs",
            "structural-only",
            "separate TradingView manual-check list",
            "File placement and local validation do not prove that the host loaded or obeyed",
        ):
            self.assertIn(phrase, normalized_content)

    def test_rule_contribution_template_has_required_fields_and_public_links(self):
        template_path = "docs/rule-contribution-template.md"
        path = ROOT / template_path
        self.assertTrue(path.is_file(), template_path)
        template = path.read_text(encoding="utf-8")
        contributing = (ROOT / "CONTRIBUTING.md").read_text(encoding="utf-8")
        pull_request = (ROOT / ".github/PULL_REQUEST_TEMPLATE.md").read_text(encoding="utf-8")
        fields = (
            "Rule ID",
            "Claim",
            "Scope",
            "Rationale",
            "Exceptions",
            "Official source ID",
            "Official source locator",
            "Verified date",
            "Example",
            "Counterexample",
            "Local test",
            "TradingView manual verification required",
        )

        for field in fields:
            self.assertEqual(template.count(f"## {field}"), 1, field)
        self.assertIn(template_path, contributing)
        durable_url = (
            "https://github.com/trugurpala/pinescriptv6/blob/main/"
            "docs/rule-contribution-template.md"
        )
        self.assertIn(durable_url, pull_request)
        self.assertNotIn("../docs/rule-contribution-template.md", pull_request)

    def test_reliability_guides_cover_apis_settings_and_evidence_limits(self):
        for relative_path in RELIABILITY_DOCS:
            self.assertTrue((ROOT / relative_path).is_file(), relative_path)
        alerts = (ROOT / "docs/alerts.md").read_text(encoding="utf-8")
        strategy = (ROOT / "docs/strategy-execution.md").read_text(encoding="utf-8")
        repainting = (ROOT / "docs/repainting-taxonomy.md").read_text(encoding="utf-8")
        backtesting = (ROOT / "docs/backtesting-realism.md").read_text(encoding="utf-8")

        for term in (
            "alert()",
            "alertcondition()",
            "alert_message",
            "{{strategy.order.alert_message}}",
            "creation snapshot",
            "structural-only",
            "Manual-check checklist",
        ):
            self.assertIn(term, alerts)
        for term in (
            "calc_on_every_tick",
            "calc_on_order_fills",
            "calc_on_every_history_tick",
            "process_orders_on_close",
            "Bar Magnifier",
            "broker emulator",
            "non-standard chart",
            "TradingView",
        ):
            self.assertIn(term, strategy)
        self.assertIn("`immediately` parameter on `strategy.close()`", strategy)
        self.assertIn("`strategy.close_all()`", strategy)
        self.assertNotIn("An order call's `immediately` behavior", strategy)
        for term in (
            "classification",
            "varip",
            "future leakage",
            "provider/history revisions",
            "latency",
            "cannot conclude locally",
        ):
            self.assertIn(term, repainting)
        for term in (
            "**Same-bar sequencing:**",
            "**Commission:**",
            "**Slippage:**",
            "**Alert-to-real-order latency:**",
            "future execution",
            "profitability",
        ):
            self.assertIn(term, backtesting)

    def test_new_public_docs_avoid_unsupported_claims(self):
        forbidden = (
            "alertcondition() does not compile",
            "backtest reliable",
            "no repainting",
            "production-ready",
            "guaranteed profitable",
            "guarantees profitability",
        )

        for relative_path in NEW_PUBLIC_DOCS:
            path = ROOT / relative_path
            self.assertTrue(path.is_file(), relative_path)
            lowered = path.read_text(encoding="utf-8").lower()
            for claim in forbidden:
                self.assertNotIn(claim, lowered, relative_path)

    def test_readmes_share_status_commands_and_core_links(self):
        english = (ROOT / "README.md").read_text(encoding="utf-8")
        turkish = (ROOT / "README.tr.md").read_text(encoding="utf-8")

        for content in (english, turkish):
            for command in REQUIRED_README_COMMANDS:
                self.assertIn(command, content)
            for phrase in REQUIRED_STATUS_PHRASES:
                self.assertIn(phrase, content)
            for link in REQUIRED_LINKS:
                self.assertIn(link, content)
            lowered = content.lower()
            for claim in FORBIDDEN_CLAIMS:
                self.assertNotIn(claim, lowered)
        self.assertIn("not affiliated with or endorsed by TradingView", english)
        self.assertIn(
            "TradingView ile bağlantılı değildir ve TradingView tarafından onaylanmamıştır",
            turkish,
        )
        self.assertIn("README.tr.md", english)
        self.assertIn("README.md", turkish)
        self.assertIn("The current release is **v1.1.0**", english)
        self.assertIn("Güncel sürüm **v1.1.0**", turkish)

    def test_readmes_label_the_displayed_output_as_the_final_check_ending(self):
        english = (ROOT / "README.md").read_text(encoding="utf-8")
        turkish = (ROOT / "README.tr.md").read_text(encoding="utf-8")

        self.assertIn(
            "The final `python tools/psak.py check` command ends with:", english
        )
        self.assertNotIn("Expected result:", english)
        self.assertIn(
            "Son `python tools/psak.py check` komutunun çıktısı şu satırlarla biter:",
            turkish,
        )
        self.assertNotIn("Beklenen sonuç:", turkish)

    def test_readmes_map_zed_precedence_and_list_devin(self):
        english = (ROOT / "README.md").read_text(encoding="utf-8")
        turkish = (ROOT / "README.tr.md").read_text(encoding="utf-8")

        for content in (english, turkish):
            self.assertIn("| Zed | `.cursorrules` |", content)
            self.assertNotIn("| Zed | `AGENTS.md`", content)
            self.assertIn("| Devin | `AGENTS.md` |", content)
            self.assertIn("Devin", "\n".join(content.splitlines()[:30]))

    def test_readmes_use_the_maintenance_first_public_format(self):
        english = (ROOT / "README.md").read_text(encoding="utf-8")
        turkish = (ROOT / "README.tr.md").read_text(encoding="utf-8")

        self.assertNotIn("Built with Divan", english)
        self.assertNotIn("Divan ile üretildi", turkish)
        self.assertNotIn("Divan%20ile-%C3%BCretildi", english + turkish)
        self.assertNotIn("[!IMPORTANT]", turkish)
        self.assertIn("> **Önemli sınır**", turkish)
        self.assertNotIn("Ã", turkish)

        for badge in REQUIRED_README_BADGES:
            self.assertIn(badge, english)
            self.assertIn(badge, turkish)

        self.assertNotIn("No failing automation currently requires intervention", english)
        self.assertIn("This project is maintained and accepts community contributions", english)
        self.assertIn("What it does", english)
        self.assertIn("What it does not do", english)
        self.assertIn("Free for the community", english)

        self.assertNotIn("Şu anda müdahale gerektiren hata veya başarısız otomasyon bulunmuyor", turkish)
        self.assertIn("Proje bakımdadır ve topluluk katkılarını kabul eder", turkish)
        self.assertIn("Ne işe yarar?", turkish)
        self.assertIn("Ne yapmaz?", turkish)
        self.assertIn("Topluluk için ücretsiz", turkish)

    def test_skill_frontmatter_and_adoption_surfaces_follow_host_contracts(self):
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(skill.startswith("---\n"))
        frontmatter = skill.split("---", 2)[1]

        self.assertIn("name: pine-script-agent-kit", frontmatter)
        self.assertIn("description: Evidence-first Pine Script v6 guidance", frontmatter)
        self.assertNotIn("license:", frontmatter)
        self.assertNotIn("metadata:", frontmatter)
        self.assertNotRegex(frontmatter, r"(?m)^maintainer:")
        self.assertNotRegex(frontmatter, r"(?m)^repository:")

        scoped = (ROOT / ".github/instructions/pine-script.instructions.md").read_bytes()
        repository_wide = (ROOT / ".github/copilot-instructions.md").read_bytes()
        self.assertTrue(scoped.startswith(b'---\napplyTo: "**/*.pine"\n---\n'))
        self.assertFalse(repository_wide.startswith(b"---"))

    def test_roadmap_uses_durable_unreleased_status(self):
        roadmap = (ROOT / "ROADMAP.md").read_text(encoding="utf-8")

        self.assertNotIn("current branch", roadmap.lower())
        self.assertIn("Unreleased", roadmap)
        self.assertIn("CHANGELOG.md", roadmap)
        self.assertIn("v1.1.0", roadmap)

    def test_social_preview_is_approved_png_size(self):
        path = ROOT / "assets/social-preview.png"
        data = path.read_bytes()

        self.assertEqual(data[:8], b"\x89PNG\r\n\x1a\n")
        self.assertEqual(data[12:16], b"IHDR")
        width, height = struct.unpack(">II", data[16:24])
        self.assertEqual((width, height), (1280, 640))

        source = (ROOT / "assets/social-preview.svg").read_text(encoding="utf-8")
        self.assertIn('width="1280" height="640"', source)
        self.assertIn("Pine Script Agent Kit", source)
        self.assertIn("VERIFIED KNOWLEDGE", source)
        self.assertNotIn("LESSONS_LEARNED", source)

    def test_readme_language_and_attribution_surfaces_are_consistent(self):
        english = (ROOT / "README.md").read_text(encoding="utf-8")
        turkish = (ROOT / "README.tr.md").read_text(encoding="utf-8")

        self.assertIn("assets/social-preview.png", english)
        self.assertIn("assets/social-preview.tr.png", turkish)
        self.assertIn("> **Önemli sınır**", turkish)
        self.assertNotIn("[!IMPORTANT]", turkish)
        self.assertNotIn("Built with Divan", english)
        self.assertNotIn("Divan ile üretildi", turkish)

        path = ROOT / "assets/social-preview.tr.png"
        data = path.read_bytes()
        self.assertEqual(data[:8], b"\x89PNG\r\n\x1a\n")
        self.assertEqual(data[12:16], b"IHDR")
        width, height = struct.unpack(">II", data[16:24])
        self.assertEqual((width, height), (1280, 640))

    def test_readmes_guide_people_before_exposing_repository_internals(self):
        english = (ROOT / "README.md").read_text(encoding="utf-8")
        turkish = (ROOT / "README.tr.md").read_text(encoding="utf-8")

        self.assertIn("Start with your Pine task", english)
        self.assertIn("How an AI agent uses this kit", english)
        self.assertIn("What the answer should tell you", english)

        self.assertIn("Pine görevinle başla", turkish)
        self.assertIn("Bir yapay zekâ ajanı bu paketi nasıl kullanır?", turkish)
        self.assertIn("Yanıt sana ne söylemeli?", turkish)

        for path, _ in EXPLANATORY_ASSETS:
            self.assertIn(path, english)
            self.assertIn(path, turkish)

        opening = "\n".join(turkish.splitlines()[:90]).lower()
        for machine_word in (
            "provenans",
            "telemetry",
            "credential",
            "runtime",
            "structural-only",
        ):
            self.assertNotIn(machine_word, opening)

    def test_explanatory_assets_and_durable_writing_guidance_exist(self):
        for relative_path, expected_size in EXPLANATORY_ASSETS:
            path = ROOT / relative_path
            self.assertTrue(path.is_file(), relative_path)
            data = path.read_bytes()
            self.assertEqual(data[:8], b"\x89PNG\r\n\x1a\n")
            self.assertEqual(data[12:16], b"IHDR")
            self.assertEqual(struct.unpack(">II", data[16:24]), expected_size)

        style = (ROOT / "docs/writing-style.md").read_text(encoding="utf-8")
        self.assertIn("TDK_Yazim_Kurallari_200319.pdf", style)
        self.assertIn("İnsan önce, sistem sonra", style)
        self.assertIn("Doğal Türkçe", style)

        self.assertFalse((ROOT / ".divan").exists())

    def test_public_snapshot_uses_current_release_contract(self):
        for relative_path in PUBLIC_HISTORY_DOCS:
            content = (ROOT / relative_path).read_text(encoding="utf-8")
            self.assertIsNone(
                re.search(r"\b[0-9a-f]{40}\b", content),
                relative_path,
            )

        for private_path in (
            ".divan",
            "BLUEPRINT.md",
            "docs/audits",
            "docs/superpowers",
        ):
            self.assertFalse((ROOT / private_path).exists(), private_path)

    def test_public_docs_do_not_publish_version_two(self):
        changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
        citation = (ROOT / "CITATION.cff").read_text(encoding="utf-8")

        self.assertNotIn("## [2.0.0]", changelog)
        self.assertIn("## [Unreleased]", changelog)
        self.assertIn("## [1.1.0] — 2026-08-02", changelog)
        self.assertIn("Pine Script Agent Kit", citation)
        self.assertIn("version: 1.1.0", citation)
        self.assertIn("date-released: 2026-08-02", citation)
        self.assertIn("https://github.com/trugurpala/pinescriptv6", citation)

    def test_v110_changelog_records_host_and_session_alert_hardening(self):
        changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
        v110 = changelog.split("## [1.1.0]", 1)[1].split("## [1.0.0]", 1)[0]

        self.assertIn("Windsurf", v110)
        self.assertIn("host adoption", v110)
        self.assertIn("session-close alert", v110)
        self.assertIn("first-match precedence", v110)
        self.assertIn("entry signals", v110)

    def test_manual_tradingview_verification_guide_is_linked_without_overclaiming(self):
        english = (ROOT / "README.md").read_text(encoding="utf-8")
        turkish = (ROOT / "README.tr.md").read_text(encoding="utf-8")
        contributing = (ROOT / "CONTRIBUTING.md").read_text(encoding="utf-8")
        guide = (ROOT / "docs/tradingview-manual-verification.md").read_text(encoding="utf-8")

        for content in (english, turkish, contributing):
            self.assertIn("docs/tradingview-manual-verification.md", content)

        self.assertIn("structural-only", guide)
        self.assertIn("tradingview-verified", guide)
        self.assertIn("verification/tradingview.json", guide)
        self.assertIn("examples/manifest.json", guide)
        self.assertIn("Do not record", guide)

    def test_support_guide_is_linked_and_routes_sensitive_questions(self):
        english = (ROOT / "README.md").read_text(encoding="utf-8")
        turkish = (ROOT / "README.tr.md").read_text(encoding="utf-8")
        contributing = (ROOT / "CONTRIBUTING.md").read_text(encoding="utf-8")
        support = (ROOT / "SUPPORT.md").read_text(encoding="utf-8")

        for content in (english, turkish, contributing):
            self.assertIn("SUPPORT.md", content)

        for link in (
            "github.com/trugurpala/pinescriptv6/discussions",
            "github.com/trugurpala/pinescriptv6/issues/new/choose",
            "SECURITY.md",
            "docs/tradingview-manual-verification.md",
        ):
            self.assertIn(link, support)

        self.assertIn("Do not post private code", support)
        self.assertIn("Özel kodu", support)

    def test_subdirectory_readmes_are_user_facing_and_evidence_bounded(self):
        forbidden = (
            "copy-paste ready",
            "errors auto-saved",
            "Premium or higher required",
            "ready-to-use trading systems",
        )

        for relative_path in SUB_READMES:
            content = (ROOT / relative_path).read_text(encoding="utf-8")
            self.assertIn("structural-only", content, relative_path)
            self.assertIn("SUPPORT.md", content, relative_path)
            self.assertIn("tradingview-manual-verification.md", content, relative_path)
            lowered = content.lower()
            for claim in forbidden:
                self.assertNotIn(claim.lower(), lowered, relative_path)

    def test_publish_descriptions_keep_publication_and_signal_claims_bounded(self):
        for relative_path in PUBLISH_DESCRIPTIONS:
            content = (ROOT / relative_path).read_text(encoding="utf-8")
            self.assertIn("structural-only", content, relative_path)
            self.assertIn("Evidence boundary", content, relative_path)
            self.assertNotIn("PUBLISHED", content, relative_path)
            self.assertNotIn("gerçekçi backtest", content.lower(), relative_path)

    def test_legacy_custom_gpt_docs_are_safe_bridges(self):
        paths = (
            ROOT / "docs/custom-gpt/PINE_SCRIPT_V6_KNOWLEDGE_PACK.md",
            ROOT / "docs/custom-gpt/PINE_SCRIPT_V6_HATA_HAFIZASI_GPT.md",
        )
        forbidden = (
            "math.avg() → yok",
            "math.avg() removed",
            "asla bare `input()`",
            "Never use v5 syntax: study(), security(), bare input() are forbidden.",
            "calc_on_every_tick=true` → backtest bozar",
        )

        for path in paths:
            content = path.read_text(encoding="utf-8")
            self.assertIn("generated/custom-gpt/", content)
            for claim in forbidden:
                self.assertNotIn(claim, content)

    def test_public_relative_markdown_links_resolve(self):
        paths = (
            ROOT / "README.md",
            ROOT / "README.tr.md",
            ROOT / "CONTRIBUTING.md",
            ROOT / "SECURITY.md",
            ROOT / "SUPPORT.md",
            ROOT / "examples/README.md",
            ROOT / "global-markets/README.md",
            ROOT / "tradingview-publish/README.md",
            ROOT / "v5-to-v6-migration/README.md",
            ROOT / "webhook-templates/README.md",
            ROOT / "docs/provenance.md",
            ROOT / "docs/custom-gpt/PINE_SCRIPT_V6_KNOWLEDGE_PACK.md",
            ROOT / "docs/custom-gpt/PINE_SCRIPT_V6_HATA_HAFIZASI_GPT.md",
            *(ROOT / relative_path for relative_path in NEW_PUBLIC_DOCS),
        )
        missing = []
        for path in paths:
            self.assertTrue(path.is_file(), str(path.relative_to(ROOT)))
            content = path.read_text(encoding="utf-8")
            for target in re.findall(r"\[[^]]+\]\(([^)]+)\)", content):
                clean = target.split("#", 1)[0]
                if not clean or "://" in clean or clean.startswith("mailto:"):
                    continue
                destination = (path.parent / clean).resolve()
                if not destination.exists():
                    missing.append(f"{path.relative_to(ROOT)} -> {target}")

        self.assertEqual(missing, [])


if __name__ == "__main__":
    unittest.main()
