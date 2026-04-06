# Methods & User-Defined Types — New in v6
> v5 to v6 — github.com/trugurpala/pinescriptv6

---

## TR | Türkçe

v5'te UDT (User-Defined Type) ve user-defined method yoktu. v6'da eklendi.

### User-Defined Type (UDT)

```pine
//@version=6
indicator("UDT demo", overlay=true)

// Tip tanımla
type PivotPoint
    int   index
    float price
    bool  isHigh

// Instance oluştur
var PivotPoint lastPivot = na

if not na(ta.pivothigh(high, 5, 5))
    lastPivot := PivotPoint.new(
        index  = bar_index[5],
        price  = high[5],
        isHigh = true)
    label.new(lastPivot.index, lastPivot.price, "PH",
        style=label.style_label_down, color=color.red)
```

### User-Defined Methods

```pine
//@version=6
indicator("Method demo")

// Array üzerine method tanımla
method addAndTrim(array<float> arr, float val, int maxSize) =>
    arr.push(val)
    if arr.size() > maxSize
        arr.shift()
    arr

var queue = array.new<float>(0)
queue.addAndTrim(close, 20)  // method syntax ile çağır
plot(queue.avg(), "Rolling Avg")
```

### v5 ile karşılaştırma

```pine
// v5 — UDT yok, her şey ayrı değişken
//@version=5
var int   pivotIdx   = na
var float pivotPrice = na
var bool  pivotIsHigh = na

// v6 — UDT ile temiz
//@version=6
type PivotPoint
    int   index
    float price
    bool  isHigh
var PivotPoint pivot = na
```

---

## EN | English

UDT and user-defined methods are new in v6.

```pine
//@version=6
// Define a type
type Trade
    float entry
    float stop
    float target

// Create and use
var Trade myTrade = na
if longSignal
    myTrade := Trade.new(
        entry  = close,
        stop   = close - 2 * ta.atr(14),
        target = close + 3 * ta.atr(14))
```
