# Drawing Objects — line / label / box
> v5 to v6 — github.com/trugurpala/pinescriptv6

---

## TR | Türkçe

Drawing API v6'da büyük ölçüde aynı kaldı — sadece `chart.point` eklendi.

### line.new() — değişen yok

```pine
//@version=6
var line myLine = na
if barstate.islast
    line.delete(myLine)
    myLine := line.new(bar_index - 10, ta.lowest(10),
                       bar_index,      ta.highest(10),
                       color=color.orange, width=2)
```

### label.new() — değişen yok

```pine
//@version=6
if ta.pivothigh(high, 5, 5)
    label.new(bar_index[5], high[5],
        str.tostring(high[5], format.mintick),
        style=label.style_label_down,
        color=color.red, textcolor=color.white)
```

### Yeni v6: chart.point

```pine
//@version=6
indicator("chart.point demo", overlay=true)
// chart.point koordinat sistemi — line.new için de kullanılabilir
cp = chart.point.now(high)
line.new(chart.point.from_index(bar_index - 5, low[5]), cp)
```

### Limit artırma — v5 ile aynı

```pine
//@version=6
indicator("Demo",
    max_lines_count  = 500,
    max_labels_count = 500,
    max_boxes_count  = 500)
```

---

## EN | English

Drawing API is mostly unchanged. The main addition in v6 is `chart.point`.

```pine
//@version=6
// New: chart.point coordinate system
cp = chart.point.now(high)
line.new(chart.point.from_index(bar_index - 5, low[5]), cp)
```
