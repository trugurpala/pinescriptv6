# Debugging - Pine Script v6
Maintainer: Ugur Pala - mail@ugurpala.com

## Pine Logs (Tavsiye Edilen)
TradingView > Script > Pine Editor > Pine Logs paneli

```pine
//@version=6
indicator("Debug Demo")

// Sadece son barda log yaz
if barstate.islast
    log.info("Close: {0}", close)
    log.info("RSI: {0}", ta.rsi(close, 14))

// Her barda
if ta.crossover(ta.ema(close,9), ta.ema(close,21))
    log.warning("EMA kesisimi - Bar {0}", bar_index)
```

## plot() ile Gorsel Debug
```pine
// Deger veri penceresinde gorunsun
plot(myVar, "Debug", display=display.data_window)

// Kosul true/false -> 1/0 olarak izle
plot(myCondition ? 1 : 0, "Kosul")
```

## label ile Anlık Degerleri Goster
```pine
if barstate.islast
    label.new(bar_index, high,
              "RSI: " + str.tostring(math.round(ta.rsi(close,14))) +
              " ATR: " + str.tostring(math.round(ta.atr(14), 2)),
              style=label.style_label_down, color=color.navy,
              textcolor=color.white)
```

## table ile Debug Paneli
```pine
var table dbg = table.new(position.top_left, 2, 4,
                           bgcolor=color.new(color.black, 70), border_width=1)
if barstate.islast
    table.cell(dbg, 0, 0, "RSI",  text_color=color.gray)
    table.cell(dbg, 1, 0, str.tostring(math.round(ta.rsi(close,14),1)),
               text_color=color.yellow)
    table.cell(dbg, 0, 1, "ATR",  text_color=color.gray)
    table.cell(dbg, 1, 1, str.tostring(math.round(ta.atr(14),2)),
               text_color=color.yellow)
    table.cell(dbg, 0, 2, "Pos",  text_color=color.gray)
    table.cell(dbg, 1, 2, str.tostring(strategy.position_size),
               text_color=color.green)
```

## Yaygin Debug Senaryolari

### Degisken neden na?
```pine
bgcolor(na(myVar) ? color.new(color.red, 80) : na, title="isNA")
```

### Kosul ne zaman atiyor?
```pine
bgcolor(myCondition ? color.new(color.green, 85) : na)
```

### request.security dogru calisiyor mu?
```pine
htf = request.security(syminfo.tickerid, "D", close)
plot(htf, "HTF Close", color.orange)
```
