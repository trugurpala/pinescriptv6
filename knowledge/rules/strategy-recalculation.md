# Strategy recalculation

Strategy recalculation settings change semantics rather than code style.
`calc_on_every_tick` exposes realtime updates that historical bars cannot fully
reconstruct, so results can change after reload. It can still be the intended
choice for a strategy that documents this limitation.

The July 2026 `calc_on_every_history_tick` setting is separate. It enables
documented historical recalculation behavior using the data available to the
strategy. Neither setting substitutes for market/timeframe testing, and neither
supports a blanket “safe” or “unsafe” claim.
