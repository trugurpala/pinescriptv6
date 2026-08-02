---
name: pine-script-agent-kit
description: Review, explain, and improve Pine Script v6 code with source-traceable rules, explicit evidence limits, and a separate TradingView manual-check path.
---

<!-- Generated from knowledge/catalog.json and agents/protocol.md.
     Regenerate with: python tools/psak.py render -->

# Pine Script Agent Kit

Use this installed skill for Pine Script v6 reviews, fixes, migrations, indicators,
strategies, alerts, and repaint analysis.

## Required workflow

1. Read `references/agents/protocol.md`.
2. Match the request to active rules in `references/knowledge/catalog.json`.
3. Follow each matching rule's scope and exceptions; cite its registered source IDs
   from `references/knowledge/sources.json` whenever Pine behavior matters.
4. Read the matching explanation in `references/knowledge/rules/` when a rule needs
   context beyond its catalog record.
5. Before reusing a tracked example, check its hash and evidence in
   `references/examples/manifest.json`; call it `tradingview-verified` only when a
   matching record exists in `references/verification/tradingview.json`.
6. When working in a full PSAK checkout, run its offline checks before presenting
   completion. When this installed skill is the only available PSAK surface, state
   that no repository validation was run and do not call the result `structural-only`.
7. Give a separate TradingView manual-check list when the request needs compilation,
   chart behavior, repaint, alert delivery, data access, profitability, or live-use
   evidence.

Do not infer compilation, non-repainting behavior, profitability, security, or
production readiness from this skill or from local structural checks. The project is
independent and is not affiliated with or endorsed by TradingView.
