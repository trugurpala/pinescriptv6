# Constants
> Maintainer: Ugur Pala · mail@ugurpala.com · github.com/trugurpala/pinescriptv6
> TR: Fonksiyon argümanlarında kullanılan sabit değerler. EN: Fixed constants used as function arguments.

---

## color.*
```pine
color.red     color.green   color.blue    color.orange  color.yellow
color.white   color.black   color.gray    color.lime    color.aqua
color.fuchsia color.navy    color.olive   color.maroon  color.purple
color.teal    color.silver
```

## shape.* — plotshape için / for plotshape
```pine
shape.circle       shape.cross       shape.diamond     shape.flag
shape.square       shape.triangleup  shape.triangledown
shape.arrowup      shape.arrowdown   shape.xcross
shape.labelup      shape.labeldown
```

## plot.style_*
```pine
plot.style_line      plot.style_linebr    plot.style_stepline
plot.style_area      plot.style_areabr    plot.style_columns
plot.style_histogram plot.style_circles   plot.style_cross
```

## size.*
```pine
size.tiny   size.small   size.normal   size.large   size.huge   size.auto
```

## location.*
```pine
location.abovebar   location.belowbar   location.top
location.bottom     location.absolute
```

## line.style_*
```pine
line.style_solid   line.style_dashed   line.style_dotted   line.style_arrow_right
```

## hline.style_*
```pine
hline.style_solid   hline.style_dashed   hline.style_dotted
```

## label.style_*
```pine
label.style_label_down   label.style_label_up     label.style_label_left
label.style_label_right  label.style_label_center label.style_none
label.style_text_outline label.style_circle       label.style_square
label.style_diamond      label.style_flag         label.style_cross
```

## alert.freq_*
```pine
alert.freq_once_per_bar         // bar başına bir kez
alert.freq_once_per_bar_close   // sadece kapanışta
alert.freq_all                  // her tickte
```

## extend.*
```pine
extend.none   extend.right   extend.left   extend.both
```

## position.*
```pine
position.top_left    position.top_center    position.top_right
position.middle_left position.middle_center position.middle_right
position.bottom_left position.bottom_center position.bottom_right
```

## Örnek / Example
```pine
plotshape(buySignal,
    style    = shape.triangleup,
    location = location.belowbar,
    color    = color.green,
    size     = size.small,
    title    = "Buy")
```
