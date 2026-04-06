# Annotations
> Maintainer: Ugur Pala · mail@ugurpala.com · github.com/trugurpala/pinescriptv6
> TR: Kod belgelemeleri ve metadata için kullanılan annotation'lar. EN: Annotations for documentation and metadata.

---

## @version
```pine
//@version=6
```

## @description — Library açıklaması
```pine
// @description RSI + EMA kombinasyonu için yardımcı fonksiyonlar.
// @description Helper functions for RSI + EMA combinations.
library("MyLibrary")
```

## @function
```pine
// @function Verilen uzunlukta EMA hesaplar.
// @function Calculates EMA for the given length.
// @param src  (series float) Kaynak seri / Source series
// @param len  (simple int)  Periyod / Period
// @returns    (series float) EMA değeri / EMA value
export myEma(series float src, simple int len) =>
    ta.ema(src, len)
```

## @param
```pine
// @param length (simple int) RSI periyodu. Min: 1, Max: 500
```

## @returns
```pine
// @returns (series bool) Kesişim olduğunda true döner.
// @returns (series bool) Returns true when crossover occurs.
```

## @type ve @field
```pine
// @type Grafik üzerindeki bir pivot noktasını temsil eder.
// @type Represents a pivot point on the chart.
// @field index (int)   Bar indexi / Bar index
// @field price (float) Fiyat seviyesi / Price level
type PivotPoint
    int   index
    float price
```

## @strategy_alert_message
```pine
//@strategy_alert_message {{strategy.order.action}} @ {{close}}
```
