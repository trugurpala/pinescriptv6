# Timeframes & Multi-Timeframe (MTF)
> Maintainer: Ugur Pala · mail@ugurpala.com · github.com/trugurpala/pinescriptv6

---

## TR | Türkçe

### request.security() Temeli

```pine
//@version=6
indicator("MTF Demo", overlay=true)
dailyClose = request.security(syminfo.tickerid, "D", close)
weeklyEma  = request.security(syminfo.tickerid, "W", ta.ema(close, 20))
plot(dailyClose)
plot(weeklyEma)
```

### Repainting Önleme

```pine
// ❌ Canlı bar verisi — repainting yapabilir
htf = request.security(syminfo.tickerid, "D", close)

// ✅ Kapanmış bar — güvenli
htf_safe = request.security(syminfo.tickerid, "D", close[1])
```

### Çoklu Değer — Tuple

```pine
[htfOpen, htfHigh, htfLow, htfClose] =
    request.security(syminfo.tickerid, "D", [open, high, low, close])
```

### Timeframe Stringleri

| String | Anlamı |
|--------|--------|
| `"1"` | 1 dakika |
| `"5"` | 5 dakika |
| `"15"` | 15 dakika |
| `"60"` | 1 saat |
| `"240"` | 4 saat |
| `"D"` | Günlük |
| `"W"` | Haftalık |
| `"M"` | Aylık |

### Grafik Timeframe'ini Kontrol Et

```pine
isDaily = timeframe.in_seconds() >= timeframe.in_seconds("D")
bgcolor(isDaily ? color.new(color.blue, 90) : na)
```

---

## EN | English

### request.security() Basics

```pine
//@version=6
indicator("MTF Demo", overlay=true)
dailyClose = request.security(syminfo.tickerid, "D", close)
weeklyEma  = request.security(syminfo.tickerid, "W", ta.ema(close, 20))
plot(dailyClose)
plot(weeklyEma)
```

### Prevent Repainting

```pine
// ❌ Live bar data — may repaint
htf = request.security(syminfo.tickerid, "D", close)

// ✅ Confirmed bar — safe
htf_safe = request.security(syminfo.tickerid, "D", close[1])
```

### Multiple Values — Tuple

```pine
[htfOpen, htfHigh, htfLow, htfClose] =
    request.security(syminfo.tickerid, "D", [open, high, low, close])
```

### Timeframe Strings

| String | Meaning |
|--------|---------|
| `"1"` | 1 minute |
| `"5"` | 5 minutes |
| `"15"` | 15 minutes |
| `"60"` | 1 hour |
| `"240"` | 4 hours |
| `"D"` | Daily |
| `"W"` | Weekly |
| `"M"` | Monthly |
