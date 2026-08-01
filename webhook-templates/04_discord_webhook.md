# Discord Webhook Integration
> github.com/trugurpala/pinescriptv6

---

## TR | Türkçe

TradingView alertlerini Discord kanalına iletmek için hazır şablon.

### Adım 1 — Discord Webhook URL Al

1. Discord sunucunda kanal seç
2. Kanal ayarları → **Integrations** → **Webhooks** → **New Webhook**
3. Webhook URL kopyala:
   `https://discord.com/api/webhooks/1234567890/abc...`

---

### Adım 2 — Direkt Discord'a Gönder (Python)

```python
# discord_webhook.py
from flask import Flask, request
import requests

app = Flask(__name__)
DISCORD_WEBHOOK = "https://discord.com/api/webhooks/YOUR_ID/YOUR_TOKEN"

@app.route("/webhook", methods=["POST"])
def webhook():
    data    = request.get_json()
    symbol  = data.get("symbol", "?")
    action  = data.get("action", "?")
    price   = data.get("price",  "?")

    payload = {
        "embeds": [{
            "title":       f"{symbol} — {action.upper()}",
            "color":       3066993 if action == "buy" else 15158332,
            "description": f"💰 Fiyat: **{price}**",
            "fields": [
                {"name": "Sembol",   "value": symbol, "inline": True},
                {"name": "İşlem",    "value": action, "inline": True},
                {"name": "Fiyat",    "value": str(price), "inline": True}
            ],
            "footer": {"text": "Pine Script v6 — trugurpala/pinescriptv6"}
        }]
    }
    requests.post(DISCORD_WEBHOOK, json=payload)
    return "ok", 200

app.run(host="0.0.0.0", port=5000)
```

---

### Adım 3 — TradingView Alert JSON Mesajı

```json
{
  "symbol":   "{{ticker}}",
  "action":   "{{strategy.order.action}}",
  "price":    {{close}},
  "interval": "{{interval}}",
  "time":     "{{timenow}}"
}
```

---

### Adım 4 — Webhook URL

TradingView Alert → **Webhook URL** kutusuna:
```
http://SUNUCU_IP:5000/webhook
```

---

## EN | English

### Step 1 — Get Discord Webhook URL

1. Pick a channel in your Discord server
2. Channel settings → **Integrations** → **Webhooks** → **New Webhook**
3. Copy the URL: `https://discord.com/api/webhooks/...`

### Step 2 — Python Handler

```python
from flask import Flask, request
import requests

app = Flask(__name__)
DISCORD_WEBHOOK = "https://discord.com/api/webhooks/YOUR_ID/YOUR_TOKEN"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    requests.post(DISCORD_WEBHOOK, json={
        "embeds": [{
            "title": f"{data.get('symbol')} — {data.get('action', '').upper()}",
            "color": 3066993,
            "description": f"Price: {data.get('price')}"
        }]
    })
    return "ok", 200
```

### Step 3 — TradingView Alert JSON

```json
{
  "symbol":   "{{ticker}}",
  "action":   "{{strategy.order.action}}",
  "price":    {{close}},
  "interval": "{{interval}}"
}
```
