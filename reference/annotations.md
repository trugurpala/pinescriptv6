# Annotations — Pine Script v6
Maintainer: Ugur Pala — mail@ugurpala.com

## @version
```pine
//@version=6
```

## @description
```pine
// @description Bu indikatör RSI ve EMA'yi birlestirir.
library("MyLibrary")
```

## @function
```pine
// @function Verilen uzunlukta EMA hesaplar.
// @param src (series float) Kaynak seri
// @param len (simple int) Period uzunlugu
// @returns (series float) EMA degeri
export myEma(float src, int len) =>
    ta.ema(src, len)
```

## @param
```pine
// @param length (simple int) Indicator period. Min: 1
```

## @returns
```pine
// @returns (series bool) Kesisim oldugunda true
```

## @type ve @field
```pine
// @type Grafik uzerinde bir noktayi temsil eder.
// @field index (int) Bar indexi (x koordinati)
// @field price (float) Fiyat (y koordinati)
type ChartPoint
    int   index
    float price
```

## @strategy_alert_message
```pine
//@strategy_alert_message {{strategy.order.action}} @ {{close}}
```
