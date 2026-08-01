# TradingView Pine Script v6 Official Watchlist

> Last checked: 2026-07-31
> Source: `tv-release-notes` and related official Pine v6 sources in
> `knowledge/sources.json`.

This file tracks official Pine Script v6 changes as a freshness review surface.
It does not create generated guidance by itself. A change becomes public agent
guidance only after the project records scope, exceptions, evidence, and a Divan
decision in the canonical surfaces.

## Current Review State

| Period | Official change area | Decision | Project treatment |
| --- | --- | --- | --- |
| 2025-07 | `input*()` `active`; `syminfo.current_contract` | ADOPT | Covered by scoped catalog rules. |
| 2025-08 | Larger strings and Pine Editor UX | REFERENCE | Useful context; no performance or editor-behavior claim. |
| 2025-09 | `plot()` line styles | REFERENCE | Track as candidate example coverage; do not generate advice until scoped. |
| 2025-10 | `timeframe_bars_back` | ADOPT | Covered by scoped catalog guidance. |
| 2025-11 | `syminfo.isin` | ADOPT | Covered by scoped catalog guidance. |
| 2025-12 | Updated line wrapping | ADAPT | Covered through current syntax guidance with old indentation warnings removed. |
| 2026-01 | `request.footprint()`, `footprint`, `volume_row` | ADAPT | Covered with account, data, and availability caveats. |
| 2026-04 | Multiline strings and UDT `sort_field` | ADOPT | Covered by scoped catalog rules. |
| 2026-07 | `calc_on_every_history_tick`, strategy UI changes, automatic parentheses | ADAPT | Strategy and syntax guidance keeps plan/chart availability caveats. |

The coverage summary in `knowledge/releases/2025-2026.md` is the concise public
version of this table.

## Migration Topics Still Worth Checking

These official v6 migration topics should remain visible during future source
refreshes:

- dynamic `request.*()` behavior and series string contexts;
- strict `bool` behavior and lazy `and` / `or`;
- strategy defaults for `margin_long` and `margin_short`;
- 9000-order trimming and `strategy.closedtrades.first_index`;
- `strategy.exit()` absolute vs relative parameter behavior;
- `timeframe.period` values such as `1D`, `1W`, and `1M`;
- removal of `transp`; use `color.new()`;
- negative array indexes;
- dynamic `for` loop boundaries;
- `text_formatting` and `behind_chart`.

## Automation Policy

- Documentation-only source refreshes can be proposed as normal repository
  changes.
- Pine strategy or backtest behavior changes need a scoped rule, test coverage,
  and explicit review.
- Any claim that requires TradingView manual validation must stay unverified
  until a matching hash-bound record is added to `verification/tradingview.json`.
- If a link check fails because the network or source is unavailable, report the
  source as not verified and preserve the last known scoped rule until review.
