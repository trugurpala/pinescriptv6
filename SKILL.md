---
name: pine-script-agent-kit
description: Evidence-first Pine Script v6 guidance for AI coding agents.
license: MIT
metadata:
  maintainer: Uğur Pala <mail@ugurpala.com>
  repository: https://github.com/trugurpala/pinescriptv6
---

# Pine Script Agent Kit

Use the generated host adapter for behavior and the canonical catalogs for facts.

## Required workflow

1. Read `agents/protocol.md`.
2. Match the task to active rules in `knowledge/catalog.json`.
3. Follow each rule's scope and exceptions; cite its source IDs.
4. Check the example hash/evidence in `examples/manifest.json` before reusing it.
5. Call a result `tradingview-verified` only when a current matching record exists
   in `verification/tradingview.json`.
6. Run the offline checks before presenting completion.

```bash
python tools/psak.py validate
python tools/psak.py render --check
python tools/psak.py check
```

Do not infer compilation, non-repainting behavior, profitability, security, or
production readiness from structural checks. The project is independent and is
not affiliated with or endorsed by TradingView.
