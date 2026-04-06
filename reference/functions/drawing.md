# Drawing Fonksiyonlari — Pine Script v6
Maintainer: Ugur Pala — mail@ugurpala.com

## plot()
```pine
plot(close, "Close", color.blue, 2)
plot(close, style=plot.style_histogram, color=color.green)
plot(na)  // gorulmez plot (placeholder)
```

## plotshape()
```pine
plotshape(buySignal, style=shape.triangleup,
          location=location.belowbar, color=color.green,
          size=size.small, title="Buy")
```

## hline()
```pine
hline(70, "OB", color.red, linestyle=hline.style_dashed)
hline(30, "OS", color.green)
```

## bgcolor()
```pine
bgcolor(isWeekend ? color.new(color.blue, 90) : na)
```

## line.new()
```pine
var line myLine = na
myLine := line.new(bar_index[1], close[1], bar_index, close,
                   color=color.blue, width=2)
// Sadece son cizgiyi tut
line.delete(myLine[1])
```

## box.new()
```pine
var box myBox = na
myBox := box.new(bar_index - 10, ta.highest(10), bar_index, ta.lowest(10),
                 border_color=color.red, bgcolor=color.new(color.red, 90))
box.delete(myBox[1])
```

## label.new()
```pine
label.new(bar_index, high, "High: " + str.tostring(high),
          style=label.style_label_down, color=color.green,
          textcolor=color.white)
```

## fill()
```pine
p1 = plot(ta.ema(close, 9))
p2 = plot(ta.ema(close, 21))
fill(p1, p2, color=color.new(color.blue, 80))
```
