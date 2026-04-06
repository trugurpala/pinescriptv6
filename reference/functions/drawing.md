# Drawing
> Maintainer: Ugur Pala · mail@ugurpala.com · github.com/trugurpala/pinescriptv6

---

## plot()
```pine
plot(close, "Kapanış", color.blue, linewidth=2)
plot(close, style=plot.style_histogram)
plot(na)    // görünmez placeholder
```

## plotshape()
```pine
plotshape(buySignal,
    style    = shape.triangleup,
    location = location.belowbar,
    color    = color.green,
    size     = size.small,
    title    = "Al")

plotshape(sellSignal,
    style    = shape.triangledown,
    location = location.abovebar,
    color    = color.red,
    size     = size.small,
    title    = "Sat")
```

## hline()
```pine
hline(70, "Aşırı Alım", color.red,   linestyle=hline.style_dashed)
hline(30, "Aşırı Satım", color.green, linestyle=hline.style_dashed)
hline(50, "Orta",        color.gray,  linestyle=hline.style_dotted)
```

## bgcolor()
```pine
bgcolor(isSession ? color.new(color.blue, 92) : na)
bgcolor(close > open ? color.new(color.green, 95) : color.new(color.red, 95))
```

## line.new()
```pine
// Sadece son çizgiyi tut / Keep only the last line
var line myLine = na
if barstate.islast
    line.delete(myLine)
    myLine := line.new(
        bar_index - 10, ta.lowest(10),
        bar_index,      ta.highest(10),
        color = color.orange, width = 2,
        style = line.style_dashed)
```

## box.new()
```pine
var box myBox = na
box.delete(myBox[1])
myBox := box.new(
    bar_index - 20, ta.highest(20),
    bar_index,      ta.lowest(20),
    border_color = color.blue,
    bgcolor      = color.new(color.blue, 90))
```

## label.new()
```pine
if ta.pivothigh(high, 5, 5)
    label.new(bar_index[5], high[5],
        "PH: " + str.tostring(high[5], format.mintick),
        style     = label.style_label_down,
        color     = color.red,
        textcolor = color.white)
```

## fill()
```pine
p1 = plot(ta.ema(close, 9),  color=color.green)
p2 = plot(ta.ema(close, 21), color=color.red)
fill(p1, p2, color=color.new(color.blue, 85))
```

## table.new()
```pine
var table infoTable = table.new(
    position.top_right, 2, 3,
    bgcolor      = color.new(color.black, 70),
    border_width = 1)

if barstate.islast
    table.cell(infoTable, 0, 0, "RSI", text_color=color.gray)
    table.cell(infoTable, 1, 0,
        str.tostring(math.round(ta.rsi(close, 14), 1)),
        text_color = color.yellow)
    table.cell(infoTable, 0, 1, "ATR", text_color=color.gray)
    table.cell(infoTable, 1, 1,
        str.tostring(math.round(ta.atr(14), 2)),
        text_color = color.yellow)
```
