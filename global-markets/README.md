# Global market examples

This folder contains 22 Pine Script v6 examples organized around common
futures, forex, crypto, index, and universal-symbol contexts. They demonstrate
how market context can affect sessions, symbols, and inputs; they are not
personalized trading systems.

## Evidence and limits

The files are inventoried in [`../examples/manifest.json`](../examples/manifest.json)
and remain `structural-only`. Check the exact hash before making a stronger
claim. A symbol name or market label does not prove that a feed, session,
contract, account plan, or data entitlement is available to you.

Use the [TradingView manual verification guide](../docs/tradingview-manual-verification.md)
for a human check. Review the [support guide](../SUPPORT.md) before sharing
code, screenshots, or error messages publicly.

## Instrument map

| File | Example context |
| --- | --- |
| `01_es_sp500.pine` | CME E-mini S&P 500 |
| `02_nq_nasdaq.pine` | CME E-mini Nasdaq-100 |
| `03_gc_gold.pine` | COMEX gold / XAUUSD context |
| `04_cl_crude_oil.pine` | NYMEX crude oil |
| `05_eurusd_forex.pine` | EUR/USD |
| `06_gbpusd_forex.pine` | GBP/USD |
| `07_usdjpy_forex.pine` | USD/JPY |
| `08_btc_crypto.pine` | BTC/USDT |
| `09_eth_crypto.pine` | ETH/USDT |
| `10_dax_germany.pine` | DAX context |
| `11_nikkei_japan.pine` | Nikkei 225 context |
| `12_universal_strategy.pine` | Current chart symbol |

Additional files cover trend, pullback, opening-range, VWAP, and structure
patterns. The manifest is the source of truth for the complete list and hashes.

## Before using an example

Confirm the chart symbol, exchange feed, session timezone, contract
specification, commission, slippage, and timeframe assumptions. Keep local
checks, Pine Editor compilation, chart behavior, and live-trading suitability
as separate claims.
