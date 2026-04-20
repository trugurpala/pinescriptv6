# CLAUDE.md — Pine Script v6 Proje Rehberi
> **Sahibi / Owner:** Ugur Pala
> **Mail:** mail@ugurpala.com
> **GitHub:** https://github.com/trugurpala
> **TradingView:** https://tr.tradingview.com/u/trugurpala/
> **X (Twitter):** https://x.com/trugurpala
> **Ana Repo:** https://github.com/trugurpala/pinescriptv6
> **Vitrin Repo:** https://github.com/trugurpala/awesome-pinescript-v6
> **Son Güncelleme:** Nisan 2026

---

## Bu Projenin Hikayesi / Project Story

TradingView Pine Script v6 çıktığında tüm AI editörler v5 kodu yazmaya devam etti.
Cursor `study()` yazıyordu. Copilot `security()` yazıyordu. Claude aynı hatayı tekrarlıyordu.

Bu repo şunu çözmek için kuruldu:
- AI'ın v6 için **kalıcı hafızası** olsun
- **Tüm AI editörler** (Cursor, Copilot, Windsurf, Claude, Cline, Zed...) desteklensin
- **Türkiye VİOP / BIST30** futures piyasasına özel örnekler olsun
- Karşılaşılan hatalar `LESSONS_LEARNED.md`'de kalıcı kayıt altına alınsın

---

## Repo İçeriği / Repo Contents

### Pine Script Dosyaları
| Klasör | Adet | İçerik |
|--------|------|--------|
| `examples/indicators/` | 18 | EMA, RSI, MACD, BB, Supertrend, VWAP, Ichimoku, MTF, Fakeout Filter... |
| `examples/strategies/` | 14 | EMA cross, RSI, Supertrend, MTF, VIOP Session, Fakeout Confirmed, MTF VİOP |
| `global-markets/` | 22 | ES, NQ, Gold, Crude, EUR/USD, BTC, ETH, DAX, Nikkei, London Breakout... |
| `webhook-templates/` | 7 | Telegram, Discord, JSON, VİOP alerts |

**Toplam:** 56 `.pine` dosyası · 61 `.md` dosyası · 50 commit

### Referans & Dokümantasyon
```
LESSONS_LEARNED.md          — 11 kayıtlı hata ve çözüm (AI hafızası)
reference/functions/ta.md   — ta.* fonksiyonları
reference/functions/strategy.md
reference/functions/request.md
reference/functions/drawing.md
reference/functions/collections.md
reference/functions/general.md
concepts/execution_model.md
concepts/timeframes.md
concepts/signal_quality.md
v5-to-v6-migration/         — 10 rehber (study→indicator, security→request.security...)
```

### AI Editor Konfigürasyonları (9/9)
```
.cursorrules                     — Cursor
.cursor/rules/                   — Cursor Rules
.github/copilot-instructions.md  — GitHub Copilot
.windsurfrules                   — Windsurf
.clinerules                      — Cline
.zed/                            — Zed
CLAUDE.md (bu dosya)             — Claude / Cowork
AGENTS.md                        — Tüm AI agent'lar
LLM_MANIFEST.md                  — Sorgu yönlendirme
```

---

## TradingView Yayın Durumu / Published Scripts

| # | Script | Durum | URL |
|---|--------|-------|-----|
| 1 | Fakeout Filter — 4-Layer Signal Quality | ✅ Yayında | https://tr.tradingview.com/script/SY1XkTBH/ |
| 2 | VİOP Session Strategy | ⏳ Hazır, yayın bekliyor | `examples/strategies/11_viop_session_strategy.pine` |
| 3 | Fakeout Confirmed Strategy | ⏳ Hazır, yayın bekliyor | `examples/strategies/13_fakeout_confirmed_strategy.pine` |

---

## Önemli Stratejiler / Key Strategies

### 11 — VİOP Session Strategy
- **Sembol:** BIST:XU030D1! (VİOP futures)
- **TF:** 5dk, 15dk, 1sa
- **Özellik:** 09:30-18:15 UTC+3 seans filtresi, gün sonu otomatik kapanış
- **Komisyon:** `cash_per_contract` (VİOP için doğru)

### 13 — Fakeout Confirmed Strategy
- **Sembol:** ES, NQ, BTC, XAUUSD
- **TF:** 15dk, 1sa, 4sa
- **Özellik:** 4 katmanlı filtre (Hacim + HTF + Bar Onayı + ATR), filtre tablosu

### 14 — MTF VİOP Strategy (YENİ)
- **Sembol:** BIST:XU030D1!
- **Chart TF:** 1dk (entry)
- **Trend TF:** 5dk (input ile seçilebilir)
- **Özellik:** EMA + Supertrend trend yönü, EMA cross entry, VİOP seans filtresi

---

## LESSONS_LEARNED — 11 Kayıtlı Hata

**Bu dosyayı her Pine Script yazmadan önce oku: `LESSONS_LEARNED.md`**

| # | Hata | Çözüm |
|---|------|-------|
| 1 | `ta.stoch()` tuple döndürüyor sanmak | `float k = ta.stoch(...)` — sadece K döner |
| 2 | `math.avg(a, b)` kullanmak | `(a + b) / 2` |
| 3 | `request.security()` tuple syntax yanlış | Köşeli parantez zorunlu |
| 4 | Futures komisyon yanlış tip | `strategy.commission.cash_per_contract` |
| 5 | EMA cross + hacim filtresi yok | Fakeout önlemek için hacim şart |
| 6 | `request.security()` repainting | `[1]` + `lookahead_on` kullan |
| 7 | `alertcondition()` strategy'de | `alert()` kullan, `if` bloğu içinde |
| 8 | `barstate.islast` + label strategy'de | Label kaldır veya `barstate.isconfirmed` |
| 9 | Çok satırlı `and` başta | Tek satır veya `and` satır sonunda |
| 10 | `calc_on_every_tick=true` | Kaldır — backtest bozar, uyarı verir |
| 11 | `barstate.islast` strategy'de | `barstate.isconfirmed` kullan |

---

## Protokol / Protocol

### Her Pine Script yazmadan önce / Before every Pine Script:
1. `LESSONS_LEARNED.md` oku — bilinen 11 hatayı tekrarlama
2. İlgili referans dosyasını oku (`LLM_MANIFEST.md`'den bul)
3. Kodu yaz — `//@version=6` ile başla
4. Hata alınca: çöz + `LESSONS_LEARNED.md`'ye ekle

### Kontrol Listesi / Checklist:
- [ ] `//@version=6` — ilk satır, istisnasız
- [ ] `calc_on_every_tick` yok
- [ ] `alertcondition()` yok → `alert()` kullanıldı
- [ ] `barstate.isconfirmed` (islast değil)
- [ ] Çok satırlı `and` yok — tek satır
- [ ] `request.security()` → `[1]` + `lookahead_on`
- [ ] `ta.*` kullanıldı — manuel hesaplama yok
- [ ] `study()` yok → `indicator()`
- [ ] `security()` yok → `request.security()`

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
| `alertcondition()` in strategy | `if signal \n    alert(...)` |
| `barstate.islast` in strategy | `barstate.isconfirmed` |
| `calc_on_every_tick = true` | kaldır |
| Çok satırlı `and` başta | tek satır |

---

## Referans Haritası / Reference Map

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
| Sinyal kalitesi, fakeout | `concepts/signal_quality.md` |
| **Her zaman önce** | `LESSONS_LEARNED.md` |

---

## GitHub Workflow

```bash
# Commit ve push
cd /path/to/pinescriptv6
git add .
git commit -m "feat/fix/docs: açıklama"


```

### Commit Formatı:
- `feat:` — yeni özellik / new feature
- `fix:` — hata düzeltme / bug fix
- `docs:` — dokümantasyon / documentation
- `lessons:` — LESSONS_LEARNED güncelleme

---

## Sıradaki Adımlar / Next Steps

- [ ] Script 2 (VİOP Session) TradingView'da publish et
- [ ] Script 3 (Fakeout Confirmed) TradingView'da publish et
- [ ] awesome-pinescript-v6 README'sindeki 9 adet ⏳ → ✅ güncelle (URL bekleniyor)
- [ ] X/Twitter thread: "AI v5 yazıyordu, çözdüm" hikayesi
- [ ] Reddit r/algotrading + r/TradingView post

---

## Cowork Görev Örnekleri / Cowork Task Examples

```
"LESSONS_LEARNED.md oku, sonra XU030 için yeni bir momentum stratejisi yaz,
 examples/strategies/ klasörüne ekle ve push et."

"awesome-pinescript-v6 README.md'deki tüm ⏳ işaretlerini kontrol et,
 hangilerini güncelleyebiliriz?"

"tradingview-publish/02_viop_session_description.md dosyasını oku,
 TradingView publish için hazır mı kontrol et."
```

---

> TradingView Pine Script v6 resmi dokümantasyonu temel referans materyalidir.
> TradingView bu projeyle hiçbir resmi bağlantısı bulunmamaktadır.
