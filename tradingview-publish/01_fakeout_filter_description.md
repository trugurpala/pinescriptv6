# TradingView Publish: Fakeout Filter [trugurpala]

## Pine Dosyası
`examples/indicators/18_fakeout_filter.pine`

## TradingView Title
```
Fakeout Filter — 4-Layer Signal Quality [trugurpala]
```

## TradingView Description — Kopyala Yapıştır

```
Fakeout Filter — 4-Layer Signal Quality

TR: Pine Script v6 ile yazılmış, 4 katmanlı sahte sinyal filtresi.
Her sinyalin kalitesini 0-4 arasında skorlar.
Skor 3-4 = Güçlü sinyal. Skor 0-1 = Muhtemelen fakeout.

EN: 4-layer fakeout filter written in Pine Script v6.
Scores every signal 0–4.
Score 3-4 = Strong signal. Score 0-1 = Likely fakeout.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
4 FİLTRE / 4 FILTERS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

F1 — Hacim Onayı / Volume Confirmation
Gerçek hareketler yüksek hacimle gelir.
Real moves come with high volume.
→ volume > sma(volume,20) × mult

F2 — HTF Trend Filtresi / Higher Timeframe Filter
Alt TF sinyalini üst TF trendi ile onayla.
Confirm lower TF signal with higher TF trend.
→ close > request.security(htfEma)[1]

F3 — ATR Gürültü Filtresi / ATR Noise Filter
Hareket gürültüden büyük mü?
Is the move larger than market noise?
→ abs(close - close[1]) > atr × mult

F4 — EMA Hizalama / EMA Alignment
Hızlı EMA yavaş EMA üzerinde mi?
Is the fast EMA above the slow EMA?
→ ema(fast) > ema(slow)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
SKOR / SCORE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🟢 3-4 → Güçlü sinyal / Strong → Giriş yap / Enter
🟡 2   → Orta / Medium → Dikkatli / Cautious
🔴 0-1 → Zayıf / Weak → Bekleme / Wait

Sağ üst köşedeki tablo her filtrenin ✓/✗ durumunu gösterir.
Top-right table shows each filter's ✓/✗ status in real time.

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
```

## Tags
```
pinescript, pinescriptv6, fakeout, signal, filter, volume, mtf, atr, indicator
```

## Publish Ayarları
- Visibility: Public
- Script type: Indicator
- Overlay: No (ayrı panel)
