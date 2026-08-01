# TradingView Pine Script v6 Official Watchlist

> Last checked: 2026-04-23
> Source: TradingView Pine Script official release notes and v6 migration guide.

This file tracks official Pine Script v6 changes that should be reflected in this
repository's references, migration notes, examples, and LESSONS_LEARNED memory.

## 2026-01: Footprint Requests

- Official change: `request.footprint()` was added.
- New types: `footprint`, `volume_row`.
- Repo action:
  - Add `request.footprint()` to `reference/functions/request.md`.
  - Add `footprint` and `volume_row` to `reference/types.md`.
  - Consider a future example only after TradingView manual testing.
- Risk level: documentation safe; code examples require TradingView testing.

## 2025-12: Updated Line Wrapping

- Official change: wrapped expressions inside parentheses can now use normal
  indentation, including multiples of four spaces.
- Expressions not enclosed in parentheses still need careful continuation.
- Repo action:
  - Update `writing_scripts/style_guide.md`.
  - Update `LESSONS_LEARNED.md` entry about multiline boolean expressions.
- Risk level: documentation safe.

## 2025-11: `syminfo.isin`

- Official change: `syminfo.isin` was added for ISIN lookup.
- Repo action:
  - Add to `reference/variables.md`.
  - Mention useful cases for cross-exchange symbol identity.
- Risk level: documentation safe.

## 2025-10: `timeframe_bars_back`

- Official change: `time()` and `time_close()` gained `timeframe_bars_back`.
- Repo action:
  - Add to `reference/functions/general.md` or a time/timeframe reference section.
  - Mention interactions with `bars_back`.
- Risk level: documentation safe; examples should be checked in TradingView.

## 2025-09: `plot()` Linestyle

- Official change: `plot()` can use `linestyle` with dotted/dashed/solid line
  styles where supported.
- Repo action:
  - Add to drawing/visual reference docs.
- Risk level: documentation safe.

## 2025-08: Longer Strings and Pine Editor UX

- Official change: maximum string length increased from 4,096 to 40,960 encoded
  characters.
- Official change: Pine Editor moved toward a side-panel workflow with visual
  word wrap support.
- Repo action:
  - Add the string length limit to string/reference guidance.
  - Mention editor word wrap as UX-only; it does not change source structure.
- Risk level: documentation safe.

## 2025-07: Active Inputs and Continuous Futures

- Official change: all `input*()` functions gained an `active` parameter.
- Official change: `syminfo.current_contract` was added for continuous futures.
- Repo action:
  - Add `active` to input guidance.
  - Add `syminfo.current_contract` to `reference/variables.md`.
  - Consider VIOP/global futures guidance where continuous contracts matter.
- Risk level: documentation safe; strategy behavior changes need approval.

## 2025-06: Library `export const`

- Official change: libraries can export user-defined constant variables declared
  with `export const` for supported primitive types.
- Repo action:
  - Add to `concepts/methods.md`, library guidance, or a future library reference
    section if the repo adds reusable Pine libraries.
- Risk level: documentation safe.

## 2025-05: `time_close` on Non-Time-Based Charts

- Official change: `time_close` and `time_close()` have improved behavior on tick
  charts and price-based charts such as Renko, line break, Kagi, point & figure,
  and range charts. On open realtime bars for non-time-based charts, the value is
  `na` until the bar closes.
- Repo action:
  - Add to time/timeframe guidance.
  - Warn strategy authors not to rely on realtime `time_close` values on
    non-time-based charts.
- Risk level: documentation safe; strategy behavior changes require approval.

## 2025-02: `bid` and `ask`

- Official change: `bid` and `ask` built-ins were added for realtime market
  prices on the `1T` timeframe; other timeframes return `na`.
- Repo action:
  - Add to `reference/variables.md`.
  - Warn that they are timeframe-limited and should not be used blindly in
    backtests.
- Risk level: documentation safe; strategy use requires approval.

## Migration Guide Gaps to Track

These official v6 migration topics should stay represented in the repo:

- Dynamic `request.*()` behavior and series string contexts.
- Strict `bool` behavior and lazy `and` / `or`.
- Strategy defaults: `margin_long = 100`, `margin_short = 100`.
- 9000-order trimming and `strategy.closedtrades.first_index`.
- `strategy.exit()` absolute vs relative parameter behavior.
- `timeframe.period` values such as `1D`, `1W`, `1M`.
- Removal of `transp`; use `color.new()`.
- Negative array indexes.
- Dynamic `for` loop boundaries.
- `text_formatting` and `behind_chart`.

## Automation Policy

- Safe documentation updates can be committed automatically.
- Pine strategy/backtest behavior changes require user approval.
- Any change requiring TradingView manual validation must be reported instead of
  silently applied.
