# ta.* Fonksiyonlari — Pine Script v6
Maintainer: Ugur Pala — mail@ugurpala.com

## Hareketli Ortalamalar
```pine
ta.sma(source, length)      // Basit
ta.ema(source, length)      // Ustel
ta.wma(source, length)      // Agirlikli
ta.rma(source, length)      // RSI'da kullanilan (alpha=1/length)
ta.vwma(source, length)     // Hacim agirlikli
ta.hma(source, length)      // Hull
ta.swma(source)             // Symmetric weighted (4 bar)
ta.alma(source, length, offset, sigma)  // Arnaud Legoux
```

## Osilatörler
```pine
ta.rsi(source, length)                    // RSI
[macd, signal, hist] = ta.macd(source, fast, slow, signal)
ta.cci(source, length)                    // CCI
ta.cmo(source, length)                    // Chande Momentum
ta.mfi(source, length)                    // Money Flow Index
ta.roc(source, length)                    // Rate of Change
ta.stoch(source, high, low, length)       // Stochastic
[k, d] = ta.stoch(high, low, close, length)
```

## Volatilite
```pine
ta.atr(length)                            // ATR
[upper, lower] = ta.bb(source, length, mult)   // Bollinger Bands
ta.bbw(source, length, mult)              // Bollinger Band Width
ta.tr(handle_na)                          // True Range
```

## Kesisimler
```pine
ta.crossover(source1, source2)   // source1 yukari kesti
ta.crossunder(source1, source2)  // source1 asagi kesti
ta.cross(source1, source2)       // herhangi yonde kesisti
```

## Min / Max / Pivot
```pine
ta.highest(source, length)       // En yuksek
ta.lowest(source, length)        // En dusuk
ta.highestbars(source, length)   // En yuksek kac bar once
ta.lowestbars(source, length)    // En dusuk kac bar once
ta.pivothigh(left, right)        // Pivot yukseği
ta.pivotlow(left, right)         // Pivot dusugu
```

## Diger
```pine
ta.change(source, length)        // Degisim
ta.change(source)                // 1 bar degisim
ta.cum(source)                   // Kumulatif toplam
ta.falling(source, length)       // Dususte mi?
ta.rising(source, length)        // Yukseliyor mu?
ta.valuewhen(cond, source, occurrence)  // Kosul saglandiginda deger
ta.barssince(condition)          // Son kosuldan beri kac bar
ta.range(source, length)         // max-min farki
```

## Ornek: RSI + EMA Stratejisi
```pine
//@version=6
strategy("RSI + EMA", overlay=false)
rsi = ta.rsi(close, 14)
ema = ta.ema(close, 200)

longCond  = ta.crossover(rsi, 30) and close > ema
shortCond = ta.crossunder(rsi, 70) and close < ema

if longCond
    strategy.entry("Long", strategy.long)
if shortCond
    strategy.entry("Short", strategy.short)

plot(rsi, "RSI", color.blue)
hline(70), hline(30)
```
