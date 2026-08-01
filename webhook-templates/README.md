# Webhook Templates — Pine Script v6
> Maintainer: Ugur Pala · mail@ugurpala.com · github.com/trugurpala/pinescriptv6

TR: TradingView alert'lerini dış sistemlere iletmek için hazır webhook şablonları.
EN: Ready-to-use webhook templates for forwarding TradingView alerts to external systems.

---

## Dosyalar / Files

| Dosya | Açıklama / Description |
|-------|------------------------|
| `01_alert_message_templates.md` | TradingView alert mesaj şablonları |
| `02_pine_alert_conditions.pine` | `alertcondition()` ve `alert()` örnekleri |
| `03_telegram_webhook.md` | Telegram bot entegrasyonu |
| `04_discord_webhook.md` | Discord webhook entegrasyonu |
| `05_json_payload_templates.md` | JSON payload şablonları (broker API'leri için) |
| `06_viop_bist30_alerts.pine` | VİOP / BIST30 spesifik alert örnekleri |

---

## Nasıl Çalışır / How It Works

```
TradingView Alert
      │
      ▼
Webhook URL ──► Telegram Bot
             ├─► Discord Channel
             ├─► Custom Server (Python/Node.js)
             └─► Broker API
```

TR: TradingView Premium veya üzeri gereklidir.
EN: TradingView Premium or higher required for webhook alerts.
