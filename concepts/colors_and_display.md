# Colors & Display
> Maintainer: Ugur Pala · mail@ugurpala.com · github.com/trugurpala/pinescriptv6

---

## TR | Türkçe

### Temel Renkler

```pine
color.red, color.green, color.blue, color.orange, color.yellow
color.white, color.black, color.gray, color.lime, color.aqua
color.fuchsia, color.navy, color.purple, color.teal, color.silver
```

### color.new() — Şeffaflık

```pine
color.new(color.red, 0)    // tam opak
color.new(color.red, 50)   // %50 şeffaf
color.new(color.red, 100)  // tamamen şeffaf (görünmez)
```

### color.from_gradient() — Geçiş Rengi

```pine
//@version=6
indicator("Gradient RSI")
rsi = ta.rsi(close, 14)
bull = color.from_gradient(rsi, 50, 80, color.new(color.green, 70), color.green)
bear = color.from_gradient(rsi, 20, 50, color.red, color.new(color.red, 70))
plot(rsi, color = rsi >= 50 ? bull : bear)
hline(70), hline(50), hline(30)
```

### bgcolor() — Arka Plan

```pine
// Oturum vurgusu
isSession = not na(time(timeframe.period, "0930-1730", "UTC+3"))
bgcolor(isSession ? color.new(color.blue, 92) : na)
```

---

## EN | English

### Built-in Colors

```pine
color.red, color.green, color.blue, color.orange, color.yellow
color.white, color.black, color.gray, color.lime, color.aqua
color.fuchsia, color.navy, color.purple, color.teal, color.silver
```

### color.new() — Transparency

```pine
color.new(color.red, 0)    // fully opaque
color.new(color.red, 50)   // 50% transparent
color.new(color.red, 100)  // invisible
```

### color.from_gradient() — Gradient

```pine
//@version=6
indicator("Gradient RSI")
rsi = ta.rsi(close, 14)
bull = color.from_gradient(rsi, 50, 80, color.new(color.green, 70), color.green)
bear = color.from_gradient(rsi, 20, 50, color.red, color.new(color.red, 70))
plot(rsi, color = rsi >= 50 ? bull : bear)
hline(70), hline(50), hline(30)
```

### bgcolor() — Background

```pine
// Session highlight
isSession = not na(time(timeframe.period, "0930-1730", "UTC+3"))
bgcolor(isSession ? color.new(color.blue, 92) : na)
```
