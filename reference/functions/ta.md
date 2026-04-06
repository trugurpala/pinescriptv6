# ta.* - Pine Script v6
Maintainer: Ugur Pala - mail@ugurpala.com

## Hareketli Ortalamalar
```pine
ta.sma(source, length)   // Basit
ta.ema(source, length)   // Ustel
ta.wma(source, length)   // Agirlikli
ta.rma(source, length)   // RSI MA
ta.vwma(source, length)  // Hacim agirlikli
ta.hma(source, length)   // Hull
ta.alma(source, length, offset, sigma)
```

## Osilatorler
```pine
ta.rsi(source, length)
[macd, signal, hist] = ta.macd(src, fast, slow, sig)
ta.cci(source, length)
ta.mfi(source, length)
ta.roc(source, length)
[k, d] = ta.stoch(high, low, close, length)
```

## Volatilite
```pine
ta.atr(length)
[upper, basis, lower] = ta.bb(src, len, mult)
ta.bbw(source, length, mult)
ta.tr(handle_na)
```

## Kesisimler
```pine
ta.crossover(source1, source2)   // Yukari kesti
ta.crossunder(source1, source2)  // Asagi kesti
ta.cross(source1, source2)       // Herhangi yone
```

## Min/Max/Pivot
```pine
ta.highest(source, length)
ta.lowest(source, length)
ta.highestbars(source, length)
ta.lowestbars(source, length)
ta.pivothigh(left, right)  // na dondurur yoksa
ta.pivotlow(left, right)
```

## Yardimci
```pine
ta.change(source)               // 1 barlik degisim
ta.change(source, length)       // length barlik degisim
ta.cum(source)                  // Kumulatif toplam
ta.falling(source, length)      // Dususte mi?
ta.rising(source, length)       // Yukseliyor mu?
ta.barssince(condition)         // Son kosuldan beri kac bar
ta.valuewhen(cond, src, n)      // n. kosul anindaki deger
ta.range(source, length)        // max - min
```

## Ornek - RSI + EMA Stratejisi
```pine
//@version=6
strategy("RSI+EMA", overlay=false)
rsi = ta.rsi(close, 14)
ema200 = ta.ema(close, 200)
longCond = ta.crossover(rsi, 30) and close > ema200
if longCond
    strategy.entry("Long", strategy.long)
plot(rsi, "RSI", color.blue)
hline(70), hline(30)
```
