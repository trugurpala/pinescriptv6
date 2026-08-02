# Alerts

Use `alertcondition()` when an indicator needs separately selectable conditions. In strategies, selectable alert events come from `alert()` calls and broker-emulator order fills, not from `alertcondition()` calls.

Configure `alert()` frequency in its `freq` argument. Configure `alertcondition()` frequency in the Create Alert UI, while accounting for the script's execution schedule. For strategy order-fill messages, set `alert_message` on the order-generating call and include `{{strategy.order.alert_message}}` in the UI message.

A running alert is a server-side snapshot of its creation context. Recreate it after relevant script, input, symbol, or timeframe changes. Bar-close frequency controls alert timing only; assess the data and logic separately for repaint mechanisms.

Local validation confirms catalog structure and source registration only. It does not inspect running alerts or prove TradingView runtime behavior.
