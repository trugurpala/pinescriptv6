# Global market strategy examples

These ten strategy files extend the market-context examples with trend,
pullback, breakout, VWAP, and session patterns. They are educational starting
points, not optimized systems or recommended risk settings.

## Evidence and limits

The files remain `structural-only` in the repository manifest. A strategy test
result depends on the exact file hash, symbol, feed, session timezone, data
history, commission, slippage, and account context. Repository checks do not
prove a backtest, profitability, non-repainting behavior, or live suitability.

Use the [TradingView manual verification guide](../docs/tradingview-manual-verification.md)
for a human check and the [support guide](../SUPPORT.md) for questions or safe
reporting.

## Strategies

| File | Context | Pattern |
| --- | --- | --- |
| `13_btc_trend_pullback.pine` | BTC/USDT | EMA trend and RSI pullback |
| `14_eth_momentum.pine` | ETH/USDT | Momentum and volume context |
| `15_es_opening_range.pine` | ES S&P 500 | Opening-range pattern |
| `16_nq_vwap_reversion.pine` | NQ Nasdaq | VWAP reversion context |
| `17_gc_gold_trend.pine` | Gold / XAUUSD | Triple EMA trend |
| `18_cl_crude_momentum.pine` | Crude oil | ATR momentum and session |
| `19_eurusd_london_breakout.pine` | EUR/USD | London-session pattern |
| `20_gbpusd_structure.pine` | GBP/USD | Structure and EMA context |
| `21_usdjpy_carry_trend.pine` | USD/JPY | Carry-trend context |
| `22_dax_gap_fade.pine` | DAX | Gap and Xetra-session context |

## Suggested review

1. Confirm the exact file and its manifest hash.
2. Check symbol, session timezone, order sizing, commission, and slippage.
3. Test in Pine Editor and Strategy Tester for the intended context.
4. Treat backtest output as an observation, not a promise of future results.
