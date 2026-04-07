---
name: pinescript-v6
description: "Pine Script v6 uzman geliştirici skill'i — doğru v6 kodu yazar, hataları takip eder, LESSONS_LEARNED'i günceller."
maintainer: Ugur Pala · mail@ugurpala.com
repo: github.com/trugurpala/pinescriptv6
tradingview: https://tr.tradingview.com/u/trugurpala/
triggers:
  - Pine Script
  - PineScript
  - indicator
  - strategy
  - TradingView
  - indikatör
  - strateji
  - v6
  - pine
  - VIOP
  - VİOP
  - BIST30
---

# Pine Script v6 — Skill

## Proje Bağlamı / Project Context

Bu skill **trugurpala/pinescriptv6** reposuna aittir.
- **Sahibi:** Ugur Pala · mail@ugurpala.com
- **GitHub:** github.com/trugurpala
- **TradingView:** https://tr.tradingview.com/u/trugurpala/
- **Vitrin:** github.com/trugurpala/awesome-pinescript-v6
- **Hedef:** Türkiye VİOP / BIST30 futures + global piyasalar için Pine Script v6
- **İçerik:** 56 Pine dosyası · 14 strateji · 18 indikatör · 22 global market · 245 commit

---

## Görev

Pine Script v6 ile doğru, optimize edilmiş kod yaz.
Kod yazmadan önce LESSONS_LEARNED.md ve referansları oku.
Hata çözümlerini hemen LESSONS_LEARNED.md'ye kaydet.

---

## Protokol

### 1. Kod Yazmadan Önce
1. **`LESSONS_LEARNED.md` oku** — 11 bilinen hata var, tekrarlama
2. **`LLM_MANIFEST.md`** ile göreve uygun referans dosyasını bul ve oku

### 2. Kod Kuralları
- `//@version=6` — her scriptin ilk satırı, istisnasız
- `ta.*` kullan — manuel hesaplama yazma
- `var` / `varip` — execution model'e göre doğru kullan
- Referansta olmayan fonksiyon adı uydurma

### 3. Hata Olduğunda
- Hatayı çöz
- `LESSONS_LEARNED.md`'ye hemen ekle: başlık + hata + sebep + çözüm + kod örneği

---

## LESSONS_LEARNED Özeti (11 Hata — Detay için dosyayı oku)

| # | Hata | Çözüm |
|---|------|-------|
| 1 | `ta.stoch()` tuple döndürüyor sanmak | `float k = ta.stoch(...)` |
| 2 | `math.avg(a, b)` kullanmak | `(a + b) / 2` |
| 3 | `request.security()` tuple syntax yanlış | Köşeli parantez zorunlu |
| 4 | Futures komisyon tipi yanlış | `strategy.commission.cash_per_contract` |
| 5 | EMA cross + hacim filtresi yok | Fakeout önlemek için şart |
| 6 | `request.security()` repainting | `[1]` + `lookahead_on` kullan |
| 7 | `alertcondition()` strategy'de | `alert()` kullan, `if` bloğu içinde |
| 8 | `barstate.islast` + label strategy'de | `barstate.isconfirmed` kullan |
| 9 | Çok satırlı `and` başta | Tek satır veya `and` satır sonunda |
| 10 | `calc_on_every_tick=true` | Kaldır — backtest bozar, uyarı verir |
| 11 | `barstate.islast` strategy'de | `barstate.isconfirmed` kullan |

---

## v5 → v6 Dönüşüm Tablosu

| ❌ v5 — YAZMA | ✅ v6 — YAZ |
|--------------|------------|
| `study("name")` | `indicator("name")` |
| `security(ticker, tf, expr)` | `request.security(ticker, tf, expr)` |
| `input(14, type=input.integer)` | `input.int(14, "Label")` |
| `array.new_float(0)` | `array.new<float>(0)` |
| `[k, d] = ta.stoch(...)` | `float k = ta.stoch(...)` |
| `math.avg(a, b)` | `(a + b) / 2` |
| `alertcondition()` strategy'de | `if signal\n    alert(...)` |
| `barstate.islast` strategy'de | `barstate.isconfirmed` |
| `calc_on_every_tick = true` | kaldır |
| Çok satırlı `and` başta | tek satır |

---

## VİOP / BIST30 Şablonu

VİOP stratejisi yazarken bu template'i kullan:

```pine
//@version=6
strategy("VİOP Strategy [trugurpala]",
    overlay              = true,
    initial_capital      = 100000,
    default_qty_type     = strategy.fixed,
    default_qty_value    = 1,
    commission_type      = strategy.commission.cash_per_contract,
    commission_value     = 2.0,
    slippage             = 2)

// Seans: 09:30-18:15 UTC+3
bool inSession = not na(time(timeframe.period, "0930-1815", "UTC+3"))

// Seans kapanışında kapat
if not inSession and inSession[1]
    strategy.close_all(comment="Seans sonu")
```

- **Sembol:** `BIST:XU030D1!` veya `F_XU030`
- **Seans:** 09:30–18:15 UTC+3
- **Komisyon:** 2 TL/kontrat (cash_per_contract)
- **Önerilen TF:** 5dk, 15dk, 1sa

---

## Referans Haritası

| İhtiyaç | Dosya |
|---------|-------|
| RSI, EMA, MACD, ATR, crossover, pivot | `reference/functions/ta.md` |
| strategy.entry, exit, close, position | `reference/functions/strategy.md` |
| plot, line, box, label, table | `reference/functions/drawing.md` |
| request.security, MTF | `reference/functions/request.md` |
| array, map, matrix | `reference/functions/collections.md` |
| math, str, input, alert | `reference/functions/general.md` |
| open, close, bar_index, syminfo | `reference/variables.md` |
| color.red, shape.*, style.* | `reference/constants.md` |
| int, float, series, simple | `reference/types.md` |
| if, for, var, varip, switch | `reference/keywords.md` |
| barstate, var, history, realtime | `concepts/execution_model.md` |
| Repainting, HTF, MTF | `concepts/timeframes.md` |
| color.new, gradient | `concepts/colors_and_display.md` |
| Fakeout, sinyal kalitesi | `concepts/signal_quality.md` |
| Bilinen hatalar | `concepts/common_errors.md` |
| **Her zaman önce** | `LESSONS_LEARNED.md` |

---

## Kontrol Listesi

- [ ] `LESSONS_LEARNED.md` okundu (11 hata)
- [ ] `//@version=6` — ilk satır
- [ ] `alertcondition()` yok → `alert()` kullanıldı
- [ ] `calc_on_every_tick` yok
- [ ] `barstate.isconfirmed` (islast değil)
- [ ] Çok satırlı `and` yok — tek satır
- [ ] `request.security()` → `[1]` + `lookahead_on`
- [ ] `ta.*` kullanıldı — manuel hesaplama yok
- [ ] `study()` yok → `indicator()`
- [ ] `security()` yok → `request.security()`
