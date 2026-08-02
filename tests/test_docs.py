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
    "Divan%20ile-%C3%BCretildi",
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

    def test_readmes_use_the_maintenance_first_public_format(self):
        english = (ROOT / "README.md").read_text(encoding="utf-8")
        turkish = (ROOT / "README.tr.md").read_text(encoding="utf-8")

        for badge in REQUIRED_README_BADGES:
            self.assertIn(badge, english)
            self.assertIn(badge, turkish)

        self.assertIn("No failing automation currently requires intervention", english)
        self.assertIn("The project is in maintenance and accepts community contributions", english)
        self.assertIn("What it does", english)
        self.assertIn("What it does not do", english)
        self.assertIn("Free for the community", english)

        self.assertIn("Şu anda müdahale gerektiren hata veya başarısız otomasyon bulunmuyor", turkish)
        self.assertIn("Proje bakım ve topluluk katkısı kabul etme aşamasında", turkish)
        self.assertIn("Ne işe yarar?", turkish)
        self.assertIn("Ne yapmaz?", turkish)
        self.assertIn("Topluluk için ücretsiz", turkish)

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
        self.assertIn("Pine Script Agent Kit", citation)
        self.assertIn("https://github.com/trugurpala/pinescriptv6", citation)

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
        )
        missing = []
        for path in paths:
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
