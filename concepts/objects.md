# Objects ve UDT — Pine Script v6
Maintainer: Ugur Pala — mail@ugurpala.com

## User-Defined Type (UDT) Tanimla

```pine
//@version=6
indicator("UDT demo")

type PivotPoint
    int   index
    float price
    bool  isHigh

// Instance olustur
var PivotPoint lastPivot = na

if ta.pivothigh(high, 5, 5)
    lastPivot := PivotPoint.new(bar_index, high, true)
    label.new(lastPivot.index, lastPivot.price, "PH")
```

## Copy — Shallow vs Deep
```pine
p1 = PivotPoint.new(bar_index, high, true)
p2 = p1.copy()  // shallow copy — ozel type field'lari ayni referans!
```

## na Kontrolu
```pine
if not na(lastPivot)
    // lastPivot kullan
```
