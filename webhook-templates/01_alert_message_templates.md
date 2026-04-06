# Alert Message Templates
> github.com/trugurpala/pinescriptv6

---

## TR | Türkçe

TradingView alert mesajlarında kullanılabilecek dinamik değişkenler ve hazır şablonlar.

### TradingView Dinamik Değişkenler

| Değişken | Açıklama |
|----------|----------|
| `{{ticker}}` | Sembol adı (ör. XU030) |
| `{{exchange}}` | Borsa (ör. BIST) |
| `{{close}}` | Kapanış fiyatı |
| `{{open}}` | Açılış fiyatı |
| `{{high}}` | Yüksek |
| `{{low}}` | Düşük |
| `{{volume}}` | Hacim |
| `{{time}}` | Bar zamanı |
| `{{timenow}}` | Şu anki zaman |
| `{{interval}}` | Grafik zaman dilimi |
| `{{strategy.order.action}}` | `buy` veya `sell` |
| `{{strategy.order.price}}` | Emir fiyatı |
| `{{strategy.order.contracts}}` | Lot sayısı |
| `{{strategy.position_size}}` | Pozisyon büyüklüğü |

---

### Hazır Şablonlar

**Basit fiyat alarmı:**
```
{{ticker}} | {{interval}} | Fiyat: {{close}} | {{timenow}}
```

**EMA Cross sinyali:**
```
🚨 EMA CROSS | {{ticker}}
Yön: {{strategy.order.action}}
Fiyat: {{close}}
Zaman: {{timenow}}
```

**VİOP / BIST30 stratejisi:**
```json
{
  "symbol":   "{{ticker}}",
  "action":   "{{strategy.order.action}}",
  "price":    {{close}},
  "qty":      {{strategy.order.contracts}},
  "interval": "{{interval}}",
  "time":     "{{timenow}}"
}
```

**Telegram için:**
```
📊 *{{ticker}}* | {{interval}}
🎯 Sinyal: {{strategy.order.action}}
💰 Fiyat: {{close}}
📦 Lot: {{strategy.order.contracts}}
🕐 {{timenow}}
```

**Discord Embed için:**
```json
{
  "embeds": [{
    "title": "{{ticker}} — {{strategy.order.action}}",
    "color": 3066993,
    "fields": [
      {"name": "Fiyat", "value": "{{close}}", "inline": true},
      {"name": "Zaman", "value": "{{timenow}}", "inline": true}
    ]
  }]
}
```

---

## EN | English

### Dynamic Variables

Same variables work in English — see table above.

### Ready Templates

**Simple price alert:**
```
{{ticker}} | {{interval}} | Price: {{close}} | {{timenow}}
```

**Strategy signal:**
```json
{
  "symbol":   "{{ticker}}",
  "action":   "{{strategy.order.action}}",
  "price":    {{close}},
  "qty":      {{strategy.order.contracts}},
  "interval": "{{interval}}",
  "time":     "{{timenow}}"
}
```

**Telegram format:**
```
📊 *{{ticker}}* | {{interval}}
🎯 Signal: {{strategy.order.action}}
💰 Price: {{close}}
📦 Qty: {{strategy.order.contracts}}
🕐 {{timenow}}
```
