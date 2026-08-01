# LLM manifest compatibility bridge

The canonical machine-readable routing data is now:

- `knowledge/sources.json` — source registry;
- `knowledge/catalog.json` — scoped rules and evidence;
- `examples/manifest.json` — Pine file status and hashes;
- `verification/tradingview.json` — manual hash-bound records;
- `governance/decisions.json` — project decisions using ADOPT, ADAPT,
  REFERENCE, and REJECT;
- `agents/protocol.md` — tool-neutral behavior.

Generated tool instructions live in `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`,
`.cursor/rules/`, `.clinerules`, `.windsurf/rules/`, `.github/`, `.zed/rules`,
and `generated/custom-gpt/`.

Do not add independent Pine claims to this bridge. Register a source and rule,
add a regression test, then run:

```bash
python tools/psak.py validate
python tools/psak.py render
python tools/psak.py render --check
```
