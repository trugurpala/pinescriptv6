---
name: pinescript-v6
description: "Pine Script v6 uzman gelistirici skill - TradingView indiktor ve stratejileri icin dogru, optimize edilmis v6 kodu yazar. Hatalari takip eder ve LESSONS_LEARNED.md'yi otomatik gunceller."
maintainer: "Ugur Pala - mail@ugurpala.com"
repo: "github.com/trugurpala/pinescriptv6"
triggers:
  - Pine Script
  - PineScript
  - indicator
  - strategy
  - TradingView
  - indiktor
  - strateji
  - v6
  - pine
  - BIST
  - VIOP
  - XU030
---

# Pine Script v6 Gelistirici Skill

## Gorev
Pine Script v6 ile dogru, optimize ve iyi yapilandirilmis kod yaz.
Kod yazmadan once mutlaka referans dokumantasyonuna basvur.
Her hata cozumunden sonra LESSONS_LEARNED.md'yi guncelle.

## Protokol

### 1. Kod Yazmadan Once
- LESSONS_LEARNED.md kontrol et (ayni hatalari tekrarlama)
- LLM_MANIFEST.md ile ilgili referans dosyasini bul ve oku

### 2. Kod Kurallari
- //@version=6 ile basla
- Manuel hesaplama yerine ta.* kullan
- var / varip execution model'e gore dogru kullan
- Referansta olmayan fonksiyon adi uydurma

### 3. Hata Oldugunda
HEMEN LESSONS_LEARNED.md'yi guncelle:
- Hata mesaji
- Sebep
- Cozum + kod ornegi

## Referans Dosya Haritasi

| Ihtiyac | Dosya |
|---------|-------|
| ta.rsi, ta.ema, ta.macd, ta.crossover, ta.atr, ta.pivot | reference/functions/ta.md |
| strategy.entry, exit, close, position_size | reference/functions/strategy.md |
| plot, line, box, label, table, plotshape | reference/functions/drawing.md |
| request.security, financial, MTF | reference/functions/request.md |
| array, map, matrix | reference/functions/collections.md |
| math, str, input, alert, timestamp | reference/functions/general.md |
| open, close, high, low, bar_index, syminfo | reference/variables.md |
| color.red, shape.*, plot.style_* | reference/constants.md |
| int, float, bool, series, simple | reference/types.md |
| if, for, var, varip, switch | reference/keywords.md |
| @version, @param, @returns | reference/annotations.md |
| max_bars_back, series string hatasi | concepts/common_errors.md |
| barstate, var, history, realtime | concepts/execution_model.md |
| request.security, repainting | concepts/timeframes.md |
| color.new, color.from_gradient | concepts/colors_and_display.md |
| User-defined methods | concepts/methods.md |
| UDT, type, object | concepts/objects.md |
| Pine Logs, debug | writing_scripts/debugging.md |
| Profiler, optimizasyon | writing_scripts/profiling_and_optimization.md |
| Script limitleri | writing_scripts/limitations.md |
| Kod stili | writing_scripts/style_guide.md |

## Kontrol Listesi
- [ ] LESSONS_LEARNED.md kontrol edildi
- [ ] //@version=6 mevcut
- [ ] Fonksiyon imzalari referansla dogrulandi
- [ ] v5 syntax yok
- [ ] var/varip dogru
- [ ] Repainting kontrolu yapildi (request.security varsa)
