# request.* - Pine Script v6
Maintainer: Ugur Pala - mail@ugurpala.com

## request.security()
```pine
dailyClose = request.security(syminfo.tickerid, "D", close)
weeklyEma  = request.security(syminfo.tickerid, "W", ta.ema(close, 20))
btcClose   = request.security("BINANCE:BTCUSDT", "D", close)

// GUVENLI - repainting yok
htf_safe = request.security(syminfo.tickerid, "D", close[1])

// Coklu deger
[o, h, l, c] = request.security(syminfo.tickerid, "D",
                                 [open, high, low, close])
```

## request.security_lower_tf()
```pine
lowerCloses = request.security_lower_tf(syminfo.tickerid, "1", close)
// array<float> dondurur
```

## request.financial()
```pine
pe  = request.financial(syminfo.tickerid, "P_E", "TTM")
eps = request.financial(syminfo.tickerid, "EARNINGS_PER_SHARE", "FQ")
```

## request.currency_rate()
```pine
usdtry = request.currency_rate("USD", "TRY")
```

## Limitler
- Max 40 request.security() per script
- Performans icin minimize et
- Koleksiyon dondururken memory dikkat
