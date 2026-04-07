# CLAUDE.md — Proje Hafızası / Project Memory
> Maintainer: Ugur Pala · mail@ugurpala.com
> TradingView: https://tr.tradingview.com/u/trugurpala/
> X (Twitter): https://x.com/trugurpala
> GitHub: github.com/trugurpala | github.com/trugurpala/pinescriptv6
> Repo 2: github.com/trugurpala/awesome-pinescript-v6

---

## KİM / WHO

**Ugur Pala** — Algo trader, Pine Script v6 geliştirici.
Türkiye VİOP (BIST30/XU030 index futures) piyasasına odaklı.
Python, data pipeline, web dashboard geliştirme deneyimi var.
Hedef: TradingView alert → otomatik emir gönderimi (webhook tabanlı).

---

## PROJE NEDİR / WHAT IS THIS PROJECT

Bu repo iki amaca hizmet eder:

1. **AI Hafızası** — Claude, Cursor, Copilot, Windsurf gibi AI editörler Pine Script v6 çıktığında
   hâlâ v5 kodu yazıyordu. Bu repo onlara doğru referans ve kalıcı hata hafızası verir.

2. **VİOP Algo Trading** — Türkiye vadeli işlem piyasası (VIOP) için Pine Script v6 stratejileri,
   backtest şablonları ve webhook alert sistemi.

---

## İKİ REPO / TWO REPOS

### 1. trugurpala/pinescriptv6 (Ana Repo)
- **245 commit**, MIT License
- 56 Pine Script dosyası, 61 Markdown dosyası
- AI editor konfigürasyonları: 9 adet (Cursor, Copilot, Windsurf, Zed, Cline, Claude, vb.)
- GitHub Community Standards: %100

### 2. trugurpala/awesome-pinescript-v6 (Vitrin Repo)
- CC0 License, Discussions açık
- Rakip analizi dahil kuratoryal liste
- Community Health: %100

---

## VİOP TEKNIK DETAYLAR / VIOP SPECS

Bunları her strateji yazarken kullan:

```pine
// VİOP F_XU030 — Borsa İstanbul index futures
strategy("...",
    commission_type  = strategy.commission.cash_per_contract,
    commission_value = 2.0,        // TL per contract per side
    slippage         = 2,
    initial_capital  = 100000,
    default_qty_type = strategy.fixed,
    default_qty_value = 1)

// Seans filtresi — zorunlu
bool inSession = not na(time(timeframe.period, "0930-1815", "UTC+3"))

// Seans kapanışında kapat
if not inSession and inSession[1]
    strategy.close_all(comment="Seans sonu")
```

- **Sembol:** `BIST:XU030D1!` veya `F_XU030`
- **Seans:** 09:30–18:15 UTC+3
- **Uzlaşma:** Nakdi (cash settlement)
- **Vergi:** Index kontratlarında %0 stopaj
- **Lot:** endeks/1000 × 100
- **Komisyon:** 0.03% veya 2 TL/kontrat (cash_per_contract)
- **Önerilen TF:** 5dk, 15dk, 1sa

---

## REPO İÇERİĞİ / REPO CONTENTS

```
examples/indicators/     18 dosya  — EMA, RSI, MACD, BB, Supertrend, VWAP,
                                      Ichimoku, MTF, Fakeout Filter...
examples/strategies/     14 dosya  — 01-10 temel, 11 VIOP Session,
                                      12 Chandelier, 13 Fakeout Confirmed,
                                      14 MTF VIOP (5dk trend + 1dk entry)
global-markets/          22 dosya  — ES, NQ, Gold, Crude, EUR/USD, GBP/USD,
                                      USD/JPY, BTC, ETH, DAX, Nikkei...
webhook-templates/        7 dosya  — Telegram, Discord, JSON, VIOP alerts
v5-to-v6-migration/      10 dosya  — study, security, input, type system...
concepts/                 7 dosya  — execution model, MTF, signal quality...
reference/functions/      6 dosya  — ta, strategy, request, drawing,
                                      collections, general
LESSONS_LEARNED.md       240 satır — 11 kayıtlı hata
tradingview-publish/      4 dosya  — yayın açıklamaları ve URL'ler
```

---

## TRADİNGVİEW YAYINLARI / TRADINGVIEW PUBLISHED

| # | Script | Durum | URL |
|---|--------|-------|-----|
| 1 | Fakeout Filter — 4-Layer Signal Quality | ✅ Yayında | https://tr.tradingview.com/script/SY1XkTBH/ |
| 2 | VIOP Session Strategy | ⏳ Hazır, bekliyor | `examples/strategies/11_viop_session_strategy.pine` |
| 3 | Fakeout Confirmed Strategy | ⏳ Hazır, bekliyor | `examples/strategies/13_fakeout_confirmed_strategy.pine` |

---

## SIRADAM / NEXT STEPS

Öncelik sırasıyla:

1. **TradingView Script 2 publish** — VIOP Session Strategy
   - Description: `tradingview-publish/02_viop_session_description.md`
   - Tags: `viop, bist30, turkey, session, strategy, atr, ema, pinescriptv6`

2. **TradingView Script 3 publish** — Fakeout Confirmed Strategy
   - Description: `tradingview-publish/03_fakeout_confirmed_strategy_description.md`
   - Tags: `pinescriptv6, fakeout, strategy, volume, htf, atr, filter, signal`

3. **URL güncelleme** — Publish sonrası:
   - `pinescriptv6` README
   - `awesome-pinescript-v6` README (9 adet ⏳ → ✅)
   - `tradingview-publish/` dosyaları

4. **X/Twitter kampanyası** — "AI v5 yazıyordu, çözdüm" thread
5. **Reddit** — r/algotrading + r/TradingView post
6. **Webhook → otomasyon** — TradingView alert → otomatik emir gönderimi

---

## LESSONS_LEARNED ÖZETİ / ERROR MEMORY (11 Hata)

Detay için `LESSONS_LEARNED.md` oku. Hızlı referans:

| # | Hata | Çözüm |
|---|------|-------|
| 1 | `ta.stoch()` tuple döndürmez | `float k = ta.stoch(...)` |
| 2 | `math.avg()` yok | `(a + b) / 2` |
| 3 | `request.security()` tuple syntax | köşeli parantez `[a, b]` |
| 4 | Futures komisyon | `strategy.commission.cash_per_contract` |
| 5 | EMA cross + hacim yok = fakeout | hacim filtresi ekle |
| 6 | Repainting | `[1]` + `lookahead_on` |
| 7 | `alertcondition()` strategy'de çalışmaz | `alert()` kullan |
| 8 | `barstate.islast` + label strategy'de | `barstate.isconfirmed` kullan |
| 9 | Çok satırlı `and` başta | tek satır veya `and` satır sonunda |
| 10 | `calc_on_every_tick=true` | kaldır — backtest bozar |
| 11 | `barstate.islast` strategy'de uyarı | `barstate.isconfirmed` kullan |

---

## KOD KURALLARI / CODE RULES

```pine
//@version=6   // Her scriptin ilk satırı — istisnasız
```

| ❌ YAZMA | ✅ YAZ |
|---------|--------|
| `study("name")` | `indicator("name")` |
| `security(ticker, tf, expr)` | `request.security(ticker, tf, expr)` |
| `[k, d] = ta.stoch(...)` | `float k = ta.stoch(...)` |
| `math.avg(a, b)` | `(a + b) / 2` |
| `alertcondition()` strategy'de | `alert()` if bloğu içinde |
| `barstate.islast` strategy'de | `barstate.isconfirmed` |
| `calc_on_every_tick = true` | kaldır |
| Çok satırlı `and` başta | tek satır |

---

## PROTOKOL / PROTOCOL

**Pine Script yazmadan önce MUTLAKA:**
1. `LESSONS_LEARNED.md` oku — 11 hata var, tekrarlama
2. `LLM_MANIFEST.md` ile doğru referans dosyasını bul
3. O referans dosyasını oku
4. Kodu yaz — `//@version=6` ile başla
5. Hata olursa: çöz + `LESSONS_LEARNED.md`'ye ekle

**Kontrol listesi:**
- [ ] `//@version=6` var
- [ ] `LESSONS_LEARNED.md` okundu
- [ ] `alertcondition()` yok
- [ ] `calc_on_every_tick` yok
- [ ] `barstate.isconfirmed` (islast değil)
- [ ] Çok satırlı `and` yok
- [ ] `request.security` → `[1]` + `lookahead_on`

---

## REFERANS HARİTASI / REFERENCE MAP

| İhtiyaç | Dosya |
|---------|-------|
| RSI, EMA, MACD, ATR, crossover | `reference/functions/ta.md` |
| strategy.entry, exit, position | `reference/functions/strategy.md` |
| plot, line, box, label, table | `reference/functions/drawing.md` |
| request.security, MTF | `reference/functions/request.md` |
| array, map, matrix | `reference/functions/collections.md` |
| math, str, input, alert | `reference/functions/general.md` |
| var, varip, barstate | `concepts/execution_model.md` |
| MTF, repainting | `concepts/timeframes.md` |
| Fakeout, sinyal kalitesi | `concepts/signal_quality.md` |
| **Her zaman önce** | `LESSONS_LEARNED.md` |

---

> Son güncelleme: Nisan 2026
> TradingView bu projeyle resmi bağlantısı yoktur.
