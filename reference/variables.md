# Variables
> Maintainer: Ugur Pala · mail@ugurpala.com · github.com/trugurpala/pinescriptv6
> TR: Yerleşik değişkenler. EN: Built-in read-only variables.

---

## Fiyat / Price
```pine
open, high, low, close    // OHLC
volume                    // hacim / volume
vwap                      // gün içi VWAP
hl2                       // (high + low) / 2
hlc3                      // (high + low + close) / 3
ohlc4                     // (open + high + low + close) / 4
hlcc4                     // (high + low + close + close) / 4
```

## Bar & Zaman / Bar & Time
```pine
bar_index    // 0'dan başlar, her yeni barda 1 artar
time         // Unix ms — açılış zamanı
time_close   // Unix ms — kapanış zamanı
timenow      // Unix ms — şu an
```

## Sembol / Symbol
```pine
syminfo.ticker          // "XU030"
syminfo.tickerid        // "BIST:XU030"
syminfo.exchange        // "BIST"
syminfo.description     // tam açıklama
syminfo.type            // "futures", "stock" vb.
syminfo.currency        // "TRY", "USD"
syminfo.mintick         // minimum fiyat adımı
syminfo.pointvalue      // nokta değeri
```

## Timeframe
```pine
timeframe.period        // "1", "D", "W" — mevcut grafik
timeframe.multiplier    // sayısal çarpan
timeframe.isminutes     // true ise dakika bazlı
timeframe.ishours       // true ise saatlik
timeframe.isdaily       // true ise günlük
timeframe.isweekly      // true ise haftalık
timeframe.ismonthly     // true ise aylık
timeframe.in_seconds()  // saniye cinsinden
```

## Strateji / Strategy
```pine
strategy.equity              // toplam sermaye
strategy.position_size       // + long, - short, 0 yok
strategy.position_avg_price  // ortalama giriş fiyatı
strategy.netprofit           // net kâr
strategy.grossprofit         // brüt kâr
strategy.grossloss           // brüt zarar
strategy.opentrades          // açık işlem sayısı
strategy.closedtrades        // kapanmış işlem sayısı
strategy.wintrades           // kazanan işlem
strategy.losstrades          // kaybeden işlem
```

## Örnek / Example
```pine
//@version=6
indicator("Variables demo", overlay=true)
label.new(bar_index, high,
    syminfo.ticker + " | " + str.tostring(close, format.mintick),
    style=label.style_label_down)
```
