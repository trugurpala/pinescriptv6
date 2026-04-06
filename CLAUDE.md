# Pine Script v6 — Claude Instructions
> Author: Ugur Pala · mail@ugurpala.com · github.com/trugurpala/pinescriptv6

TR: Bu dosya Claude Code ve Claude Projects tarafından otomatik okunur.
EN: This file is automatically read by Claude Code and Claude Projects.

---

## Protocol / Protokol

**Before writing any code / Kod yazmadan önce:**

1. Read `LESSONS_LEARNED.md` — known errors and fixes / bilinen hatalar ve çözümler
2. Check `LLM_MANIFEST.md` — find the correct reference file / doğru dosyayı bul
3. Read that reference file / o dosyayı oku
4. Write the code / kodu yaz
5. On error: solve it + append to `LESSONS_LEARNED.md` / Hata olursa: çöz + ekle

---

## Code Rules / Kod Kuralları

```pine
//@version=6          // TR: Her scriptin ilk satırı / EN: First line of every script
```

- `ta.*` fonksiyonlarını kullan — manuel yeniden yazma / use `ta.*` — never reimplement
- `var` / `varip` execution model'e göre / per execution model
- Fonksiyon adı uydurma / never invent function names
- v5 syntax kullanma / no v5 syntax (`study()`, `security()`, `input()` → `input.*`)

---

## Reference Map / Referans Haritası

| Need / İhtiyaç | File / Dosya |
|----------------|-------------|
| RSI, EMA, MACD, ATR, crossover | `reference/functions/ta.md` |
| strategy.entry, exit, position | `reference/functions/strategy.md` |
| plot, line, box, label, table | `reference/functions/drawing.md` |
| request.security, MTF | `reference/functions/request.md` |
| array, map, matrix | `reference/functions/collections.md` |
| math, str, input, alert | `reference/functions/general.md` |
| Errors / Hatalar | `concepts/common_errors.md` |
| var, varip, barstate | `concepts/execution_model.md` |
| **Always first / Her zaman önce** | `LESSONS_LEARNED.md` |

---

## Checklist / Kontrol Listesi

- [ ] `LESSONS_LEARNED.md` read / okundu
- [ ] `//@version=6` present / mevcut
- [ ] Function signatures verified / İmzalar doğrulandı
- [ ] No v5 syntax / v5 syntax yok
- [ ] `var`/`varip` correct / doğru
- [ ] Repainting checked if `request.security` used

---

## Examples / Örnekler

```
examples/indicators/   — 17 ready indicators / 17 hazır indikatör
examples/strategies/   — 12 ready strategies / 12 hazır strateji
webhook-templates/     — Telegram, Discord, JSON webhook templates
v5-to-v6-migration/    — v5 → v6 migration guide
```

> TR: TradingView Pine Script v6 resmi dokümantasyonu temel referans materyalidir.
> EN: TradingView Pine Script v6 official documentation is the primary reference.
