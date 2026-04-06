# strategy.* Fonksiyonlari — Pine Script v6
Maintainer: Ugur Pala — mail@ugurpala.com

## Deklarasyon
```pine
//@version=6
strategy("Strategy Name", overlay=true, 
         initial_capital=10000, 
         default_qty_type=strategy.percent_of_equity,
         default_qty_value=10,
         commission_type=strategy.commission.percent,
         commission_value=0.1)
```

## Emir Giris
```pine
strategy.entry("Long",  strategy.long)   // piyasadan long
strategy.entry("Short", strategy.short)  // piyasadan short

// Limit ile
strategy.entry("Long", strategy.long, limit=1500.0)

// Stop ile
strategy.entry("Long", strategy.long, stop=1600.0)

// Miktar ile
strategy.entry("Long", strategy.long, qty=100)
```

## Pozisyon Kapama
```pine
strategy.close("Long")           // ID ile kapat
strategy.close_all()             // Hepsini kapat
strategy.exit("Exit", "Long",
    profit=100,   // tick cinsinden kar hedefi
    loss=50,      // tick cinsinden zarar durdurma
    trail_points=20)
```

## Strateji Bilgisi
```pine
strategy.position_size      // Pozisyon buyuklugu (+ long, - short, 0 yok)
strategy.equity             // Toplam sermaye
strategy.netprofit          // Net kar
strategy.opentrades         // Acik islem sayisi
strategy.closedtrades       // Kapali islem sayisi
strategy.position_avg_price // Ortalama giris fiyati
```

## Ornek
```pine
//@version=6
strategy("MA Cross", overlay=true)
fast = ta.ema(close, 9)
slow = ta.ema(close, 21)

if ta.crossover(fast, slow)
    strategy.entry("Long", strategy.long)
if ta.crossunder(fast, slow)
    strategy.close("Long")

plot(fast, color=color.green)
plot(slow, color=color.red)
```
