# Strategy Declaration Changes
> v5 to v6 — github.com/trugurpala/pinescriptv6

---

## TR | Türkçe

Strategy declaration v6'da aynı kaldı — sadece version değişir.

```pine
// ❌ v5
//@version=5
strategy("My Strategy", overlay=true,
    initial_capital=10000,
    default_qty_type=strategy.percent_of_equity,
    default_qty_value=10)

// ✅ v6
//@version=6
strategy("My Strategy", overlay=true,
    initial_capital=10000,
    default_qty_type=strategy.percent_of_equity,
    default_qty_value=10)
```

### strategy.entry() — değişen yok

```pine
//@version=6
strategy("Demo", overlay=true)
if ta.crossover(ta.ema(close,9), ta.ema(close,21))
    strategy.entry("Long", strategy.long)
if ta.crossunder(ta.ema(close,9), ta.ema(close,21))
    strategy.close("Long")
```

### Yeni v6 özelliği — process_orders_on_close

```pine
//@version=6
strategy("Demo", overlay=true,
    process_orders_on_close=true)  // v6'da eklendi
```

---

## EN | English

Strategy declaration is mostly unchanged — only the version number changes.

### New in v6: process_orders_on_close parameter

```pine
//@version=6
strategy("Demo", overlay=true,
    process_orders_on_close=true)
```
