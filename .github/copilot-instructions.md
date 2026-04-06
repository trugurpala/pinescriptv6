# Pine Script v6 — GitHub Copilot Instructions
# Maintainer: Ugur Pala · mail@ugurpala.com
# github.com/trugurpala/pinescriptv6

## TR | Türkçe
Pine Script v6 kodu yazmak için şu protokolü takip et:

1. **Her zaman önce** `LESSONS_LEARNED.md` dosyasını oku — bilinen hatalar ve çözümleri burada
2. `LLM_MANIFEST.md` dosyasına bak — göreve uygun referans dosyasını belirle
3. Referans dosyasını oku, sonra kodu yaz
4. Hata alırsan: çöz + `LESSONS_LEARNED.md`'ye ekle

### Kod Kuralları
- `//@version=6` — her scriptin ilk satırı
- `ta.*` fonksiyonlarını kullan
- `var` / `varip` execution model'e göre
- v5 syntax kullanma

## EN | English
Follow this protocol when writing Pine Script v6 code:

1. **Always first** read `LESSONS_LEARNED.md` — known errors and fixes are there
2. Check `LLM_MANIFEST.md` — find the correct reference file for the task
3. Read that file, then write the code
4. On error: solve it + append to `LESSONS_LEARNED.md`

### Code Rules
- `//@version=6` — first line of every script
- Use `ta.*` functions
- Use `var` / `varip` per the execution model
- No v5 syntax

## Reference Map / Referans Haritası
| Need | File |
|------|------|
| ta.rsi, ta.ema, ta.crossover | reference/functions/ta.md |
| strategy.entry, exit | reference/functions/strategy.md |
| plot, line, label, table | reference/functions/drawing.md |
| request.security | reference/functions/request.md |
| array, map | reference/functions/collections.md |
| math, str, input | reference/functions/general.md |
| Errors | concepts/common_errors.md |
