# Pine Script v6 Reference — Agent Instructions
> Author: Ugur Pala · mail@ugurpala.com · github.com/trugurpala/pinescriptv6
> TradingView: https://tr.tradingview.com/u/trugurpala/
> X (Twitter): https://x.com/trugurpala

---

## Bu Repo Neden Var? / Why This Repo Exists?

TR: TradingView Pine Script v6 çıktığında tüm AI editörler v5 kodu yazmaya devam etti.
    Claude v5 hatalarını tekrarlıyordu. Cursor `study()` yazıyordu.
    Bu repo AI agent'lara doğru v6 referansı ve kalıcı hata hafızası verir.

EN: When Pine Script v6 launched, all AI editors kept writing v5 code.
    Claude repeated v5 errors. Cursor wrote `study()`.
    This repo gives AI agents correct v6 reference and permanent error memory.

---

## Kullandığını Nasıl Anlarsın? / How to Verify?

✅ Agent LESSONS_LEARNED.md okuduğunu belirtmeli / should mention reading it
✅ //@version=6 ile başlamalı / must start with //@version=6
✅ ta.* kullanmalı / must use ta.*
✅ Hata olunca LESSONS_LEARNED.md'ye eklemeli / must append on error
❌ v5 syntax görüyorsan repo bağlı değil / if v5 syntax, repo not connected

---

## Görev Protokolü / Task Protocol

1. `LESSONS_LEARNED.md` oku — bilinen hatalar
2. `LLM_MANIFEST.md` ile doğru referans dosyasını bul
3. O dosyayı oku
4. `//@version=6` ile başlayan kod yaz
5. Hata olunca: çöz + `LESSONS_LEARNED.md`'ye ekle

---

## Kesin Kurallar / Non-Negotiable Rules

1. `//@version=6` — her scriptin ilk satırı, istisna yok
2. `ta.*` — asla manuel hesaplama
3. `input.int()`, `input.float()` — asla bare `input()`
4. `request.security()` — asla `security()`
5. `indicator()` — asla `study()`
6. Hata çözümünü `LESSONS_LEARNED.md`'ye ekle

---

## Repo İçeriği / What's In This Repo

```
LESSONS_LEARNED.md        — Hata hafızası / Error memory (AI auto-updates)
LLM_MANIFEST.md           — Sorgu yönlendirme / Query routing
reference/                — v6 API referansı / API reference
concepts/                 — Temel kavramlar / Core concepts
examples/indicators/      — 18 indikatör / indicators
examples/strategies/      — 14 strateji / strategies
global-markets/           — 22 global market (ES, NQ, Gold, BTC, ETH, DAX, Nikkei...)
webhook-templates/        — Telegram, Discord, JSON
v5-to-v6-migration/       — v5 → v6 geçiş rehberi / migration guide
```

---

> TR: TradingView resmi Pine Script v6 dokümantasyonu temel referans materyalidir.
> TradingView bu projeyle hiçbir resmi bağlantısı bulunmamaktadır.
>
> EN: TradingView official Pine Script v6 documentation is the primary reference.
> TradingView is not affiliated with this project.

---

## LESSONS_LEARNED Özeti (11 Hata)

1. `ta.stoch()` → tuple değil
2. `math.avg()` → yok
3. `request.security()` tuple syntax
4. Futures komisyon → `cash_per_contract`
5. EMA + hacim filtresi
6. `request.security()` → `[1]` + `lookahead_on`
7. `alertcondition()` → strategy'de `alert()` kullan
8. `barstate.islast` + label → sorunlu
9. Çok satırlı `and` başta → hata
10. `calc_on_every_tick=true` → backtest bozar
11. `barstate.islast` → `barstate.isconfirmed` kullan
