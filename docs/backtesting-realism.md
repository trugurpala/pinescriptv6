# Backtesting realism checklist

Use this checklist before interpreting a TradingView strategy report:

- **Chart type:** Is the chart standard, or does it use synthetic prices?
- **Calculation settings:** Record realtime, post-fill, historical-tick, and
  close-processing choices plus user property overrides.
- **Order type:** Identify market, limit, stop, and stop-limit assumptions.
- **Creation/fill timing:** Separate the calculation, order creation, and first
  eligible emulator fill.
- **Same-bar sequencing:** Explain which intrabar path or data supports the order
  sequence.
- **Bar Magnifier/data coverage:** Record lower-timeframe detail and gaps in its
  available history.
- **Commission:** State the model and value; zero is also an assumption.
- **Slippage:** State the tick assumption and where it applies.
- **Sizing:** Record quantity, equity, currency, leverage, margin, and rounding.
- **Sessions:** Check session filters and order behavior outside the intended hours.
- **Gaps:** Inspect missing bars, session gaps, and requested-data gap handling.
- **Symbol/exchange:** Record the ticker, venue, contract, adjustments, and data
  entitlement.
- **Stop/target anchor:** Say which price, bar, or fill anchors each level.
- **Alert-to-real-order latency:** Separate a Pine event, alert delivery, receiver
  processing, broker acceptance, and eventual fill.

TradingView's broker emulator provides simulated performance under selected data
and assumptions. Bar Magnifier and more detailed settings can change the
simulation, but they do not turn it into future execution evidence. Commission,
slippage, liquidity, latency, and data coverage can differ in live conditions.

Do not present a backtest as proof of future profitability. Local repository
checks are `structural-only`; they do not run the strategy, inspect TradingView
properties, validate market data, or verify fills. Pair this checklist with the
[strategy execution guide](strategy-execution.md) and document manual checks.
