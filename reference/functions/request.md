# request.*
> Maintainer: Ugur Pala · mail@ugurpala.com · github.com/trugurpala/pinescriptv6

---

## request.security() — Temel / Basic
```pine
// Farklı timeframe / Different timeframe
dailyClose = request.security(syminfo.tickerid, "D", close)
weeklyEma  = request.security(syminfo.tickerid, "W", ta.ema(close, 20))

// Farklı sembol / Different symbol
btcClose   = request.security("BINANCE:BTCUSDT", "D", close)
xu030Daily = request.security("BIST:XU030", "D", close)
```

## Repainting Önleme / Prevent Repainting
```pine
// ❌ Canlı bar — repainting yapabilir / Live bar — may repaint
htf = request.security(syminfo.tickerid, "D", close)

// ✅ Kapanmış bar — güvenli / Confirmed bar — safe
htf_safe = request.security(syminfo.tickerid, "D", close[1])
```

## Çoklu Değer — Tuple / Multiple Values
```pine
[htfOpen, htfHigh, htfLow, htfClose] =
    request.security(syminfo.tickerid, "D", [open, high, low, close])
```

## Alt Timeframe / Lower Timeframe
```pine
// array<float> döndürür / returns array<float>
lowerCloses = request.security_lower_tf(syminfo.tickerid, "1", close)
```

## request.financial()
```pine
pe  = request.financial(syminfo.tickerid, "P_E",                  "TTM")
eps = request.financial(syminfo.tickerid, "EARNINGS_PER_SHARE",    "FQ")
rev = request.financial(syminfo.tickerid, "TOTAL_REVENUE",         "FY")
```

## request.currency_rate()
```pine
usdtry = request.currency_rate("USD", "TRY")
eurusd = request.currency_rate("EUR", "USD")
```

## Limitler / Limits
- TR: Bir scriptte maksimum 40 `request.security()` çağrısı
- EN: Maximum 40 `request.security()` calls per script
- TR: Performans için çağrıları birleştir (tuple kullan)
- EN: Combine calls for performance (use tuple)
