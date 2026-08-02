# Adopt Pine Script Agent Kit

Choose the row for your AI tool, place the listed repository file at the stated
location, and run its starter prompt. Keep the files together when a surface uses
more than one file.

| Surface | Source file(s) | Destination or placement | Verification step | Starter prompt |
| --- | --- | --- | --- | --- |
| Portable Agent Skill | `SKILL.md` | Install the complete repository tree under a parent directory named `pine-script-agent-kit` and use it as the skill directory because the skill name must match the directory. `SKILL.md` depends on `agents/protocol.md`, `knowledge/catalog.json`, `knowledge/sources.json`, `examples/manifest.json`, `verification/tradingview.json`, and `tools/psak.py`. | Ask the host to name the loaded skill and run the smoke prompt below. | “Use the Portable Agent Skill to review this Pine v6 code; follow the smoke-prompt evidence format.” |
| Codex | `AGENTS.md` | Keep it at the project root, or at the intended subtree root. | Open the project in Codex and run the smoke prompt from a file under its scope. | “Use the Codex project instructions to review this Pine v6 code; follow the smoke-prompt evidence format.” |
| Claude Code | `CLAUDE.md` | Keep it at the project root. | Start Claude Code in that project and run the smoke prompt. | “Use the Claude Code project guidance to review this Pine v6 code; follow the smoke-prompt evidence format.” |
| Gemini CLI | `GEMINI.md` | Keep it at the project root. | Start Gemini CLI in that project and run the smoke prompt. | “Use the Gemini CLI project guidance to review this Pine v6 code; follow the smoke-prompt evidence format.” |
| Cursor | `.cursor/rules/pinescriptv6.mdc`; `.cursorrules` compatibility | Prefer `.cursor/rules/pinescriptv6.mdc`; use `.cursorrules` only for a host version that needs the compatibility file. | Open a Pine file in Cursor and run the smoke prompt. | “Use the active Cursor Pine rule to review this Pine v6 code; follow the smoke-prompt evidence format.” |
| Cline | `AGENTS.md` | Keep it at the project root. The generated root `.clinerules` file remains a compatibility artifact; Cline also supports additional rules in the `.clinerules/` directory. | Confirm `AGENTS.md` appears in Cline's Rules panel, then run the smoke prompt. | “Use the Cline project rules to review this Pine v6 code; follow the smoke-prompt evidence format.” |
| Windsurf | `AGENTS.md` primary; `.windsurf/rules/pine-script-agent-kit.md` modern bridge; `.windsurfrules` legacy compatibility | Keep `AGENTS.md` at the project root and retain both generated bridges. | Open a Pine file in Windsurf and run the smoke prompt. | “Use the active Windsurf Pine rule to review this Pine v6 code; follow the smoke-prompt evidence format.” |
| GitHub Copilot | `.github/copilot-instructions.md`; `.github/instructions/pine-script.instructions.md` | Keep both under `.github`; the scoped file supplies Pine-specific placement. | Open an in-scope Pine file and run the smoke prompt in Copilot Chat. | “Use the GitHub Copilot repository instructions to review this Pine v6 code; follow the smoke-prompt evidence format.” |
| Zed | `AGENTS.md` | Keep `AGENTS.md` at the project root. | Open the project in Zed and run the smoke prompt from a Pine file. | “Use the Zed project guidance to review this Pine v6 code; follow the smoke-prompt evidence format.” |
| ChatGPT Custom GPT | `generated/custom-gpt/INSTRUCTIONS.md`; `generated/custom-gpt/KNOWLEDGE.md`; `knowledge/catalog.json`; `knowledge/sources.json`; `examples/manifest.json`; `verification/tradingview.json` | Put the instructions text in the GPT instruction field. Upload the knowledge snapshot and four canonical evidence files as knowledge. | Start a new conversation with that GPT and run the smoke prompt. | “Use the ChatGPT Custom GPT knowledge to review this Pine v6 code; follow the smoke-prompt evidence format.” |

## Validate the repository copy

Run these commands before placing or uploading files:

```bash
python tools/psak.py validate
python tools/psak.py render --check
python tools/psak.py check
```

They check the shared data and generated surfaces. File placement and local
validation do not prove that the host loaded or obeyed the files. Host behavior
can change, so the verification step in each row remains necessary.

## Smoke prompt

Paste a small Pine v6 example after this request:

```text
Review this Pine v6 code. State your assumptions first. Cite the exact PSAK rule IDs
and exact source IDs used for Pine behavior. Label local results structural-only.
Give me a separate TradingView manual-check list. Do not infer compilation, runtime,
repaint behavior, alert delivery, market data, or profitability from local checks.
```

Compare the answer with the [source and evidence model](docs/provenance.md). A
host-name claim alone is not proof that it followed the files.

Versioned, tool-specific bundles are planned in the [roadmap](ROADMAP.md); this
repository does not claim a downloadable archive that has not been published.
