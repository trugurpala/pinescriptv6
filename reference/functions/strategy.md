# strategy.* - Pine Script v6
Maintainer: Ugur Pala - mail@ugurpala.com

## Deklarasyon
```pine
//@version=6
strategy("Ad", overlay=true,
         initial_capital=10000,
         default_qty_type=strategy.percent_of_equity,
         default_qty_value=10,
         commission_type=strategy.commission.percent,
         commission_value=0.1)
```

## Pozisyon Acma
```pine
strategy.entry("Long",  strategy.long)
strategy.entry("Short", strategy.short)
strategy.entry("Long",  strategy.long,  limit=1500.0)
strategy.entry("Long",  strategy.long,  stop=1600.0)
strategy.entry("Long",  strategy.long,  qty=100)
```

## Kapama ve Cikis
```pine
strategy.close("Long")
strategy.close_all()
strategy.exit("Exit", "Long",
    profit=100, loss=50,
    trail_points=20, trail_offset=10)
```

## Iptal
```pine
strategy.cancel("Long")
strategy.cancel_all()
```

## Degiskenler
```pine
strategy.position_size       // + long, - short, 0 yok
strategy.equity
strategy.netprofit
strategy.opentrades
strategy.closedtrades
strategy.position_avg_price
strategy.wintrades
strategy.losstrades
```

## Ornek - EMA Kesisim
```pine
//@version=6
strategy("EMA Cross", overlay=true)
fast = ta.ema(close, 9)
slow = ta.ema(close, 21)
if ta.crossover(fast, slow)
    strategy.entry("Long", strategy.long)
if ta.crossunder(fast, slow)
    strategy.close("Long")
plot(fast, color=color.green)
plot(slow, color=color.red)
```
