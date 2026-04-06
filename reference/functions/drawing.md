# Drawing - Pine Script v6
Maintainer: Ugur Pala - mail@ugurpala.com

## plot()
```pine
plot(close, "Kapanis", color.blue, linewidth=2)
plot(close, style=plot.style_histogram)
plot(na)  // gorulmez
```

## plotshape()
```pine
plotshape(buySignal, style=shape.triangleup,
          location=location.belowbar,
          color=color.green, size=size.small)
```

## hline()
```pine
hline(70, "OB", color.red, linestyle=hline.style_dashed)
hline(30, "OS", color.green)
```

## bgcolor()
```pine
bgcolor(condition ? color.new(color.green, 90) : na)
```

## line.new()
```pine
var line myLine = na
if barstate.islast
    line.delete(myLine)
    myLine := line.new(bar_index-10, ta.lowest(10),
                       bar_index, ta.highest(10),
                       color=color.orange, width=2)
```

## box.new()
```pine
var box myBox = na
box.delete(myBox[1])
myBox := box.new(bar_index-20, ta.highest(20),
                 bar_index, ta.lowest(20),
                 border_color=color.blue,
                 bgcolor=color.new(color.blue, 90))
```

## label.new()
```pine
label.new(bar_index, high,
          "PH: " + str.tostring(high, format.mintick),
          style=label.style_label_down,
          color=color.red, textcolor=color.white)
```

## fill()
```pine
p1 = plot(ta.ema(close, 9))
p2 = plot(ta.ema(close, 21))
fill(p1, p2, color=color.new(color.blue, 80))
```

## table.new()
```pine
var table t = table.new(position.top_right, 2, 3,
                         bgcolor=color.new(color.black, 70))
if barstate.islast
    table.cell(t, 0, 0, "RSI", text_color=color.white)
    table.cell(t, 1, 0, str.tostring(math.round(ta.rsi(close,14))),
               text_color=color.yellow)
```
