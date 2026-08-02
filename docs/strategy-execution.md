# Strategy calculation, orders, and fills

Read a strategy as three separate events:

1. Pine calculates and evaluates the strategy.
2. The strategy creates an order.
3. TradingView's broker emulator fills or leaves that order pending.

With default settings, a strategy normally calculates at bar close. A newly
created order is first eligible to fill on the next available tick, commonly the
next bar's open. This is the bounded default in `PSAK-STRATEGY-003`, supported by
sources `tv-strategies` and `tv-execution-model` in the
[canonical catalog](../knowledge/catalog.json).

## Settings that can change the sequence

- `calc_on_every_tick` adds realtime recalculations. Historical bars do not
  preserve the complete realtime tick sequence, so reloaded results can differ.
- `calc_on_order_fills` requests another calculation after an emulator fill. It
  can create additional same-bar decisions that need their own plausibility check.
- `calc_on_every_history_tick` uses eligible historical intrabar updates when the
  account, chart type, and available data support them. It is distinct from
  realtime tick recalculation.
- `process_orders_on_close` can make orders eligible for a closing-tick fill.
  The `immediately` parameter on `strategy.close()` and `strategy.close_all()`,
  plus user property overrides, can also alter timing.

These settings are semantic choices, not quality labels. A user can override
script defaults in strategy properties. A plan, chart type, symbol, timeframe,
or dataset can also make a setting or its required data unavailable. Confirm the
effective settings in TradingView.

## Bound the broker-emulator result

Default historical fills use chart OHLC values and an inferred intrabar path.
Bar Magnifier can use available lower-timeframe detail to refine that path. Its
coverage can still be incomplete, and the result remains a broker emulator
simulation rather than evidence of a real fill.

When two orders could fill within one bar, inspect the order type, creation time,
assumed path, and available intrabar coverage. Do not infer an unseen same-bar
sequence from the final OHLC values alone. See `PSAK-STRATEGY-004` and source
`tv-strategies`.

State commission and slippage explicitly. They are absent or zero unless
configured, and configured values remain assumptions about venue, instrument,
size, liquidity, and period. Sizing, sessions, gaps, and stop or target anchors
also change simulated results.

On a non-standard chart, synthetic chart prices can differ from executable market
prices. Check the chart type before interpreting fills or performance.

Local validation is `structural-only`. It does not reproduce TradingView's
effective settings, data coverage, broker emulator, chart executions, or future
fills. Use the [backtesting checklist](backtesting-realism.md) and record the
required TradingView checks separately.
