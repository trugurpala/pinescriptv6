# LLM Manifest — Pine Script v6
# Maintainer: Ugur Pala · mail@ugurpala.com

---

## TR | Türkçe

Bu dosya, yapay zekanın hangi soruda hangi referans dosyasını okuması
gerektiğini belirleyen yönlendirme haritasıdır.

### Protokol
1. Kullanıcının isteğini belirle
2. Aşağıdaki tablodan ilgili dosyayı bul
3. **Her zaman önce `LESSONS_LEARNED.md`'yi kontrol et**
4. Yalnızca ilgili dosyayı oku (context penceresi verimliliği için)

### Kavramlar ve Temel Dil

| Anahtar Kelime | Dosya |
|----------------|-------|
| barstate, var, varip, history, realtime | `concepts/execution_model.md` |
| repainting, request.security, HTF, MTF | `concepts/timeframes.md` |
| color.new, from_gradient, bgcolor | `concepts/colors_and_display.md` |
| max_bars_back, series string, hata | `concepts/common_errors.md` |
| method, user-defined method | `concepts/methods.md` |
| type, UDT, object, field | `concepts/objects.md` |

### API Referansı

| Anahtar Kelime | Dosya |
|----------------|-------|
| open, close, high, low, volume, bar_index, syminfo | `reference/variables.md` |
| color.red, shape.*, plot.style_*, size.* | `reference/constants.md` |
| int, float, bool, string, series, simple | `reference/types.md` |
| if, for, while, switch, var, varip, export | `reference/keywords.md` |
| @version, @param, @returns, @type | `reference/annotations.md` |

### Fonksiyonlar

| İhtiyaç | Dosya |
|---------|-------|
| RSI, EMA, SMA, MACD, ATR, BB, crossover, pivot | `reference/functions/ta.md` |
| strategy.entry, exit, close, position_size | `reference/functions/strategy.md` |
| plot, line.new, box.new, label.new, table | `reference/functions/drawing.md` |
| request.security, financial, currency_rate | `reference/functions/request.md` |
| array, map, matrix | `reference/functions/collections.md` |
| math, str, input, alert, timestamp | `reference/functions/general.md` |

### Kod Yazma

| İhtiyaç | Dosya |
|---------|-------|
| İsimlendirme, sıralama, yorum | `writing_scripts/style_guide.md` |
| Pine Logs, debug paneli | `writing_scripts/debugging.md` |
| Profiler, optimizasyon | `writing_scripts/profiling_and_optimization.md` |
| Script limitleri, drawing limitleri | `writing_scripts/limitations.md` |

---

## EN | English

This file is the routing map that tells the AI which reference file
to read for which query.

### Protocol
1. Identify the user's intent
2. Find the relevant file in the tables below
3. **Always check `LESSONS_LEARNED.md` first**
4. Read only the relevant file (for context window efficiency)

### Concepts & Core Language

| Keyword | File |
|---------|------|
| barstate, var, varip, history, realtime | `concepts/execution_model.md` |
| repainting, request.security, HTF, MTF | `concepts/timeframes.md` |
| color.new, from_gradient, bgcolor | `concepts/colors_and_display.md` |
| max_bars_back, series string, error | `concepts/common_errors.md` |
| method, user-defined method | `concepts/methods.md` |
| type, UDT, object, field | `concepts/objects.md` |

### API Reference

| Keyword | File |
|---------|------|
| open, close, high, low, volume, bar_index, syminfo | `reference/variables.md` |
| color.red, shape.*, plot.style_*, size.* | `reference/constants.md` |
| int, float, bool, string, series, simple | `reference/types.md` |
| if, for, while, switch, var, varip, export | `reference/keywords.md` |
| @version, @param, @returns, @type | `reference/annotations.md` |

### Functions

| Need | File |
|------|------|
| RSI, EMA, SMA, MACD, ATR, BB, crossover, pivot | `reference/functions/ta.md` |
| strategy.entry, exit, close, position_size | `reference/functions/strategy.md` |
| plot, line.new, box.new, label.new, table | `reference/functions/drawing.md` |
| request.security, financial, currency_rate | `reference/functions/request.md` |
| array, map, matrix | `reference/functions/collections.md` |
| math, str, input, alert, timestamp | `reference/functions/general.md` |

### Writing Scripts

| Need | File |
|------|------|
| Naming, ordering, comments | `writing_scripts/style_guide.md` |
| Pine Logs, debug panel | `writing_scripts/debugging.md` |
| Profiler, optimization | `writing_scripts/profiling_and_optimization.md` |
| Script limits, drawing limits | `writing_scripts/limitations.md` |
