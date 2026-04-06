# TradingView Publish: Fakeout-Confirmed Strategy [trugurpala]

## Pine Dosyası
`examples/strategies/13_fakeout_confirmed_strategy.pine`

## TradingView Title
```
Fakeout-Confirmed Strategy — Volume + HTF + ATR + Bar [trugurpala]
```

## TradingView Description — Kopyala Yapıştır

```
Fakeout-Confirmed Strategy — 4 Filter Layers

TR: Tüm 4 fakeout filtresi aktif olan, yüksek kaliteli sinyaller arayan strateji.
Her filtre ayrı ayrı açılıp kapatılabilir.
Az filtre = çok sinyal. Çok filtre = yüksek doğruluk.

EN: Strategy that seeks only high-quality signals with all 4 fakeout filters active.
Each filter can be toggled independently.
Fewer filters = more signals. More filters = higher accuracy.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4 FİLTRE / 4 FILTERS (hepsi açılıp kapanabilir)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

F1 — Hacim Onayı / Volume Filter
→ volume > sma(volume, len) × multiplier

F2 — HTF Trend Filtresi / Higher Timeframe Filter
→ close > request.security(htfEma)[1]  ← repainting yok / no repainting

F3 — Bar Onayı / Bar Confirmation
→ N bar sinyal yönünde kapanmalı

F4 — ATR Gürültü / ATR Noise Filter
→ abs(close - close[1]) > atr × multiplier

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
GÖRSEL / VISUALS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🟢 Yeşil üçgen → Onaylı long sinyal
🔴 Kırmızı üçgen → Onaylı short sinyal
⚪ Küçük daire → Filtrelenmiş sinyal (karşılaştırma için)

Sağ üst tablo: Her filtrenin anlık durumu ✓/✗

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
pinescriptv6, fakeout, strategy, volume, htf, atr, filter, signal
```
