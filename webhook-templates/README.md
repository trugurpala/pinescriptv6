# Webhook templates for Pine Script v6

These files show how TradingView alert messages can be shaped for an external
receiver. They are educational templates, not a broker integration or a safe
live-ordering system.

## Evidence and limits

The Pine files are tracked as `structural-only`. Test the exact file and payload
in your own TradingView account and receiver before relying on it. Account
plans, alert limits, symbols, exchange data, and webhook availability vary.
See the [TradingView manual verification guide](../docs/tradingview-manual-verification.md)
and the [support guide](../SUPPORT.md).

## Files

| File | Purpose |
| --- | --- |
| `01_alert_message_templates.md` | Alert message patterns |
| `02_pine_alert_conditions.pine` | `alertcondition()` and `alert()` examples |
| `03_telegram_webhook.md` | Telegram delivery notes |
| `04_discord_webhook.md` | Discord delivery notes |
| `05_json_payload_templates.md` | JSON payload examples |
| `06_viop_bist30_alerts.pine` | VIOP/BIST30 alert context |

## Delivery path

```text
TradingView alert -> webhook endpoint -> validation -> application/logging
```

Before any real integration, use HTTPS, authenticate requests, validate the
symbol/side/size/timestamp/nonce, prevent replay, rate-limit, log safely, and
provide a kill switch. Keep tokens outside Pine source and Git history. The
templates use placeholders and do not authorize live orders.
