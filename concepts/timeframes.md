# Timeframes — Pine Script v6
Maintainer: Ugur Pala — mail@ugurpala.com

## request.security Temeli

```pine
//@version=6
indicator("MTF", overlay=true)
daily_close = request.security(syminfo.tickerid, "D", close)
weekly_ema  = request.security(syminfo.tickerid, "W", ta.ema(close, 20))
plot(daily_close)
plot(weekly_ema)
```

## Repainting Onleme

```pine
// REPAINTING YAPABILIR
htf = request.security(syminfo.tickerid, "D", close)

// GUVENLI — kapanmis cubuk
htf_safe = request.security(syminfo.tickerid, "D", close[1])
```

## Timeframe Stringleri
"1"=1dk, "5"=5dk, "15"=15dk, "60"=1sa, "240"=4sa, "D"=gunluk, "W"=haftalik, "M"=aylik

## timeframe.period
```pine
isDaily = timeframe.in_seconds() >= timeframe.in_seconds("D")
```
