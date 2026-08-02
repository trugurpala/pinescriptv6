# Repainting review is a classification

A repaint review should name the mechanism behind a historical/realtime
difference. A yes/no label hides timing, data, and execution tradeoffs. Some
differences are intentional and useful, but they still need disclosure.

This taxonomy follows `PSAK-REPAINT-001`, `PSAK-REPAINT-002`, and the registered
sources `tv-repainting` and `tv-execution-model` in the
[canonical catalog](../knowledge/catalog.json).

| Mechanism | What to inspect | What you cannot conclude locally |
| --- | --- | --- |
| Developing current-chart values | Uses of current `high`, `low`, `close`, crosses, and open-bar calculations | Whether a provisional value will survive the closing update |
| Confirmed bars | Previous-bar references and the exact meaning of `barstate.isconfirmed` | That confirmation also makes requested contexts or later dataset revisions stable |
| Higher-timeframe developing values/lookahead | Requested timeframe, expression offset, `lookahead`, and whether confirmed HTF data is intended | That one request pattern fits equal, lower, and higher timeframes |
| Lower-timeframe intrabars | Intrabar selection, ordering, array handling, and available coverage | That all lower-timeframe data exists or matches realtime availability |
| `varip`/intrabar state | Rollback, persistence, reset conditions, and reload behavior | Historical reproduction of an unrecorded realtime update sequence |
| future leakage/past plotting | Negative offsets, pivot confirmation, lookahead, and values drawn on earlier bars | That a visually early mark was knowable at that earlier time |
| Historical vs realtime strategy execution | Calculation settings, order creation, fills, and reload behavior | That historical bars reproduce realtime ticks or real executions |
| Alert timing | Event API, frequency, calculation schedule, and running-alert snapshot | That bar-close delivery settles every upstream data or state mechanism |
| Intrabar visuals | Object updates, rollback, `barstate` conditions, and what remains after reload | That a transient drawing will match the historical chart |
| provider/history revisions | Feed changes, back-adjustments, history depth, and chart reloads | That a provider's dataset will remain byte-for-byte unchanged |

## Use timing as a design choice

Signals based on a realtime bar's developing high, low, or close are provisional.
Waiting for confirmation often increases stability but adds latency and changes
the signal's meaning. Previous-bar values and the current bar's open have
different stability properties; requested contexts and intrabar state still need
separate analysis.

Do not treat every repaint mechanism as a bug. State what can change, when it can
change, why the behavior is useful, and what delay or limitation would reduce
the difference.

A repository review can classify source structure and registered claims. It
cannot conclude locally that TradingView history and realtime execution are
equivalent. Report local results as `structural-only`, then provide a separate
manual test for the relevant chart, timeframe, data, and execution settings.
