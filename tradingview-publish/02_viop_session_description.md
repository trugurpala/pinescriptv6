# TradingView Publish: VIOP Session Strategy [trugurpala]

## Pine Dosyası
`examples/strategies/11_viop_session_strategy.pine`

## TradingView Title
```
VIOP Session Strategy — Seans Filtreli BIST30 [trugurpala]
```

## TradingView Description — Kopyala Yapıştır

```
VIOP / BIST30 Session-Filtered Strategy

TR: Borsa İstanbul VİOP piyasasına özel, seans saati filtrelemeli strateji.
Sabah seansı (09:30-12:30) ve öğleden sonra seansı (14:00-18:15) ayrı ayrı kontrol edilir.
Seans dışında pozisyon açılmaz. Gün sonu tüm pozisyonlar otomatik kapatılır.

EN: Strategy specifically designed for Borsa Istanbul VIOP (Turkish derivatives market).
Filters trades by session: morning (09:30-12:30) and afternoon (14:00-18:15) UTC+3.
No positions opened outside market hours. All positions auto-closed at day end.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ÖZELLİKLER / FEATURES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✅ VİOP seans filtresi — 09:30-18:15 UTC+3
✅ Gün sonu otomatik kapanış — 18:10'da tüm pozisyonlar kapatılır
✅ ATR tabanlı SL/TP — volatiliteye adaptif
✅ Hacim onayı — fakeout sinyalleri filtrelenir
✅ EMA trend filtresi — trend yönünde giriş
✅ Komisyon %0.03 — VİOP gerçekçi backtest
✅ Slippage 2 tick dahil

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SEMBOL / SYMBOL
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Önerilen: BIST:XU030 veya VİOP hisse sözleşmeleri
Önerilen TF: 5M, 15M, 1H

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
KAYNAK / SOURCE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Bu script AI destekli Pine Script v6 geliştirme ortamının bir parçasıdır.
This script is part of an AI-powered Pine Script v6 development environment.

Tüm kaynak kodlar ve 55+ örnek:
github.com/trugurpala/pinescriptv6

Yazar / Author: Ugur Pala
github.com/trugurpala | x.com/trugurpala

Pine Script v6 | MIT License | Open Source

Not: Eğitim amaçlıdır. Canlı işlemde risk yönetimi uygulayın.
Disclaimer: Educational purposes only. Apply risk management in live trading.
```

## Tags
```
viop, bist30, turkey, session, strategy, atr, ema, pinescriptv6
```
