# Pine Script v6 examples

This folder contains 32 educational indicator and strategy examples for Pine
Script v6. They are useful starting points for an AI-assisted review or a
manual TradingView experiment.

## Evidence and limits

Every example is tracked in [`manifest.json`](manifest.json). Most entries are
`structural-only`; one entry has a dated, hash-bound `tradingview-verified`
Pine Editor record. The repository confirms each file, its SHA-256, and its v6
header. A manual record establishes only its stated check for the exact hash
and environment. It does not prove runtime behavior, non-repainting behavior,
profitability, security, alert delivery, or live-trading suitability.

Before making a stronger claim, follow the [TradingView manual verification guide](../docs/tradingview-manual-verification.md). Never paste credentials or private code into an issue or pull request; see the [support guide](../SUPPORT.md).

## Disclosure checklist

Review each example against this checklist before adapting it:

- Evidence status
- Signal timing
- Requested timeframes and confirmation
- Strategy calculation settings
- Order fill timing
- Commission and slippage
- Stop/target anchor
- Alert setup

The two EMA examples below are the first hardened slice. The other examples in
the 56-file manifest do not yet carry equivalent disclosure detail.

| File | Current-code disclosure |
| --- | --- |
| `indicators/01_ema_cross.pine` | Structural-only chart-timeframe indicator. Open realtime-bar crosses and markers can change before close. `alertcondition()` exposes selectable conditions; Create Alert controls frequency, and bar-close delivery is only a timing choice. |
| `strategies/01_ema_cross_strategy.pine` | Structural-only chart-timeframe strategy using default recalculation/order processing. Signals calculate at bar close and orders are normally first eligible on the next tick. Commission is fixed at 0.1%, slippage is unset, exits anchor to signal-bar close plus/minus ATR, and no alert workflow is configured. |

## Indicators

| File | Focus |
| --- | --- |
| `indicators/01_ema_cross.pine` | EMA 9/21 cross, background, alerts |
| `indicators/02_rsi_ob_os.pine` | RSI 14 and overbought/oversold levels |
| `indicators/03_macd_histogram.pine` | MACD 12/26/9 histogram |
| `indicators/04_bollinger_bands.pine` | Bollinger Bands and squeeze context |
| `indicators/05_supertrend.pine` | ATR-based trend display |
| `indicators/06_vwap_session.pine` | Session VWAP and deviation bands |
| `indicators/07_atr_levels.pine` | ATR-based reference levels |
| `indicators/08_pivot_points.pine` | Daily pivot levels |
| `indicators/09_volume_profile.pine` | Volume and OBV context |
| `indicators/10_stoch_rsi.pine` | Stochastic RSI K/D |
| `indicators/11_ichimoku.pine` | Ichimoku components |
| `indicators/12_mtf_ema.pine` | Multi-timeframe EMA context |

The remaining indicator files continue the same inventory through
`18_fakeout_filter.pine`; use `manifest.json` for the complete, hash-bound list.

## Strategies

The strategy files cover EMA, RSI, Supertrend, Bollinger, MACD, ATR, and
multi-timeframe patterns. Strategy settings are examples, not risk parameters
for a particular account, symbol, or market. Review commission, session,
slippage, position sizing, and recalculation behavior before any experiment.

## Try one example

1. Open a `.pine` file and confirm its first line is `//@version=6`.
2. Copy the exact file into TradingView Pine Editor.
3. Add it to a chart that matches the intended symbol and timeframe context.
4. Record compile, alert, repaint, and runtime observations separately.

Local repository checks remain `structural-only`; they are not a TradingView
compiler or chart test.
