# Objects & UDT
> Maintainer: Ugur Pala · mail@ugurpala.com · github.com/trugurpala/pinescriptv6

---

## TR | Türkçe

### User-Defined Type (UDT) Tanımla

```pine
//@version=6
indicator("UDT demo", overlay=true)

// @type Grafikteki bir pivot noktasını temsil eder.
// @field index (int)   Bar indexi
// @field price (float) Fiyat seviyesi
// @field isHigh (bool) Pivot yüksek mi?
type PivotPoint
    int   index
    float price
    bool  isHigh
```

### Instance Oluştur

```pine
var PivotPoint lastPivot = na

if not na(ta.pivothigh(high, 5, 5))
    lastPivot := PivotPoint.new(
        index  = bar_index[5],
        price  = high[5],
        isHigh = true
    )
    label.new(lastPivot.index, lastPivot.price, "PH",
              style=label.style_label_down, color=color.red)
```

### na Kontrolü

```pine
if not na(lastPivot)
    // lastPivot güvenle kullan
    plot(lastPivot.price, "Last Pivot", color.orange)
```

### Copy

```pine
p1 = PivotPoint.new(bar_index, high, true)
p2 = p1.copy()  // shallow copy
```

---

## EN | English

### Define a User-Defined Type (UDT)

```pine
//@version=6
indicator("UDT demo", overlay=true)

// @type Represents a pivot point on the chart.
// @field index (int)   Bar index
// @field price (float) Price level
// @field isHigh (bool) Is it a pivot high?
type PivotPoint
    int   index
    float price
    bool  isHigh
```

### Create an Instance

```pine
var PivotPoint lastPivot = na

if not na(ta.pivothigh(high, 5, 5))
    lastPivot := PivotPoint.new(
        index  = bar_index[5],
        price  = high[5],
        isHigh = true
    )
    label.new(lastPivot.index, lastPivot.price, "PH",
              style=label.style_label_down, color=color.red)
```

### na Check

```pine
if not na(lastPivot)
    // safely use lastPivot
    plot(lastPivot.price, "Last Pivot", color.orange)
```

### Copy

```pine
p1 = PivotPoint.new(bar_index, high, true)
p2 = p1.copy()  // shallow copy
```
