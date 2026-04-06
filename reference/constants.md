# Constants — Pine Script v6
Maintainer: Ugur Pala — mail@ugurpala.com

## color.*
color.red, color.green, color.blue, color.orange, color.yellow
color.white, color.black, color.gray, color.lime, color.aqua
color.fuchsia, color.navy, color.olive, color.maroon, color.purple
color.teal, color.silver

## shape.* (plotshape icin)
shape.circle, shape.cross, shape.diamond, shape.flag, shape.square
shape.triangledown, shape.triangleup, shape.arrowdown, shape.arrowup
shape.xcross, shape.labeldown, shape.labelup

## plot.style_*
plot.style_line, plot.style_linebr, plot.style_stepline
plot.style_area, plot.style_areabr, plot.style_columns
plot.style_histogram, plot.style_circles, plot.style_cross

## size.*
size.tiny, size.small, size.normal, size.large, size.huge, size.auto

## location.*
location.abovebar, location.belowbar, location.top, location.bottom
location.absolute

## alert.freq_*
alert.freq_once_per_bar, alert.freq_once_per_bar_close
alert.freq_all

## extend.*
extend.none, extend.right, extend.left, extend.both

## line.style_*
line.style_solid, line.style_dashed, line.style_dotted, line.style_arrow_right

## Ornek
```pine
plotshape(condition, style=shape.triangleup, location=location.belowbar, 
          color=color.green, size=size.small)
```
