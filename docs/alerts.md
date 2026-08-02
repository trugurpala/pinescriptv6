# Alerts: events, running alerts, and checks

Pine code creates alert **events**. A user creates a **running alert** from those
events in TradingView's Create Alert UI. Keeping those two stages separate makes
configuration mistakes easier to find.

## Choose the event mechanism

| Mechanism | Where it applies | What controls it |
| --- | --- | --- |
| `alert()` | Indicators and strategies | The call site, message, and `freq` argument in Pine code |
| `alertcondition()` | Selectable conditions in indicators | The condition and constant message in code; frequency in the Create Alert UI |
| Strategy order-fill event | Orders filled by the broker emulator | The order call, fill event, and the alert configuration in the UI |

An `alertcondition()` call in a strategy does not create a separately selectable
alert condition. Strategies can instead expose `alert()` events and order-fill
events. See rules `PSAK-ALERT-001` through `PSAK-ALERT-003` and source
`tv-alerts` in the [canonical catalog](../knowledge/catalog.json).

`alert()` uses its `freq` argument. `alertcondition()` has no frequency argument;
the user selects its frequency in the Create Alert UI. A strategy's calculation
schedule can still limit when either kind of code-based event is reached.

For a custom strategy fill message, set `alert_message` on the order-generating
call. Then include `{{strategy.order.alert_message}}` in the Create Alert message.
Both parts are required for that custom text to reach an order-fill alert.

## Treat a running alert as a snapshot

A running alert keeps a creation snapshot of the script, inputs, chart symbol,
and timeframe. Later changes to that context do not update the saved alert.
Recreate the alert after a relevant change and confirm its settings again. This
boundary is recorded by `PSAK-ALERT-004` and source `tv-alerts`.

Bar-close timing can avoid sending an event from an earlier update of the open
realtime bar. It does not establish that the inputs, requested data, stored
state, strategy behavior, or plotted values are stable. Use the
[repainting taxonomy](repainting-taxonomy.md) for that separate review.

## Manual-check checklist

- Confirm the script type and the intended event mechanism.
- Confirm the Create Alert condition, frequency, message, symbol, and timeframe.
- For order fills, trigger a controlled fill and inspect the resolved message.
- Change no input or script version without recreating the running alert.
- Compare realtime-bar and closed-bar behavior for the intended signal.
- Record what TradingView showed, including plan, data, chart, and date.

Local checks are `structural-only`. They can inspect files and registered rules,
but they cannot create a running alert, deliver a notification, or establish
runtime or repaint behavior. Follow the
[TradingView manual verification guide](tradingview-manual-verification.md) for a
stronger, hash-bound file record.
