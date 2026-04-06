# Renkler ve Gorsel — Pine Script v6
Maintainer: Ugur Pala — mail@ugurpala.com

## Temel Renkler
```pine
color.red, color.green, color.blue, color.orange
color.white, color.black, color.gray, color.yellow
color.lime, color.aqua, color.fuchsia, color.purple
```

## color.new — Saydamlik
```pine
color.new(color.red, 0)    // tam opak
color.new(color.red, 50)   // yuzde 50 saydam
color.new(color.red, 100)  // tamamen saydam (gorulmez)
```

## color.from_gradient — Renk Gecisi
```pine
//@version=6
indicator("Gradient RSI")
rsi = ta.rsi(close, 14)
bull = color.from_gradient(rsi, 50, 80, color.new(color.green, 70), color.green)
bear = color.from_gradient(rsi, 20, 50, color.red, color.new(color.red, 70))
rsiColor = rsi >= 50 ? bull : bear
plot(rsi, color=rsiColor)
```

## bgcolor — Grafik Arka Plani
```pine
bgcolor(condition ? color.new(color.green, 90) : na)
```
