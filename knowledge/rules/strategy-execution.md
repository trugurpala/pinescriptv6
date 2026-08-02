# Strategy execution

Under default settings, separate the bar-close calculation that creates an order from the next available tick when the broker emulator can first fill it. Settings such as `process_orders_on_close`, the `immediately` parameter on `strategy.close()` and `strategy.close_all()`, intrabar or post-fill recalculation, historical-tick recalculation, and user property overrides can alter that sequence.

Treat historical fills as simulation evidence. Default fills use chart OHLC values and inferred intrabar paths; available lower-timeframe detail can refine the emulator's path without proving real-world execution. State commission and slippage settings explicitly, and present configured costs as assumptions that depend on venue, instrument, liquidity, size, and period.

Local validation is structural-only. It does not reproduce TradingView's broker emulator, chart execution, or future fills.
