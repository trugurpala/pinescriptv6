# Changelog — trugurpala/pinescriptv6

---

## [Unreleased] — Bekleyenler

- TradingView Script 2 publish: VIOP Session Strategy
- TradingView Script 3 publish: Fakeout Confirmed Strategy
- awesome-pinescript-v6 README güncellemesi (9 ⏳ → ✅)
- X/Twitter kampanya thread'i
- Reddit r/algotrading + r/TradingView post
- Webhook → otomatik emir gönderimi (otomasyon)

---

## [2.0.0] — Nisan 2026

### Eklenenler
- `examples/strategies/14_mtf_viop_strategy.pine` — 5dk trend + 1dk entry MTF stratejisi
- `examples/strategies/13_fakeout_confirmed_strategy.pine` — 4 filtre katmanlı strateji
- `examples/strategies/11_viop_session_strategy.pine` — VİOP seans bazlı strateji
- `examples/strategies/12_chandelier_strategy.pine` — Chandelier Exit stratejisi
- `examples/indicators/18_fakeout_filter.pine` — **TradingView'da yayınlandı** ✅
- `global-markets/` — 22 global market stratejisi (ES, NQ, Gold, BTC, ETH, DAX, Nikkei...)
- `tradingview-publish/` — yayın açıklamaları ve URL'ler
- AI editor konfigürasyonları: 9 adet (.cursorrules, copilot-instructions, .windsurfrules, .zed, CLAUDE.md, AGENTS.md, LLM_MANIFEST.md, .clinerules, .cursor/rules/)
- GitHub Community Standards %100: Issue templates (3 YML), PR template, FUNDING, CITATION, CODE_OF_CONDUCT, SECURITY, CONTRIBUTING
- Social Preview görseli her iki repoya yüklendi
- `awesome-pinescript-v6` vitrin repo kuruldu (CC0, Discussions, Community %100)
- LESSONS_LEARNED.md — 11 kayıtlı hata ve çözüm

### Düzeltmeler (LESSONS_LEARNED kayıtlı)
- `alertcondition()` → `alert()` (strategy içinde çalışmaz)
- `barstate.islast` → `barstate.isconfirmed` (strategy uyarısı)
- `calc_on_every_tick=true` kaldırıldı (backtest bozuyor)
- Çok satırlı `and` → tek satır (Mismatched input hatası)

---

## [1.0.0] — 2025

### Eklenenler
- Pine Script v6 referansı sıfırdan kuruldu — Ugur Pala
- `LESSONS_LEARNED.md` — AI hata hafızası sistemi
- `SKILL.md` — AI yazma protokolü
- `LLM_MANIFEST.md` — sorgu yönlendirme haritası
- `examples/indicators/` — 18 indikatör
- `examples/strategies/` — ilk 10 strateji
- `v5-to-v6-migration/` — 10 rehber
- `concepts/` — 7 kavram dosyası
- `reference/functions/` — 6 referans dosyası
- `webhook-templates/` — 7 şablon
- MIT License
