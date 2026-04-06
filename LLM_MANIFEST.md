# LLM Manifest — Pine Script v6
# Repo: github.com/trugurpala/pinescriptv6
# Maintainer: Ugur Pala · mail@ugurpala.com

TR: Bu dosya AI'ın hangi soruda hangi referans dosyasını okuyacağını belirler.
EN: This file tells the AI which reference file to read for each type of query.

---

## Protokol / Protocol

1. TR: LESSONS_LEARNED.md'yi kontrol et — bilinen hataları tekrarlama
   EN: Check LESSONS_LEARNED.md — never repeat a known error

2. TR: Aşağıdaki tablodan ilgili dosyayı bul ve ONU oku
   EN: Find the relevant file below and read ONLY that file

3. TR: Kodu yaz, hata olursa LESSONS_LEARNED.md'yi güncelle
   EN: Write code; on error update LESSONS_LEARNED.md

---

## 1. Kavramlar / Concepts

| Anahtar Kelimeler / Keywords | Dosya / File |
|---|---|
| barstate, var, varip, history, realtime | `concepts/execution_model.md` |
| max_bars_back, series string, undeclared | `concepts/common_errors.md` |
| request.security, repainting, HTF, MTF | `concepts/timeframes.md` |
| color.new, from_gradient, bgcolor | `concepts/colors_and_display.md` |
| method, user-defined method | `concepts/methods.md` |
| type, UDT, object, field | `concepts/objects.md` |

## 2. Referans / Reference

| Anahtar Kelimeler / Keywords | Dosya / File |
|---|---|
| open, close, high, low, bar_index, syminfo | `reference/variables.md` |
| color.red, shape.triangle, plot.style_line | `reference/constants.md` |
| int, float, bool, series, simple | `reference/types.md` |
| if, for, while, var, varip, switch | `reference/keywords.md` |
| @version, @param, @returns, @type | `reference/annotations.md` |

## 3. Fonksiyonlar / Functions

| İhtiyaç / Need | Dosya / File |
|---|---|
| ta.rsi, ta.ema, ta.macd, ta.atr, ta.crossover, ta.pivot | `reference/functions/ta.md` |
| strategy.entry, strategy.exit, strategy.close | `reference/functions/strategy.md` |
| plot, line.new, box.new, label.new, table | `reference/functions/drawing.md` |
| request.security, request.financial | `reference/functions/request.md` |
| array, map, matrix | `reference/functions/collections.md` |
| math, str, input, alert, timestamp | `reference/functions/general.md` |

## 4. Kod Yazma / Writing

| İhtiyaç / Need | Dosya / File |
|---|---|
| İsimlendirme, sıralama / Naming, ordering | `writing_scripts/style_guide.md` |
| Pine Logs, debug | `writing_scripts/debugging.md` |
| Performans / Performance | `writing_scripts/profiling_and_optimization.md` |
| Limitler / Limits | `writing_scripts/limitations.md` |

---

## Örnekler / Examples

| Görev / Task | Oku / Read |
|---|---|
| RSI indikatörü yaz | `reference/functions/ta.md` + `reference/functions/drawing.md` |
| EMA strateji yaz | `reference/functions/ta.md` + `reference/functions/strategy.md` |
| Çoklu TF (MTF) | `reference/functions/request.md` + `concepts/timeframes.md` |
| Hata alıyorum | `concepts/common_errors.md` + `LESSONS_LEARNED.md` |
| Değişkenim neden sıfırlanıyor | `concepts/execution_model.md` |
