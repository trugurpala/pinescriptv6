# request.* Fonksiyonlari — Pine Script v6
Maintainer: Ugur Pala — mail@ugurpala.com

## request.security()
```pine
// Baska sembolu veya timeframe'i cek
request.security(symbol, timeframe, expression, 
                 gaps, lookahead, ignore_invalid_symbol,
                 currency, calc_bars_count)

// Ornekler
daily = request.security(syminfo.tickerid, "D", close)
btc   = request.security("BINANCE:BTCUSDT", "D", close)

// Guvenli (repainting olmadan)
daily_safe = request.security(syminfo.tickerid, "D", close[1])
```

## request.financial()
```pine
// Finansal veri (P/E, EPS vb.)
pe = request.financial(syminfo.tickerid, "P_E", "TTM")
eps = request.financial(syminfo.tickerid, "EARNINGS_PER_SHARE", "FQ")
```

## request.currency_rate()
```pine
// Doviz kuru
usdtry = request.currency_rate("USD", "TRY")
```

## request.security_lower_tf()
```pine
// Alt timeframe OHLCV array olarak
lowerClose = request.security_lower_tf(syminfo.tickerid, "1", close)
// lowerClose bir array<float> dondurur
```

## Onemli Not — Repainting
```pine
// REPAINTING YAPABILIR (canli cubuk verisini kullanir)
htf = request.security(syminfo.tickerid, "D", close)

// GUVENLI
htf = request.security(syminfo.tickerid, "D", close[1])
// veya
htf = request.security(syminfo.tickerid, "D", close, 
                       lookahead=barmerge.lookahead_off)
```
