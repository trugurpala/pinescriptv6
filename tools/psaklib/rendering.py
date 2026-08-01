from __future__ import annotations

from pathlib import Path

from .validation import Issue, load_json, validate_catalog, validate_sources


GENERATED_NOTICE = """<!-- Generated from knowledge/catalog.json and agents/protocol.md.
     Regenerate with: python tools/psak.py render -->"""

TEMPLATE_OUTPUTS = {
    "adapters/codex.md": ("AGENTS.md",),
    "adapters/claude.md": ("CLAUDE.md",),
    "adapters/gemini.md": ("GEMINI.md",),
    "adapters/cursor.mdc": (".cursor/rules/pinescriptv6.mdc", ".cursorrules"),
    "adapters/cline.md": (".clinerules",),
    "adapters/windsurf.md": (
        ".windsurf/rules/pine-script-agent-kit.md",
        ".windsurfrules",
    ),
    "adapters/copilot.md": (
        ".github/copilot-instructions.md",
        ".github/instructions/pine-script.instructions.md",
    ),
    "adapters/zed.md": (".zed/rules",),
    "adapters/custom-gpt-instructions.md": (
        "generated/custom-gpt/INSTRUCTIONS.md",
    ),
    "adapters/custom-gpt-knowledge.md": ("generated/custom-gpt/KNOWLEDGE.md",),
}


def render_rule_section(rules: list[dict[str, object]]) -> str:
    blocks: list[str] = []
    for rule in sorted(rules, key=lambda item: str(item.get("id", ""))):
        evidence = rule.get("evidence")
        if rule.get("status") != "active" or evidence == "unverified":
            continue
        label = " [structural-only]" if evidence == "structural-only" else ""
        exceptions = rule.get("exceptions", [])
        exception_text = "\n".join(f"- {item}" for item in exceptions)
        source_text = ", ".join(f"`{item}`" for item in rule.get("sources", []))
        blocks.append(
            "\n".join(
                (
                    f"## {rule['id']} — {rule['title']}{label}",
                    "",
                    str(rule["claim"]),
                    "",
                    f"**Scope:** {rule['scope']}",
                    "",
                    f"**Why:** {rule['rationale']}",
                    "",
                    "**Exceptions:**",
                    exception_text,
                    "",
                    f"**Evidence:** `{evidence}` · **Sources:** {source_text} · **Verified:** {rule['verified_on']}",
                )
            )
        )
    return "\n\n".join(blocks).rstrip() + "\n"


def render_outputs(root: Path) -> dict[Path, str]:
    sources = load_json(root / "knowledge/sources.json")
    catalog = load_json(root / "knowledge/catalog.json")
    source_issues, source_ids = validate_sources(root, sources)
    catalog_issues = validate_catalog(root, catalog, source_ids)
    issues = sorted(source_issues + catalog_issues)
    if issues:
        summary = ", ".join(f"{issue.code}:{issue.path}" for issue in issues)
        raise ValueError(f"canonical render inputs are invalid: {summary}")
    protocol = (root / "agents/protocol.md").read_text(encoding="utf-8").strip()
    rules = render_rule_section(catalog["rules"]).strip()
    outputs: dict[Path, str] = {}
    for template_name, output_names in TEMPLATE_OUTPUTS.items():
        template = (root / template_name).read_text(encoding="utf-8")
        content = (
            template.replace("{{NOTICE}}", GENERATED_NOTICE)
            .replace("{{PROTOCOL}}", protocol)
            .replace("{{RULES}}", rules)
            .rstrip()
            + "\n"
        )
        for output_name in output_names:
            outputs[Path(output_name)] = content
    return dict(sorted(outputs.items(), key=lambda item: item[0].as_posix()))


def write_outputs(root: Path) -> list[Path]:
    written: list[Path] = []
    for relative, content in render_outputs(root).items():
        destination = root / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(content, encoding="utf-8", newline="\n")
        written.append(destination)
    return written


def check_outputs(root: Path) -> list[Issue]:
    issues: list[Issue] = []
    for relative, expected in render_outputs(root).items():
        destination = root / relative
        if not destination.is_file():
            issues.append(Issue("missing-generated", relative.as_posix(), "generated output is missing"))
        elif destination.read_text(encoding="utf-8") != expected:
            issues.append(Issue("generated-drift", relative.as_posix(), "generated output differs from canonical data"))
    return sorted(issues)
