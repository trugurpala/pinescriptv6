<!-- Generated from knowledge/catalog.json and agents/protocol.md.
     Regenerate with: python tools/psak.py render -->
# Pine Script Agent Kit context for Gemini CLI

This file is repository context. Prefer the canonical catalogs when another
instruction surface differs.

# Evidence-first operating protocol

You are working with Pine Script v6. Treat `knowledge/catalog.json` as the
canonical rule index and `knowledge/sources.json` as the canonical source index.

1. Establish the user's indicator, strategy, library, migration, or review intent.
2. Establish timeframe relationships, repaint expectations, strategy execution
   semantics, data availability, and alert/webhook risk before choosing a pattern.
3. Apply only rules whose scope matches. Preserve each rule's exceptions.
4. Cite the registered official source ID when behavior depends on Pine semantics.
5. Label local static results `structural-only`. Do not describe them as compiled,
   TradingView-tested, non-repainting, secure, or production-ready.
6. Treat a hash-matching record in `verification/tradingview.json` as manual
   evidence only for the recorded file and environment.
7. If sources conflict, a source is unavailable, or intent is ambiguous, narrow
   the claim and state what remains unverified.
8. Never expose credentials or place real webhook secrets in code or output.
9. Prefer a minimal change, include a validation path, and separate code-ready,
   tested, published, and live states.

The project is independent and is not affiliated with or endorsed by TradingView.

# Active sourced rules

## PSAK-ALERT-001 — Selectable alertcondition events

alertcondition() calls create separately selectable conditions in indicators; calls in a strategy do not create selectable alertcondition alerts.

**Scope:** Pine v6 indicator and strategy alert API selection.

**Why:** The alert creation UI exposes indicator alertcondition() events separately, while strategy alert choices use other event mechanisms.

**Exceptions:**
- A strategy can still compile with alertcondition(); strategies can expose alert() calls and broker-emulator order-fill events.

**Evidence:** `official` · **Sources:** `tv-alerts` · **Verified:** 2026-08-02

## PSAK-ALERT-002 — Frequency belongs to the alert mechanism

alert() uses its freq argument; alertcondition() has no frequency argument, so its frequency is selected in the Create Alert UI.

**Scope:** Pine v6 alert() and alertcondition() frequency configuration.

**Why:** Frequency is configured through different surfaces for the two alert APIs and must not be assigned to the wrong mechanism.

**Exceptions:**
- A strategy's execution schedule can limit actual call frequency even when freq permits more calls.

**Evidence:** `official` · **Sources:** `tv-alerts`, `tv-execution-model` · **Verified:** 2026-08-02

## PSAK-ALERT-003 — Bind custom messages to order fills

An order-generating call's alert_message is evaluated when its order executes, and an order-fill alert uses it only when the UI message includes {{strategy.order.alert_message}}.

**Scope:** strategy.entry(), strategy.order(), strategy.exit(), and strategy.close() order-fill alerts.

**Why:** The order call and the Create Alert message must be configured together for custom order-fill text to reach the alert.

**Exceptions:**
- Calls without alert_message can yield empty placeholder content; other Create Alert placeholders cannot be used inside alert_message.

**Evidence:** `official` · **Sources:** `tv-alerts` · **Verified:** 2026-08-02

## PSAK-ALERT-004 — Running alerts keep a creation snapshot

A running alert retains the script, inputs, chart symbol, and timeframe saved when it was created; later context changes require recreating the alert.

**Scope:** TradingView script alerts created through the chart UI.

**Why:** TradingView saves a server-side alert snapshot rather than continuously synchronizing it with later chart or script changes.

**Exceptions:**
- Local repository checks cannot inspect or update an already running server-side alert.

**Evidence:** `official` · **Sources:** `tv-alerts` · **Verified:** 2026-08-02

## PSAK-ALERT-005 — Bar-close frequency is not a repaint verdict

alert.freq_once_per_bar_close gates an alert() event to a closing realtime-bar execution; the values and logic feeding the call still require separate repaint analysis.

**Scope:** Claims based on alert.freq_once_per_bar_close or an equivalent bar-close alert configuration.

**Why:** Alert timing controls event delivery, whereas repaint behavior also depends on data, request context, state, and execution semantics.

**Exceptions:**
- Bar-close timing does not establish higher-timeframe confirmation, absence of lookahead, runtime equivalence, or backtest validity.

**Evidence:** `official` · **Sources:** `tv-alerts`, `tv-repainting` · **Verified:** 2026-08-02

## PSAK-BARSTATE-001 — Choose bar states by intent

barstate.islast and barstate.isconfirmed describe different execution states and are not mechanical replacements for one another.

**Scope:** Indicators, libraries, and strategies whose behavior depends on chart update state.

**Why:** The last available chart bar and a confirmed update are different conditions, especially on realtime bars.

**Exceptions:**
- A script can legitimately require both conditions or neither condition.

**Evidence:** `official` · **Sources:** `tv-bar-states` · **Verified:** 2026-07-31

## PSAK-HTF-001 — Confirmed higher-timeframe requests

For confirmed higher-timeframe values, offset the requested expression and pair it with barmerge.lookahead_on.

**Scope:** request.security calls where the requested timeframe is higher than the chart and confirmed values are the intended behavior.

**Why:** This pattern retrieves the last confirmed higher-timeframe value consistently on historical and realtime bars.

**Exceptions:**
- Do not apply the pattern mechanically to lower or equal timeframes, or when developing-bar values are intentional.

**Evidence:** `official` · **Sources:** `tv-other-timeframes` · **Verified:** 2026-07-31

## PSAK-INPUT-001 — Generic and typed inputs

Generic input() remains valid; typed input functions are useful when type-specific parameters or clearer intent are needed.

**Scope:** User-configurable script inputs in Pine Script v6.

**Why:** Pine v6 documents both generic and typed input functions.

**Exceptions:**
- A typed function is required when using parameters that exist only on that typed input.

**Evidence:** `official` · **Sources:** `tv-inputs`, `tv-reference-v6` · **Verified:** 2026-07-31

## PSAK-INPUT-002 — Conditionally active inputs

The active parameter can make supported input controls editable only when a controlling condition is true.

**Scope:** Input functions that expose the active parameter in current Pine v6.

**Why:** The July 2025 release added conditional activation to input controls.

**Exceptions:**
- The parameter changes UI editability, not the runtime type of the input value.

**Evidence:** `official` · **Sources:** `tv-inputs`, `tv-release-notes` · **Verified:** 2026-07-31

## PSAK-MATH-001 — Use documented math.avg

math.avg() is a documented Pine v6 function and can be used when its averaging semantics match the task.

**Scope:** Arithmetic means over arguments accepted by the current math.avg overloads.

**Why:** The v6 reference includes math.avg; banning it produces incorrect guidance.

**Exceptions:**
- Use another averaging function when windowed, weighted, or collection semantics are required.

**Evidence:** `official` · **Sources:** `tv-reference-v6` · **Verified:** 2026-07-31

## PSAK-RELEASE-001 — Current symbol and timeframe metadata

Current Pine v6 includes syminfo.current_contract, syminfo.isin, and timeframe_bars_back additions documented in the 2025 release notes.

**Scope:** Scripts running where the documented symbol or timeframe data is available.

**Why:** These additions reduce custom metadata work and support newer market/timeframe queries.

**Exceptions:**
- Availability and returned values still depend on the chart symbol, market, and timeframe context.

**Evidence:** `official` · **Sources:** `tv-release-notes`, `tv-reference-v6` · **Verified:** 2026-07-31

## PSAK-RELEASE-002 — Footprint requests

request.footprint() and its footprint and volume_row objects expose documented volume-footprint data in Pine v6.

**Scope:** Scripts and accounts for which footprint data is available under TradingView's current product rules.

**Why:** The January 2026 release introduced an official footprint data model.

**Exceptions:**
- Scripts need to handle unavailable data and should not infer account entitlement from static checks.

**Evidence:** `official` · **Sources:** `tv-release-notes`, `tv-reference-v6` · **Verified:** 2026-07-31

## PSAK-RELEASE-003 — UDT collection sorting fields

The sort_field parameter can select a field when sorting supported collections of user-defined type objects.

**Scope:** Supported array and matrix sorting operations on user-defined type objects.

**Why:** The April 2026 release expanded collection sorting for UDT objects.

**Exceptions:**
- Field values and collection element types need to satisfy the documented sorting constraints.

**Evidence:** `official` · **Sources:** `tv-arrays`, `tv-release-notes`, `tv-reference-v6` · **Verified:** 2026-07-31

## PSAK-REPAINT-001 — Classify repainting by mechanism

A repaint review should name the historical/realtime difference—open-bar values, request context, intrabar persistence, past plotting, strategy execution, alert timing, or dataset revision—instead of returning one blanket label.

**Scope:** Repaint assessments for indicators, strategies, libraries, alerts, and visuals.

**Why:** Different repaint mechanisms have different causes, tradeoffs, and mitigations, so one undifferentiated verdict hides material behavior.

**Exceptions:**
- Some differences are intentional and useful but still require disclosure.

**Evidence:** `official` · **Sources:** `tv-repainting`, `tv-execution-model` · **Verified:** 2026-08-02

## PSAK-REPAINT-002 — Treat open-bar cross signals as provisional

Conditions derived from developing high, low, or close values can change before a realtime bar closes; confirmation delays the signal and changes its timing.

**Scope:** Current-chart indicator signals, markers, and alerts based on developing OHLC or derived series.

**Why:** Fluid realtime OHLC values can make a condition appear and disappear before rollback commits the closing-bar state.

**Exceptions:**
- open is fixed during the realtime bar; previous-bar values are confirmed; requested timeframes and varip need separate analysis.

**Evidence:** `official` · **Sources:** `tv-repainting`, `tv-bar-states` · **Verified:** 2026-08-02

## PSAK-STRATEGY-001 — Realtime tick recalculation is a semantic choice

calc_on_every_tick changes strategy recalculation behavior and can produce results that differ after a chart reload.

**Scope:** Strategies that opt into recalculation on realtime ticks.

**Why:** Historical bars do not contain the complete realtime tick sequence available while a bar is open.

**Exceptions:**
- A strategy may intentionally require realtime tick reactions and disclose the repaint/reload implications.

**Evidence:** `official` · **Sources:** `tv-strategies` · **Verified:** 2026-07-31

## PSAK-STRATEGY-002 — Historical tick recalculation

calc_on_every_history_tick enables documented strategy recalculation on available historical intrabar updates for eligible plans on standard chart types.

**Scope:** Pine v6 strategies used by Premium or Ultimate accounts on standard chart types with supported historical data.

**Why:** The July 2026 release added a distinct historical recalculation setting for Premium and Ultimate users on standard charts.

**Exceptions:**
- The setting is unavailable on non-standard chart types; plan availability can change, and behavior still depends on the market and timeframe data.

**Evidence:** `official` · **Sources:** `tv-release-notes`, `tv-strategies` · **Verified:** 2026-07-31

## PSAK-STRATEGY-003 — Separate order creation from order fill

With default settings a strategy calculates once at bar close, and a newly created order is first eligible to fill on the next available tick, commonly the following bar's open.

**Scope:** Default Pine v6 strategy calculation and broker-emulator fill timing.

**Why:** The broker emulator cannot fill a new order before the strategy has created it, so calculation and fill timestamps are distinct by default.

**Exceptions:**
- process_orders_on_close, immediately, intrabar execution, post-fill execution, historical-tick execution, and user property overrides can change timing.

**Evidence:** `official` · **Sources:** `tv-strategies`, `tv-execution-model` · **Verified:** 2026-08-02

## PSAK-STRATEGY-004 — Bound historical intrabar conclusions to emulator data

Default historical fills use chart OHLC values and inferred intrabar paths; higher historical detail can use lower-timeframe data when available, but neither proves real-world fills.

**Scope:** Same-bar sequencing, price-based orders, and historical strategy results.

**Why:** Historical strategy fills are broker-emulator results constrained by the chart and any available lower-timeframe coverage.

**Exceptions:**
- lower-timeframe coverage can be incomplete; chart type, plan, market, and selected detail affect available data.

**Evidence:** `official` · **Sources:** `tv-strategies` · **Verified:** 2026-08-02

## PSAK-STRATEGY-005 — State trading-cost assumptions explicitly

Commission and slippage are absent or zero unless configured; configured values remain simulation assumptions rather than verified future execution costs.

**Scope:** Pine v6 strategy examples and performance interpretations.

**Why:** Unstated or unrealistic cost settings can materially distort simulated strategy results.

**Exceptions:**
- suitable values vary by broker, venue, instrument, size, liquidity, and period; fixed slippage cannot precisely reproduce dynamic fills.

**Evidence:** `official` · **Sources:** `tv-strategies` · **Verified:** 2026-08-02

## PSAK-STRING-001 — Multiline strings

Pine v6 supports multiline string literals under the syntax documented in the April 2026 release notes.

**Scope:** String literals authored for current Pine v6.

**Why:** Multiline source text no longer needs to be represented only through concatenated single-line literals.

**Exceptions:**
- Formatting, escapes, and runtime string-size limits still apply.

**Evidence:** `official` · **Sources:** `tv-release-notes`, `tv-strings` · **Verified:** 2026-07-31

## PSAK-WRAP-001 — Current line wrapping behavior

Current Pine v6 accepts documented wrapping inside parentheses and includes the July 2026 automatic-parentheses update.

**Scope:** Pine v6 source formatted according to the current grammar and release notes.

**Why:** Older indentation-only wrapping warnings can reject syntax that current Pine accepts.

**Exceptions:**
- Code still needs syntactically valid expression boundaries; release-note changes do not make arbitrary line breaks valid.

**Evidence:** `official` · **Sources:** `tv-release-notes`, `tv-reference-v6` · **Verified:** 2026-07-31
