# strategy.*
> Maintainer: Ugur Pala · mail@ugurpala.com · github.com/trugurpala/pinescriptv6

---

## Deklarasyon / Declaration
```pine
//@version=6
strategy("Strateji Adı",
    overlay                   = true,
    initial_capital           = 10000,
    default_qty_type          = strategy.percent_of_equity,
    default_qty_value         = 10,
    commission_type           = strategy.commission.percent,
    commission_value          = 0.1,
    slippage                  = 1,
    calc_on_every_tick        = false,
    process_orders_on_close   = false)
```

## Pozisyon Açma / Entry
```pine
strategy.entry("Long",  strategy.long)                // piyasadan / market
strategy.entry("Short", strategy.short)
strategy.entry("Long",  strategy.long,  limit = 1500.0)   // limit emir
strategy.entry("Long",  strategy.long,  stop  = 1600.0)   // stop emir
strategy.entry("Long",  strategy.long,  qty   = 100)      // lot miktarı
```

## Çıkış / Exit
```pine
strategy.close("Long")         // ID ile kapat / close by ID
strategy.close_all()           // hepsini kapat

strategy.exit("Exit", "Long",
    profit       = 100,   // tick cinsinden kâr hedefi
    loss         = 50,    // tick cinsinden zarar durdurucu
    trail_points = 20,    // trailing stop (tick)
    trail_offset = 10)    // trailing offset (tick)
```

## İptal / Cancel
```pine
strategy.cancel("Long")        // bekleyen emri iptal
strategy.cancel_all()
```

## Bilgi Değişkenleri / Info Variables
```pine
strategy.position_size        // + long, - short, 0 yok
strategy.equity               // toplam sermaye
strategy.netprofit            // net kâr
strategy.grossprofit          // brüt kâr
strategy.grossloss            // brüt zarar
strategy.opentrades           // açık işlem sayısı
strategy.closedtrades         // kapanmış işlem
strategy.position_avg_price   // ortalama giriş
strategy.wintrades            // kazanan
strategy.losstrades           // kaybeden
```

## Örnek — ATR Tabanlı Stop/Take-Profit
```pine
//@version=6
strategy("ATR SL/TP", overlay=true)

int   lenInput  = input.int(14,  "ATR Periyodu")
float slMult    = input.float(2.0, "SL Çarpan", step=0.1)
float tpMult    = input.float(3.0, "TP Çarpan", step=0.1)

ema   = ta.ema(close, 50)
atr14 = ta.atr(lenInput)

if ta.crossover(close, ema) and strategy.position_size == 0
    strategy.entry("Long", strategy.long)
    strategy.exit("Exit Long", "Long",
        stop   = close - slMult * atr14,
        limit  = close + tpMult * atr14)

plot(ema, "EMA 50", color.orange)
```
