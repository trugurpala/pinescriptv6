# JSON Payload Templates
> github.com/trugurpala/pinescriptv6

---

## TR | Türkçe

Farklı broker API'leri ve sistemler için hazır JSON payload şablonları.
TradingView Alert → Message kutusuna yapıştır.

---

### Basit Buy/Sell

```json
{
  "action":   "{{strategy.order.action}}",
  "symbol":   "{{ticker}}",
  "price":    {{close}},
  "time":     "{{timenow}}"
}
```

---

### Strateji Detaylı

```json
{
  "symbol":        "{{ticker}}",
  "exchange":      "{{exchange}}",
  "interval":      "{{interval}}",
  "action":        "{{strategy.order.action}}",
  "price":         {{close}},
  "qty":           {{strategy.order.contracts}},
  "position_size": {{strategy.position_size}},
  "order_price":   {{strategy.order.price}},
  "time":          "{{timenow}}"
}
```

---

### VİOP / BIST30 Spesifik

```json
{
  "market":    "VIOP",
  "symbol":    "F_XU030",
  "action":    "{{strategy.order.action}}",
  "price":     {{close}},
  "lot":       {{strategy.order.contracts}},
  "interval":  "{{interval}}",
  "signal_id": "{{ticker}}_{{timenow}}"
}
```

---

### Risk Yönetimi Dahil

```json
{
  "symbol":     "{{ticker}}",
  "action":     "{{strategy.order.action}}",
  "price":      {{close}},
  "sl_price":   {{strategy.order.price}},
  "position":   {{strategy.position_size}},
  "equity":     {{strategy.equity}},
  "interval":   "{{interval}}",
  "time":       "{{timenow}}"
}
```

---

### Çoklu Sinyal (indikatör için)

```json
{
  "symbol":    "{{ticker}}",
  "signal":    "ema_cross_bull",
  "price":     {{close}},
  "interval":  "{{interval}}",
  "time":      "{{timenow}}"
}
```

---

## EN | English

### Simple Buy/Sell

```json
{
  "action":  "{{strategy.order.action}}",
  "symbol":  "{{ticker}}",
  "price":   {{close}},
  "time":    "{{timenow}}"
}
```

### Full Strategy Payload

```json
{
  "symbol":        "{{ticker}}",
  "exchange":      "{{exchange}}",
  "interval":      "{{interval}}",
  "action":        "{{strategy.order.action}}",
  "price":         {{close}},
  "qty":           {{strategy.order.contracts}},
  "position_size": {{strategy.position_size}},
  "time":          "{{timenow}}"
}
```
