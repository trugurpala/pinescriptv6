---
name: pinescript-v6
description: Pine Script v6 uzman gelistirici skill - TradingView indiktor ve stratejileri icin dogru v6 kodu yazar, hatalari takip eder.
maintainer: Ugur Pala - mail@ugurpala.com
repo: github.com/trugurpala/pinescriptv6
---

# Pine Script v6 Gelistirici Skill

## Gorev
Pine Script v6 ile dogru, optimize edilmis, iyi yapilandirilmis kod yaz.
Her seferinde once LESSONS_LEARNED.md'yi kontrol et.

## Kod Yazma Protokolu

### 1. Kod Yazmadan Once
- LESSONS_LEARNED.md'yi kontrol et (ayni hatalar tekrarlanmasin)
- LLM_MANIFEST.md'ye bak, ilgili referans dosyasini oku

### 2. Kod Kurallari
- Her script //@version=6 ile baslIyor
- Manuel hesaplama yerine ta.* kullan
- var/varip kullanimi execution model'e gore dogru olmali
- Referansta olmayan fonksiyon adi uydurma - v6'da yoktur

### 3. Hata Oldugunda
HEMEN LESSONS_LEARNED.md'yi guncelle:
- Hata mesaji
- Sebep
- Cozum
- Kod ornegi

## Referans Dosya Haritasi

| Ihtiyac | Dosya |
|---------|-------|
| ta.rsi, ta.ema, ta.crossover | reference/functions/ta.md |
| strategy.entry, exit, position | reference/functions/strategy.md |
| plot, line, box, label, table | reference/functions/drawing.md |
| request.security, MTF | reference/functions/request.md |
| array, map, matrix | reference/functions/collections.md |
| math, str, input, alert | reference/functions/general.md |
| open, close, bar_index, syminfo | reference/variables.md |
| color.red, shape.*, style.* | reference/constants.md |
| int, float, series, simple | reference/types.md |
| if, for, var, varip | reference/keywords.md |
| Yaygin hatalar | concepts/common_errors.md |
| Execution model | concepts/execution_model.md |
| Repainting, HTF | concepts/timeframes.md |

## Kontrol Listesi
- [ ] LESSONS_LEARNED.md kontrol edildi
- [ ] //@version=6 mevcut
- [ ] Fonksiyon imzalari referansla dogrulandi
- [ ] v5 syntax yok
- [ ] var/varip dogru kullanildi
- [ ] request.security varsa repainting kontrolu yapildi
