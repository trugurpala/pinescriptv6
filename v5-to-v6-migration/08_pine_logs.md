# Pine Logs — New in v6
> v5 to v6 — github.com/trugurpala/pinescriptv6

---

## TR | Türkçe

v5'te runtime logging yoktu. v6'da `log.*` namespace'i eklendi.

### Temel kullanım

```pine
//@version=6
indicator("Pine Logs Demo")

rsi = ta.rsi(close, 14)
atr = ta.atr(14)

// Her son barda log yaz
if barstate.islast
    log.info("Bar: {0} | Close: {1} | RSI: {2}",
        bar_index,
        str.tostring(close, format.mintick),
        str.tostring(math.round(rsi, 2)))

// Koşullu uyarı
if rsi > 70
    log.warning("RSI aşırı alım: {0}", math.round(rsi, 1))

// Hata logla
if close < 0
    log.error("Geçersiz fiyat: {0}", close)
```

### Log seviyeleri

| Fonksiyon | Seviye | Renk |
|-----------|--------|------|
| `log.info()` | Bilgi | Mavi |
| `log.warning()` | Uyarı | Sarı |
| `log.error()` | Hata | Kırmızı |

### Pine Editor'da nasıl açılır

TradingView → Pine Editor → sağ alttaki **Pine Logs** paneli

### Format string kullanımı

```pine
//@version=6
indicator("Format demo")
log.info("Sembol: {0} | TF: {1} | Bar: {2}",
    syminfo.ticker,
    timeframe.period,
    bar_index)
```

---

## EN | English

v5 had no runtime logging. v6 added the `log.*` namespace.

```pine
//@version=6
indicator("Pine Logs Demo")
if barstate.islast
    log.info("Bar: {0} | RSI: {1}", bar_index, math.round(ta.rsi(close,14), 2))
    log.warning("ATR: {0}", math.round(ta.atr(14), 4))
```

### How to open Pine Logs

TradingView → Pine Editor → **Pine Logs** panel (bottom right)
