# Telegram Webhook Integration
> github.com/trugurpala/pinescriptv6

---

## TR | Türkçe

TradingView alertlerini Telegram'a iletmek için hazır şablon.

### Adım 1 — Telegram Bot Oluştur

1. Telegram'da `@BotFather` ile konuş
2. `/newbot` yaz → bot adı ve kullanıcı adı belirle
3. **Bot Token** al: `7123456789:AAF...`
4. Botla bir konuşma başlat
5. Chat ID al: `https://api.telegram.org/bot{TOKEN}/getUpdates`

---

### Adım 2 — Python Webhook Server

```python
# webhook_server.py
from flask import Flask, request
import requests

app = Flask(__name__)

BOT_TOKEN = "7123456789:AAF..."  # BotFather'dan aldığın token
CHAT_ID   = "123456789"          # Telegram chat ID

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    msg  = data.get("message", str(data))
    url  = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={"chat_id": CHAT_ID, "text": msg, "parse_mode": "Markdown"})
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

---

### Adım 3 — TradingView Alert Kurulumu

**Alert Message:**
```
📊 *{{ticker}}* | {{interval}}
🎯 Sinyal: EMA Cross
💰 Fiyat: {{close}}
🕐 {{timenow}}
```

**Webhook URL:**
```
http://SUNUCU_IP:5000/webhook
```

---

### Adım 4 — Pine Script'ten JSON Gönder

```pine
//@version=6
strategy("Telegram Strategy", overlay=true)
// ...strateji kodu...

// Alert mesajı TradingView → Alert → Message kutusuna:
// {"symbol":"{{ticker}}","action":"{{strategy.order.action}}","price":{{close}}}
```

---

## EN | English

### Step 1 — Create a Telegram Bot

1. Chat with `@BotFather` on Telegram
2. Type `/newbot` → set name and username
3. Get your **Bot Token**: `7123456789:AAF...`
4. Start a conversation with your bot
5. Get Chat ID: `https://api.telegram.org/bot{TOKEN}/getUpdates`

### Step 2 — Python Webhook Server

```python
from flask import Flask, request
import requests

app = Flask(__name__)
BOT_TOKEN = "YOUR_TOKEN"
CHAT_ID   = "YOUR_CHAT_ID"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    msg  = data.get("message", str(data))
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        json={"chat_id": CHAT_ID, "text": msg, "parse_mode": "Markdown"})
    return "ok", 200

app.run(host="0.0.0.0", port=5000)
```

### Step 3 — TradingView Alert Message

```
📊 *{{ticker}}* | {{interval}}
🎯 Signal: EMA Cross
💰 Price: {{close}}
🕐 {{timenow}}
```
