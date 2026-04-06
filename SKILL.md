---
name: pinescript-v6
description: Pine Script v6 gelistirici skill — dogru v6 kodu yazar, hatalari takip eder.
maintainer: Ugur Pala · mail@ugurpala.com
repo: github.com/trugurpala/pinescriptv6
---

# Pine Script v6 — Skill

---

## TR | Türkçe

### Görev
Pine Script v6 ile doğru, optimize edilmiş kod yaz.
Kod yazmadan önce referansları oku. Hata çözümlerini kaydet.

### Protokol

**1. Kod yazmadan önce**
- `LESSONS_LEARNED.md` oku — bilinen hatalar burada
- `LLM_MANIFEST.md` ile göreve uygun dosyayı bul ve oku

**2. Kod kuralları**
- `//@version=6` — her scriptin ilk satırı
- `ta.*` kullan, manuel hesaplama yazma
- `var` / `varip` execution model'e göre doğru kullan
- Referansta olmayan fonksiyon adı uydurma

**3. Hata olduğunda**
- Hatayı çöz
- `LESSONS_LEARNED.md` dosyasına hemen ekle (mesaj / sebep / çözüm / örnek)

### Referans Haritası

| İhtiyaç | Dosya |
|---------|-------|
| RSI, EMA, MACD, crossover, ATR, pivot | `reference/functions/ta.md` |
| strategy.entry, exit, close, position | `reference/functions/strategy.md` |
| plot, line, box, label, table | `reference/functions/drawing.md` |
| request.security, MTF | `reference/functions/request.md` |
| array, map, matrix | `reference/functions/collections.md` |
| math, str, input, alert | `reference/functions/general.md` |
| open, close, bar_index, syminfo | `reference/variables.md` |
| color.red, shape.*, style.* | `reference/constants.md` |
| int, float, series, simple | `reference/types.md` |
| if, for, var, varip, switch | `reference/keywords.md` |
| @version, @param, @returns | `reference/annotations.md` |
| barstate, var, history, realtime | `concepts/execution_model.md` |
| Repainting, HTF | `concepts/timeframes.md` |
| color.new, gradient | `concepts/colors_and_display.md` |
| Bilinen hatalar | `concepts/common_errors.md` |
| Pine Logs, debug | `writing_scripts/debugging.md` |
| Optimizasyon | `writing_scripts/profiling_and_optimization.md` |
| Limitler | `writing_scripts/limitations.md` |

### Kontrol Listesi
- [ ] LESSONS_LEARNED.md okundu
- [ ] `//@version=6` mevcut
- [ ] Fonksiyon imzaları referansla doğrulandı
- [ ] v5 syntax yok
- [ ] `var`/`varip` doğru
- [ ] request.security varsa repainting kontrolü yapıldı

---

## EN | English

### Task
Write correct, optimized Pine Script v6 code.
Read references before writing. Record error fixes.

### Protocol

**1. Before writing code**
- Read `LESSONS_LEARNED.md` — known errors are there
- Use `LLM_MANIFEST.md` to find and read the correct reference file

**2. Code rules**
- `//@version=6` — first line of every script
- Use `ta.*` — never reimplement manually
- Use `var` / `varip` correctly per the execution model
- Never invent function names not in the reference docs

**3. On error**
- Solve it
- Immediately append to `LESSONS_LEARNED.md` (message / cause / fix / example)

### Reference Map

| Need | File |
|------|------|
| RSI, EMA, MACD, crossover, ATR, pivot | `reference/functions/ta.md` |
| strategy.entry, exit, close, position | `reference/functions/strategy.md` |
| plot, line, box, label, table | `reference/functions/drawing.md` |
| request.security, MTF | `reference/functions/request.md` |
| array, map, matrix | `reference/functions/collections.md` |
| math, str, input, alert | `reference/functions/general.md` |
| open, close, bar_index, syminfo | `reference/variables.md` |
| color.red, shape.*, style.* | `reference/constants.md` |
| int, float, series, simple | `reference/types.md` |
| if, for, var, varip, switch | `reference/keywords.md` |
| @version, @param, @returns | `reference/annotations.md` |
| barstate, var, history, realtime | `concepts/execution_model.md` |
| Repainting, HTF | `concepts/timeframes.md` |
| color.new, gradient | `concepts/colors_and_display.md` |
| Known errors | `concepts/common_errors.md` |
| Pine Logs, debug | `writing_scripts/debugging.md` |
| Optimization | `writing_scripts/profiling_and_optimization.md` |
| Limits | `writing_scripts/limitations.md` |

### Checklist
- [ ] LESSONS_LEARNED.md read
- [ ] `//@version=6` present
- [ ] Function signatures verified against reference
- [ ] No v5 syntax
- [ ] `var`/`varip` correct
- [ ] Repainting checked if request.security used
