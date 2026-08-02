# Coverage

Coverage means a family has active, source-bound guidance in
[`knowledge/catalog.json`](knowledge/catalog.json). Read that canonical JSON for
the current rules and their sources instead of copying a rule count into public
documentation.

## Current source-bound families

- Bar states and the distinction between last-bar and confirmed-bar intent
- Confirmed higher-timeframe requests and their timeframe boundary
- Generic, typed, and conditionally active inputs
- Selected current-release APIs and language behavior
- Alert event selection, frequency, messages, and running-alert snapshots
- Strategy recalculation, order creation, emulator fill timing, and cost assumptions
- Repaint classification across data, state, execution, alerts, visuals, and revisions

These families are useful building blocks, not a complete Pine language or
trading-system specification. Source, account, chart, timeframe, and data
limitations still apply.

## Planned, not currently active

- Type/qualifier system
- `var`/`varip`/`na`, history, and warm-up behavior
- Functions/methods/UDTs/collections
- Sessions/timeframes/symbol/data gaps
- Granular request patterns beyond the current higher-timeframe rule
- Order API/pyramiding/reversal/OCA/risk behavior
- Webhook security
- Full migration matrix

Planned families are not active guidance. Track sequencing in the
[roadmap](ROADMAP.md) and propose a source-bound addition through the
[rule contribution template](docs/rule-contribution-template.md).
