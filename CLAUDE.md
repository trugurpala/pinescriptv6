# Pine Script v6 — AI Geliştirici Rehberi
> Maintainer: Ugur Pala · mail@ugurpala.com
> TradingView: https://tr.tradingview.com/u/trugurpala/
> X (Twitter): https://x.com/trugurpala
> GitHub: https://github.com/trugurpala/pinescriptv6

---

## Bu Projenin Varoluş Nedeni / Why This Exists

TR: TradingView Pine Script v6 çıktığında tüm AI editörler v5 kodu yazmaya devam etti.
Cursor v5 syntax öneriyordu. Copilot `study()` yazıyordu. Claude hata yapıyor, aynı hatayı
tekrarlıyordu. Bu repo bu sorunu çözmek için kuruldu:

1. **AI'ın hafızası yok** — her oturumda sıfırdan başlıyor, aynı hataları yapıyor
2. **v6 referansı dağınık** — TradingView dökümantasyonu büyük, AI context'e sığmıyor
3. **Hiçbir repo tüm AI editörleri desteklemiyor** — Claude, Cursor, Windsurf, Copilot, Cline...

Bu repo şunu yapıyor: **AI'a kalıcı hafıza ve doğru referans veriyor.**

EN: When TradingView Pine Script v6 launched, all AI editors kept writing v5 code.
This repo gives AI permanent memory and correct reference.

---

## Repo İçeriği / Repo Contents (Güncel / Current)

```
examples/indicators/     — 18 indikatör (EMA, RSI, MACD, BB, Supertrend, VWAP, Ichimoku...)
examples/strategies/     — 14 strateji (EMA, MTF, VIOP Session, Fakeout Confirmed, MTF VİOP)
global-markets/          — 22 global market (ES, NQ, Gold, Crude, BTC, ETH, DAX, Nikkei...)
webhook-templates/       — 7 şablon (Telegram, Discord, JSON, VIOP alerts)
v5-to-v6-migration/      — 10 rehber (study, security, input, type system...)
concepts/                — 7 kavram (execution model, MTF, signal quality...)
reference/functions/     — 6 referans (ta, strategy, request, drawing, collections, general)
LESSONS_LEARNED.md       — 11 kayıtlı hata ve çözüm
```

**Toplam:** 56 Pine Script dosyası · 61 Markdown dosyası · 245 commit

---

## TradingView Yayınlanan Scriptler / Published Scripts

| Script | URL |
|--------|-----|
| Fakeout Filter — 4-Layer Signal Quality | https://tr.tradingview.com/script/SY1XkTBH/ |
| VIOP Session Strategy | ⏳ Hazır, yayın bekliyor |
| Fakeout Confirmed Strategy | ⏳ Hazır, yayın bekliyor |

---

## Protokol / Protocol (Her Pine Script Oturumundan Önce / Before Every Session)

**ADIM 1 — Önce oku / Read first:**
1. `LESSONS_LEARNED.md` — 11 kayıtlı hata, TEKRARLAMA
2. `LLM_MANIFEST.md` — göreve uygun referans dosyasını bul
3. İlgili referans dosyasını oku

**ADIM 2 — Kodu yaz / Write code:**
4. `//@version=6` ile başla — istisnasız
5. Kontrol listesini uygula (aşağıda)

**ADIM 3 — Hata oluşursa / On error:**
6. Çöz
7. `LESSONS_LEARNED.md`'ye ekle — format: başlık + hata + sebep + çözüm + kod

---

## Kod Kuralları / Code Rules

```pine
//@version=6   // Her scriptin ilk satırı — istisnasız
```

| ❌ v5 — YAZMA / NEVER | ✅ v6 — YAZ / ALWAYS |
|----------------------|---------------------|
| `study("name")` | `indicator("name")` |
| `security(ticker, tf, expr)` | `request.security(ticker, tf, expr)` |
| `input(14, type=input.integer)` | `input.int(14, "Label")` |
| `array.new_float(0)` | `array.new<float>(0)` |
| `[k, d] = ta.stoch(...)` | `float k = ta.stoch(...)` |
| `math.avg(a, b)` | `(a + b) / 2` |
| `alertcondition()` in strategy | `alert()` in `if` block |
| `barstate.islast` in strategy | `barstate.isconfirmed` |
| `calc_on_every_tick = true` | kaldır — backtest bozar |
| Çok satırlı `and` başta | tek satır veya `and` satır sonunda |

---

## LESSONS_LEARNED Özeti / Error Memory Summary

Detaylar için `LESSONS_LEARNED.md` oku. Kısa liste:

1. `ta.stoch()` → tuple değil, sadece K döner
2. `math.avg()` → yok, `(a+b)/2` kullan
3. `request.security()` tuple → köşeli parantez
4. Futures komisyon → `strategy.commission.cash_per_contract`
5. EMA cross + hacim filtresi → fakeout önler
6. `request.security()` → `[1]` + `lookahead_on` = repainting yok
7. `alertcondition()` → strategy'de çalışmaz, `alert()` kullan
8. `barstate.islast` + label → strategy'de sorunlu
9. Çok satırlı `and` başta → `Mismatched input` hatası
10. `calc_on_every_tick=true` → backtest bozar, uyarı verir
11. `barstate.islast` → strategy'de `barstate.isconfirmed` kullan

---

## Referans Haritası / Reference Map

| İhtiyaç / Need | Dosya / File |
|----------------|-------------|
| RSI, EMA, MACD, ATR, crossover | `reference/functions/ta.md` |
| strategy.entry, exit, position | `reference/functions/strategy.md` |
| plot, line, box, label, table | `reference/functions/drawing.md` |
| request.security, MTF | `reference/functions/request.md` |
| array, map, matrix | `reference/functions/collections.md` |
| math, str, input, alert | `reference/functions/general.md` |
| Sinyal kalitesi / Fakeout | `concepts/signal_quality.md` |
| Bilinen hatalar / Known errors | `concepts/common_errors.md` |
| var, varip, barstate | `concepts/execution_model.md` |
| MTF, repainting, timeframes | `concepts/timeframes.md` |
| **Her zaman önce / Always first** | `LESSONS_LEARNED.md` |

---

## Kontrol Listesi / Checklist (Her koddan önce / Before every code)

- [ ] `LESSONS_LEARNED.md` okundu
- [ ] `//@version=6` mevcut
- [ ] v5 syntax yok (`study`, `security`, `math.avg`, tuple stoch)
- [ ] `alertcondition()` yok → `alert()` kullanıldı
- [ ] `calc_on_every_tick` yok
- [ ] `barstate.isconfirmed` (islast değil)
- [ ] Çok satırlı `and` yok — tek satır
- [ ] `request.security` → `[1]` + `lookahead_on`
- [ ] `var`/`varip` doğru kullanıldı

---

## Cowork Notları / Cowork Notes

Bu repo Anthropic Claude Cowork ile kullanım için optimize edilmiştir.

**Cowork'a bu klasörü verdiğinde Claude şunları yapabilir:**
- Yeni Pine Script v6 stratejisi / indikatörü yaz
- LESSONS_LEARNED.md'yi güncelle
- GitHub'a commit + push yap
- awesome-pinescript-v6 README'yi güncelle
- tradingview-publish/ için description hazırla

**Önerilen ilk görev:**
```
"LESSONS_LEARNED.md ve CLAUDE.md dosyalarını oku.
Sonra [görev tanımı] yap."
```

**Güvenlik:** Hassas bilgi yok. Git token'ları bu repoda saklanmıyor.

---

## Kullandığını Nasıl Anlarsın? / How Do You Know It's Working?

✅ Her Pine Script'ten önce `LESSONS_LEARNED.md` okuduğunu söylüyor
✅ `//@version=6` ile başlıyor — her zaman
✅ `ta.*` kullanıyor — `security()` veya `study()` yazmıyor
✅ Hata alınca: `LESSONS_LEARNED.md`'ye ekliyor

❌ AI v5 syntax yazıyorsa → repo bağlı değil
❌ AI `study()` yazıyorsa → kurallar aktif değil
❌ AI aynı hatayı tekrarlıyorsa → `LESSONS_LEARNED.md` okunmuyor

---

> TradingView Pine Script v6 resmi dokümantasyonu temel referans materyalidir.
> TradingView bu projeyle hiçbir resmi bağlantısı bulunmamaktadır.
> Last updated: Nisan 2026
