# Confirmed higher-timeframe requests

When a script intentionally needs confirmed values from a timeframe higher than
the chart, the documented non-repainting pattern offsets the requested expression
and uses `barmerge.lookahead_on`. The offset refers to the previous confirmed HTF
bar, while lookahead aligns that confirmed value across historical chart bars.

This is scoped guidance, not a universal rewrite. Lower-timeframe requests,
equal-timeframe requests, intentional developing values, tuple requests, and
other data functions require their own reasoning. An agent should first establish
the requested timeframe relationship and desired realtime behavior.
