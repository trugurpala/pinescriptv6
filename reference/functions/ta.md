# ta.* — Technical Analysis
> Maintainer: Ugur Pala · mail@ugurpala.com · github.com/trugurpala/pinescriptv6

---

## Hareketli Ortalamalar / Moving Averages
```pine
ta.sma(source, length)               // Basit / Simple
ta.ema(source, length)               // Üstel / Exponential
ta.wma(source, length)               // Ağırlıklı / Weighted
ta.rma(source, length)               // RSI MA (alpha = 1/length)
ta.vwma(source, length)              // Hacim ağırlıklı / Volume-weighted
ta.hma(source, length)               // Hull
ta.alma(source, length, offset, sigma) // Arnaud Legoux
ta.swma(source)                      // Symmetric weighted (4 bar)
```

## Osilatörler / Oscillators
```pine
ta.rsi(source, length)
[macd, signal, hist] = ta.macd(source, fastLength, slowLength, signalLength)
ta.cci(source, length)
ta.cmo(source, length)                // Chande Momentum
ta.mfi(source, length)                // Money Flow Index
ta.roc(source, length)                // Rate of Change
[k, d] = ta.stoch(high, low, close, length)
ta.tsi(source, shortLength, longLength)
```

## Volatilite / Volatility
```pine
ta.atr(length)
[upper, basis, lower] = ta.bb(source, length, mult)  // Bollinger Bands
ta.bbw(source, length, mult)          // BB Width
ta.tr(handle_na)                      // True Range
ta.kc(source, length, mult)           // Keltner Channel — returns [upper, basis, lower]
```

## Kesişimler / Crossovers
```pine
ta.crossover(source1, source2)        // source1 yukarı kesti / crossed up
ta.crossunder(source1, source2)       // source1 aşağı kesti / crossed down
ta.cross(source1, source2)            // her yönde / either direction
```

## Min / Max / Pivot
```pine
ta.highest(source, length)            // en yüksek / highest value
ta.lowest(source, length)             // en düşük / lowest value
ta.highestbars(source, length)        // kaç bar önce / bars since highest
ta.lowestbars(source, length)         // kaç bar önce / bars since lowest
ta.pivothigh(source, leftBars, rightBars)  // na döner yoksa / returns na if no pivot
ta.pivotlow(source, leftBars, rightBars)
```

## Yardımcılar / Helpers
```pine
ta.change(source)                     // 1 barlık değişim / 1-bar change
ta.change(source, length)             // n barlık değişim
ta.cum(source)                        // kümülatif toplam / cumulative sum
ta.falling(source, length)            // düşüşte mi? / falling?
ta.rising(source, length)             // yükseliyor mu? / rising?
ta.barssince(condition)               // son koşuldan beri kaç bar / bars since condition
ta.valuewhen(condition, source, occurrence) // n. koşul anındaki değer / value at nth condition
ta.range(source, length)              // max - min
```

## Örnek — BIST30 EMA Cross + RSI Filtresi
```pine
//@version=6
strategy("EMA Cross + RSI Filter — XU030", overlay=false)

ema9  = ta.ema(close, 9)
ema21 = ta.ema(close, 21)
rsi14 = ta.rsi(close, 14)
atr14 = ta.atr(14)

longCond  = ta.crossover(ema9, ema21) and rsi14 > 50
shortCond = ta.crossunder(ema9, ema21) and rsi14 < 50

if longCond
    strategy.entry("Long", strategy.long)
if shortCond
    strategy.entry("Short", strategy.short)

plot(rsi14, "RSI", color.blue)
hline(70, "OB", color.red)
hline(50, "Mid", color.gray)
hline(30, "OS", color.green)
```
