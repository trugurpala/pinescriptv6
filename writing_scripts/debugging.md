# Debugging
> Maintainer: Ugur Pala · mail@ugurpala.com · github.com/trugurpala/pinescriptv6

---

## TR | Türkçe

### Pine Logs — Tavsiye Edilen Yöntem

TradingView → Pine Editor → Pine Logs paneli

```pine
//@version=6
indicator("Debug")

rsi = ta.rsi(close, 14)
atr = ta.atr(14)

if barstate.islast
    log.info("Bar {0} | RSI: {1} | ATR: {2}", bar_index, math.round(rsi, 2), math.round(atr, 4))
    log.warning("Pozisyon: {0}", strategy.position_size)
```

### Görsel Debug — plot()

```pine
// Değeri veri penceresinde göster
plot(myVar, "Debug", display=display.data_window)

// Koşul tetikleniyor mu?
bgcolor(myCondition ? color.new(color.green, 85) : na)
```

### Tablo ile Debug Paneli

```pine
var table dbg = table.new(position.top_left, 2, 4,
                          bgcolor=color.new(color.black, 70), border_width=1)
if barstate.islast
    table.cell(dbg, 0, 0, "RSI",  text_color=color.gray)
    table.cell(dbg, 1, 0, str.tostring(math.round(ta.rsi(close,14), 1)), text_color=color.yellow)
    table.cell(dbg, 0, 1, "ATR",  text_color=color.gray)
    table.cell(dbg, 1, 1, str.tostring(math.round(ta.atr(14), 2)), text_color=color.yellow)
```

### Yaygın Senaryolar

```pine
// Değişken neden na?
bgcolor(na(myVar) ? color.new(color.red, 80) : na, title="isNA?")

// Koşul ne zaman ateşleniyor?
plotshape(myCondition, style=shape.circle, location=location.abovebar, size=size.tiny)

// request.security doğru çalışıyor mu?
htf = request.security(syminfo.tickerid, "D", close)
plot(htf, "HTF Close", color.orange)
```

---

## EN | English

### Pine Logs — Recommended

TradingView → Pine Editor → Pine Logs panel

```pine
//@version=6
indicator("Debug")

rsi = ta.rsi(close, 14)
atr = ta.atr(14)

if barstate.islast
    log.info("Bar {0} | RSI: {1} | ATR: {2}", bar_index, math.round(rsi, 2), math.round(atr, 4))
    log.warning("Position: {0}", strategy.position_size)
```

### Visual Debug — plot()

```pine
// Show value in data window
plot(myVar, "Debug", display=display.data_window)

// Is condition firing?
bgcolor(myCondition ? color.new(color.green, 85) : na)
```

### Table Debug Panel

```pine
var table dbg = table.new(position.top_left, 2, 4,
                          bgcolor=color.new(color.black, 70), border_width=1)
if barstate.islast
    table.cell(dbg, 0, 0, "RSI",  text_color=color.gray)
    table.cell(dbg, 1, 0, str.tostring(math.round(ta.rsi(close,14), 1)), text_color=color.yellow)
    table.cell(dbg, 0, 1, "ATR",  text_color=color.gray)
    table.cell(dbg, 1, 1, str.tostring(math.round(ta.atr(14), 2)), text_color=color.yellow)
```

### Common Scenarios

```pine
// Why is variable na?
bgcolor(na(myVar) ? color.new(color.red, 80) : na, title="isNA?")

// When is condition firing?
plotshape(myCondition, style=shape.circle, location=location.abovebar, size=size.tiny)

// Is request.security working?
htf = request.security(syminfo.tickerid, "D", close)
plot(htf, "HTF Close", color.orange)
```
