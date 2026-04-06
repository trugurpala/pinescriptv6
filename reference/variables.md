# Variables — Pine Script v6
Maintainer: Ugur Pala — mail@ugurpala.com

## Fiyat ve Volume Degiskenleri
open, high, low, close, volume, vwap, hl2, hlc3, ohlc4, hlcc4

## Bar ve Zaman
bar_index, time, time_close, timenow

## Sembol Bilgisi
syminfo.ticker, syminfo.tickerid, syminfo.exchange
syminfo.mintick, syminfo.pointvalue, syminfo.currency
syminfo.description, syminfo.type

## Timeframe
timeframe.period, timeframe.multiplier, timeframe.isminutes
timeframe.ishours, timeframe.isdaily, timeframe.isweekly
timeframe.ismonthly, timeframe.in_seconds()

## Strateji
strategy.equity, strategy.position_size, strategy.opentrades
strategy.closedtrades, strategy.netprofit, strategy.grossprofit
strategy.grossloss, strategy.position_avg_price

## Ornek
```pine
//@version=6
indicator("Variables demo")
plot(close)           // kapanis
plot(hl2)             // (high+low)/2
plot(bar_index)       // cubuk numarasi
label.new(bar_index, high, syminfo.ticker)
```
