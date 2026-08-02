# TradingView publishing notes

This folder contains descriptions and a review order for three possible
TradingView publications. It is a preparation aid, not proof that any script
has been compiled, published, approved, or kept non-repainting.
The source files remain `structural-only` until a hash-bound manual record
exists.

## Publish order

| # | Script | Pine file | Description |
| --- | --- | --- | --- |
| 1 | Fakeout Filter | `../examples/indicators/18_fakeout_filter.pine` | `01_fakeout_filter_description.md` |
| 2 | VIOP Session Strategy | `../examples/strategies/11_viop_session_strategy.pine` | `02_viop_session_description.md` |
| 3 | Fakeout-Confirmed Strategy | `../examples/strategies/13_fakeout_confirmed_strategy.pine` | `03_fakeout_confirmed_strategy_description.md` |

## Review a script before publishing

1. Confirm the exact file and SHA-256 in [`../examples/manifest.json`](../examples/manifest.json).
2. Follow the [TradingView manual verification guide](../docs/tradingview-manual-verification.md).
3. Test the exact file in Pine Editor and on the intended chart context.
4. Record compile errors, alert behavior, repaint observations, and strategy
   results as separate observations.
5. Only publish when the account, script type, description, visibility, and
   TradingView rules are appropriate for you.

Do not turn a compile result into a profitability, security, or live-trading
claim. Do not put credentials, private code, or customer data in a description.
For contribution and reporting routes, see [`../SUPPORT.md`](../SUPPORT.md).

## Description checklist

Each description should state the Pine version, intended use, assumptions,
known limitations, and evidence level. Keep the repository URL as attribution;
do not imply endorsement by TradingView.
