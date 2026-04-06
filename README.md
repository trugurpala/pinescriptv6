# Pine Script v6 Reference

<div align="center">

![Pine Script v6](https://img.shields.io/badge/Pine%20Script-v6-1E88E5?style=for-the-badge&logo=tradingview&logoColor=white)
![TradingView](https://img.shields.io/badge/TradingView-Compatible-131722?style=for-the-badge&logo=tradingview)
![MIT License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)
![Author](https://img.shields.io/badge/Author-Ugur%20Pala-F59E0B?style=for-the-badge)
![Stars](https://img.shields.io/github/stars/trugurpala/pinescriptv6?style=for-the-badge&color=yellow)
![TR | EN](https://img.shields.io/badge/TR%20%7C%20EN-Bilingual-8B5CF6?style=for-the-badge)

**TradingView Pine Script v6 için AI destekli, hata hafızalı geliştirme ortamı.**
**AI-powered Pine Script v6 development environment with error memory.**

[Ugur Pala](https://github.com/trugurpala) · [TradingView](https://tr.tradingview.com/u/trugurpala/) · [X / Twitter](https://x.com/trugurpala) · mail@ugurpala.com

[Demo](#-demo) · [Neden / Why](#-neden-var--why-this-exists) · [Claude](#-claude--claude-code) · [Cursor](#️-cursor) · [Windsurf](#-windsurf) · [Copilot](#-github-copilot) · [Cline/Roo](#-cline--roo--aider) · [Örnekler](#-örnekler--examples) · [Global Markets](#-global-markets-22) · [Webhook](#-webhook-templates-7) · [v5→v6](#-v5--v6-migration-10) · [Yapı](#-dosya-yapısı--file-structure)

</div>

---

## 📺 Demo

> TR: Aşağıdaki indikatör, bu repodaki referanslar kullanılarak Claude ile yazıldı.
> EN: The indicator below was written by Claude using the reference files in this repo.

![EMA Cross on XU030](assets/demo_chart.png)

```pine
//@version=6
indicator("EMA Cross", overlay=true)
fast = ta.ema(close, 9)
slow = ta.ema(close, 21)
plot(fast, "EMA 9",  color.green, 2)
plot(slow, "EMA 21", color.red,   2)
bgcolor(ta.crossover(fast, slow)  ? color.new(color.green, 90) :
        ta.crossunder(fast, slow) ? color.new(color.red,   90) : na)
```

---

## ⚙️ Nasıl Çalışır / How It Works

![System Flow](assets/lessons_flow.png)

| Adım / Step | TR | EN |
|---|---|---|
| 1 | Kodu yazmadan önce `LESSONS_LEARNED.md` okunur | Read `LESSONS_LEARNED.md` before writing |
| 2 | `LLM_MANIFEST.md` ile doğru referans dosyası bulunur | Find the right file via `LLM_MANIFEST.md` |
| 3 | Temiz, v6 uyumlu kod yazılır | Write clean, v6-compliant code |
| 4 | Hata oluşursa çözülür ve **otomatik kaydedilir** | On error: solved and **auto-saved** |
| 5 | Sonraki oturumda aynı hata bir daha yapılmaz | Same mistake never repeated next session |

---

## 💡 Neden Var / Why This Exists

> TR: Pine Script v6 çıktığında AI editörler v5 yazmaya devam etti. Bu repo o sorunu çözdü.
> EN: When Pine Script v6 launched, AI editors kept writing v5. This repo fixed that.

### TR | Türkçe

TradingView Pine Script v6'yı yayınladığında **tüm AI editörler v5 kodu yazmaya devam etti.**

- Cursor `study()` öneriyordu — v6'da yok
- Copilot `security()` yazıyordu — v6'da `request.security()` oldu
- Claude aynı hataları tekrarlıyordu — çünkü hafızası yoktu
- Her yeni oturumda sıfırdan başlanıyordu

Bu repo üç şeyi çözüyor:

| Sorun | Çözüm |
|-------|-------|
| AI'ın hafızası yok | `LESSONS_LEARNED.md` — çözülen hatalar kalıcı saklanır |
| v6 referansı büyük | `LLM_MANIFEST.md` — AI sadece gerekli dosyayı okur |
| Tek editör desteği | 9 AI editör — Claude, Cursor, Windsurf, Copilot, Cline, Roo, Aider, Zed, Devin |

### EN | English

When TradingView launched Pine Script v6, **all AI editors kept writing v5 code.**

- Cursor suggested `study()` — doesn't exist in v6
- Copilot wrote `security()` — became `request.security()` in v6
- Claude repeated the same errors — because it had no memory
- Every new session started from zero

This repo solves three things:

| Problem | Solution |
|---------|---------|
| AI has no memory | `LESSONS_LEARNED.md` — solved errors stored permanently |
| v6 reference is large | `LLM_MANIFEST.md` — AI reads only the needed file |
| Single editor support | 9 AI editors — Claude, Cursor, Windsurf, Copilot, Cline, Roo, Aider, Zed, Devin |

### Kullandığını Nasıl Anlarsın? / How Do You Know It's Working?

| ✅ Çalışıyor / Working | ❌ Çalışmıyor / Not Working |
|------------------------|---------------------------|
| AI "LESSONS_LEARNED.md okudum" diyor | AI bunu söylemiyor |
| Kod `//@version=6` ile başlıyor | `study()` veya `security()` görüyorsun |
| `ta.*` fonksiyonları kullanılıyor | Aynı hata tekrarlanıyor |
| Hata olunca LESSONS_LEARNED güncelleniyor | AI hata geçmişini bilmiyor |

---

## 🚀 Hızlı Başlangıç / Quick Start

```bash
git clone https://github.com/trugurpala/pinescriptv6.git
```

---

## 🤖 Claude / Claude Code

> TR: Claude Projects ve Claude Code ile entegrasyon — en tam deneyim için önerilen yöntem.
> EN: Integration with Claude Projects and Claude Code — recommended for the fullest experience.

**Claude Projects — TR:**
[claude.ai/projects](https://claude.ai/projects) → projenizi açın → **Files** → **+** → **GitHub**
```
https://github.com/trugurpala/pinescriptv6
```
Tüm dosyaları seçin → **Add files** → proje sohbetinde: `/pinescript-v6`

**Claude Code — TR:**
```bash
git clone https://github.com/trugurpala/pinescriptv6.git
cd pinescriptv6
claude
```
`CLAUDE.md` otomatik okunur. Claude artık Pine Script v6 kurallarını ve hata hafızasını biliyor.

---

**Claude Projects — EN:**
[claude.ai/projects](https://claude.ai/projects) → open your project → **Files** → **+** → **GitHub**
```
https://github.com/trugurpala/pinescriptv6
```
Select all files → **Add files** → in project chat: `/pinescript-v6`

**Claude Code — EN:**
```bash
git clone https://github.com/trugurpala/pinescriptv6.git
cd pinescriptv6
claude
```
`CLAUDE.md` is read automatically. Claude now knows Pine Script v6 rules and the error memory system.

---

## ⌨️ Cursor

> TR: Cursor v0.44+ için `.cursor/rules/pinescriptv6.mdc` otomatik yüklenir. Eski sürümler `.cursorrules` kullanır.
> EN: `.cursor/rules/pinescriptv6.mdc` loads for Cursor v0.44+. `.cursorrules` for older versions.

```bash
git clone https://github.com/trugurpala/pinescriptv6.git
cd pinescriptv6
cursor .
```

**TR** — Chat'te kullan:
```
@LESSONS_LEARNED.md EMA cross stratejisi yaz, XU030 için
@reference/functions/ta.md RSI divergence indikatörü yaz
@concepts/common_errors.md Bu hatanın sebebi ne?
```

**EN** — Use in chat:
```
@LESSONS_LEARNED.md write an EMA cross strategy for XU030
@reference/functions/ta.md write an RSI divergence indicator
@concepts/common_errors.md what causes this error?
```

---

## 🌊 Windsurf

> TR: `.windsurfrules` dosyası Windsurf / Cascade tarafından otomatik okunur.
> EN: `.windsurfrules` is picked up automatically by Windsurf / Cascade.

```bash
git clone https://github.com/trugurpala/pinescriptv6.git
cd pinescriptv6
windsurf .
```

**TR** — Cascade chat'te kullan:
```
@LESSONS_LEARNED.md Supertrend stratejisi yaz
@reference/functions/strategy.md ATR tabanlı SL/TP nasıl yazılır?
```

**EN** — Use in Cascade:
```
@LESSONS_LEARNED.md write a Supertrend strategy
@reference/functions/strategy.md how to write ATR-based SL/TP?
```

---

## 🐙 GitHub Copilot

> TR: `.github/copilot-instructions.md` VS Code, JetBrains ve Copilot destekli editörlerde otomatik devreye girer.
> EN: `.github/copilot-instructions.md` activates automatically in VS Code, JetBrains, and any Copilot-enabled editor.

```bash
git clone https://github.com/trugurpala/pinescriptv6.git
code pinescriptv6
```

**TR** — Copilot Chat'te kullan:
```
LESSONS_LEARNED.md dosyasını kontrol et, sonra bir RSI mean reversion stratejisi yaz.
reference/functions/ta.md dosyasına göre ta.pivothigh() imzası nedir?
```

**EN** — Use in Copilot Chat:
```
Check LESSONS_LEARNED.md, then write an RSI mean reversion strategy.
According to reference/functions/ta.md, what is the ta.pivothigh() signature?
```

---

## 🔧 Cline / Roo / Aider

> TR: `.clinerules` dosyası Cline, Roo, Continue ve Aider tarafından otomatik okunur.
> EN: `.clinerules` is read automatically by Cline, Roo, Continue, and Aider.

```bash
git clone https://github.com/trugurpala/pinescriptv6.git
cd pinescriptv6
# Cline, Roo veya Aider ile aç / Open with Cline, Roo, or Aider
```

`.clinerules` otomatik yüklenir / loads automatically.

---

## 🤗 Custom GPT / Diğer LLM'ler / Other LLMs

ZIP: [main.zip](https://github.com/trugurpala/pinescriptv6/archive/refs/heads/main.zip)

Yükle / Upload: `LESSONS_LEARNED.md` + `LLM_MANIFEST.md` + `reference/functions/`

**TR sistem promptu:**
```
Bu proje Pine Script v6 geliştirme için optimize edilmiş bir bilgi tabanıdır.
Kod yazmadan önce her zaman LESSONS_LEARNED.md içeriğini kontrol et.
Hangi dosyayı okuyacağını belirlemek için LLM_MANIFEST.md'ye başvur.
Tüm scriptler //@version=6 ile başlamalıdır.
```

**EN system prompt:**
```
This project is a knowledge base optimised for Pine Script v6 development.
Always check LESSONS_LEARNED.md before writing any code.
Consult LLM_MANIFEST.md to determine which file to read for each task.
All scripts must start with //@version=6.
```

---

## 📦 Örnekler / Examples

TR: **55+ hazır Pine Script v6 örneği** — copy-paste hazır, TradingView'da test edilmiş.
EN: **55+ ready-to-use Pine Script v6 examples** — copy-paste ready, tested in TradingView.

### 📊 İndikatörler / Indicators (18)

| # | Dosya | Açıklama / Description |
|---|-------|------------------------|
| 01 | [`01_ema_cross.pine`](examples/indicators/01_ema_cross.pine) | EMA 9/21 Cross + bgcolor + alerts |
| 02 | [`02_rsi_ob_os.pine`](examples/indicators/02_rsi_ob_os.pine) | RSI 14 Gradient — OB/OS zones |
| 03 | [`03_macd_histogram.pine`](examples/indicators/03_macd_histogram.pine) | MACD 12/26/9 — colored histogram |
| 04 | [`04_bollinger_bands.pine`](examples/indicators/04_bollinger_bands.pine) | Bollinger Bands + squeeze |
| 05 | [`05_supertrend.pine`](examples/indicators/05_supertrend.pine) | Supertrend ATR-based |
| 06 | [`06_vwap_session.pine`](examples/indicators/06_vwap_session.pine) | VWAP + StDev bands |
| 07 | [`07_atr_levels.pine`](examples/indicators/07_atr_levels.pine) | ATR dynamic S/R levels |
| 08 | [`08_pivot_points.pine`](examples/indicators/08_pivot_points.pine) | Classic Pivot Points (Daily) |
| 09 | [`09_volume_profile.pine`](examples/indicators/09_volume_profile.pine) | Volume analysis + OBV |
| 10 | [`10_stoch_rsi.pine`](examples/indicators/10_stoch_rsi.pine) | Stochastic RSI K/D |
| 11 | [`11_ichimoku.pine`](examples/indicators/11_ichimoku.pine) | Ichimoku Cloud — all components |
| 12 | [`12_mtf_ema.pine`](examples/indicators/12_mtf_ema.pine) | Multi-Timeframe EMA D/W/M |
| 13 | [`13_session_highlight.pine`](examples/indicators/13_session_highlight.pine) | Session highlight (VIOP saatli) |
| 14 | [`14_rsi_divergence.pine`](examples/indicators/14_rsi_divergence.pine) | RSI Divergence detector |
| 15 | [`15_ema_ribbon.pine`](examples/indicators/15_ema_ribbon.pine) | EMA Ribbon 8/13/21/34/55/89/144/233 |
| 16 | [`16_chandelier_exit.pine`](examples/indicators/16_chandelier_exit.pine) | Chandelier Exit trailing stop |
| 17 | [`17_squeeze_momentum.pine`](examples/indicators/17_squeeze_momentum.pine) | Squeeze Momentum |
| 18 | [`18_fakeout_filter.pine`](examples/indicators/18_fakeout_filter.pine) | Fakeout Filter — 4-Layer Signal Quality |

### 🎯 Stratejiler / Strategies (13)

| # | Dosya | Açıklama / Description |
|---|-------|------------------------|
| 01 | [`01_ema_cross_strategy.pine`](examples/strategies/01_ema_cross_strategy.pine) | EMA Cross — ATR SL/TP |
| 02 | [`02_rsi_mean_reversion.pine`](examples/strategies/02_rsi_mean_reversion.pine) | RSI Mean Reversion |
| 03 | [`03_supertrend_strategy.pine`](examples/strategies/03_supertrend_strategy.pine) | Supertrend trend following |
| 04 | [`04_bb_breakout.pine`](examples/strategies/04_bb_breakout.pine) | Bollinger Band Breakout |
| 05 | [`05_macd_strategy.pine`](examples/strategies/05_macd_strategy.pine) | MACD + EMA trend filter |
| 06 | [`06_rsi_atr_strategy.pine`](examples/strategies/06_rsi_atr_strategy.pine) | RSI + ATR — **VIOP/BIST30 optimized** |
| 07 | [`07_mtf_trend_strategy.pine`](examples/strategies/07_mtf_trend_strategy.pine) | Multi-Timeframe trend |
| 08 | [`08_triple_ema_strategy.pine`](examples/strategies/08_triple_ema_strategy.pine) | Triple EMA 5/13/34 |
| 09 | [`09_stoch_strategy.pine`](examples/strategies/09_stoch_strategy.pine) | Stochastic + EMA filter |
| 10 | [`10_adx_trend_strategy.pine`](examples/strategies/10_adx_trend_strategy.pine) | ADX Trend Strength |
| 11 | [`11_viop_session_strategy.pine`](examples/strategies/11_viop_session_strategy.pine) | VIOP Session — seans bazlı |
| 12 | [`12_chandelier_strategy.pine`](examples/strategies/12_chandelier_strategy.pine) | Chandelier Exit Strategy |
| 13 | [`13_fakeout_confirmed_strategy.pine`](examples/strategies/13_fakeout_confirmed_strategy.pine) | Fakeout-Confirmed — 4 filters, high accuracy |

---

## 🌍 Global Markets (22)

TR: Dünyanın en çok işlem gören enstrümanları için hazır stratejiler.
Her dosyada doğru seans saati, komisyon ve slippage ayarları dahildir.

EN: Ready strategies for the world's most actively traded instruments.
Each file includes correct session times, commission and slippage settings.

### Temel Stratejiler / Base Strategies (12)

| # | Enstrüman | Sembol | Dosya |
|---|-----------|--------|-------|
| 01 | 🇺🇸 S&P 500 Futures | `CME_MINI:ES1!` | [`01_es_sp500.pine`](global-markets/01_es_sp500.pine) |
| 02 | 🇺🇸 Nasdaq-100 Futures | `CME_MINI:NQ1!` | [`02_nq_nasdaq.pine`](global-markets/02_nq_nasdaq.pine) |
| 03 | 🥇 Gold Futures | `COMEX:GC1!` | [`03_gc_gold.pine`](global-markets/03_gc_gold.pine) |
| 04 | 🛢️ Crude Oil | `NYMEX:CL1!` | [`04_cl_crude_oil.pine`](global-markets/04_cl_crude_oil.pine) |
| 05 | 💱 EUR/USD | `FX:EURUSD` | [`05_eurusd_forex.pine`](global-markets/05_eurusd_forex.pine) |
| 06 | 💱 GBP/USD | `FX:GBPUSD` | [`06_gbpusd_forex.pine`](global-markets/06_gbpusd_forex.pine) |
| 07 | 💱 USD/JPY | `FX:USDJPY` | [`07_usdjpy_forex.pine`](global-markets/07_usdjpy_forex.pine) |
| 08 | 🪙 Bitcoin | `BINANCE:BTCUSDT` | [`08_btc_crypto.pine`](global-markets/08_btc_crypto.pine) |
| 09 | 🪙 Ethereum | `BINANCE:ETHUSDT` | [`09_eth_crypto.pine`](global-markets/09_eth_crypto.pine) |
| 10 | 🇩🇪 DAX Germany | `XETR:DAX` | [`10_dax_germany.pine`](global-markets/10_dax_germany.pine) |
| 11 | 🇯🇵 Nikkei 225 | `TVC:NI225` | [`11_nikkei_japan.pine`](global-markets/11_nikkei_japan.pine) |
| 12 | 🌍 Universal | `syminfo.tickerid` | [`12_universal_strategy.pine`](global-markets/12_universal_strategy.pine) |

### Gelişmiş Stratejiler / Advanced Strategies (10)

| # | Enstrüman | Strateji | Dosya |
|---|-----------|----------|-------|
| 13 | 🪙 BTC | EMA Trend + RSI Pullback Entry | [`13_btc_trend_pullback.pine`](global-markets/13_btc_trend_pullback.pine) |
| 14 | 🪙 ETH | Volume-Confirmed Momentum Breakout | [`14_eth_momentum.pine`](global-markets/14_eth_momentum.pine) |
| 15 | 🇺🇸 ES | Opening Range Breakout (ORB) | [`15_es_opening_range.pine`](global-markets/15_es_opening_range.pine) |
| 16 | 🇺🇸 NQ | VWAP Mean Reversion | [`16_nq_vwap_reversion.pine`](global-markets/16_nq_vwap_reversion.pine) |
| 17 | 🥇 Gold | Triple EMA + ADX Trend | [`17_gc_gold_trend.pine`](global-markets/17_gc_gold_trend.pine) |
| 18 | 🛢️ CL | ATR Momentum + EIA Filter | [`18_cl_crude_momentum.pine`](global-markets/18_cl_crude_momentum.pine) |
| 19 | 💱 EURUSD | London Session Breakout | [`19_eurusd_london_breakout.pine`](global-markets/19_eurusd_london_breakout.pine) |
| 20 | 💱 GBPUSD | Market Structure + EMA Filter | [`20_gbpusd_structure.pine`](global-markets/20_gbpusd_structure.pine) |
| 21 | 💱 USDJPY | Carry Trade Trend Following | [`21_usdjpy_carry_trend.pine`](global-markets/21_usdjpy_carry_trend.pine) |
| 22 | 🇩🇪 DAX | Gap Fade + Xetra Session | [`22_dax_gap_fade.pine`](global-markets/22_dax_gap_fade.pine) |

---

## 🔔 Webhook Templates (7)

TR: TradingView alertlerini Telegram, Discord ve broker API'lerine iletmek için hazır şablonlar.
EN: Ready templates for forwarding TradingView alerts to Telegram, Discord, and broker APIs.

| Dosya | Açıklama / Description |
|-------|------------------------|
| [`01_alert_message_templates.md`](webhook-templates/01_alert_message_templates.md) | TradingView dinamik değişkenler + hazır mesaj şablonları |
| [`02_pine_alert_conditions.pine`](webhook-templates/02_pine_alert_conditions.pine) | `alertcondition()` + `alert()` tam örnekler |
| [`03_telegram_webhook.md`](webhook-templates/03_telegram_webhook.md) | Telegram Bot Python server kurulumu |
| [`04_discord_webhook.md`](webhook-templates/04_discord_webhook.md) | Discord webhook Python server kurulumu |
| [`05_json_payload_templates.md`](webhook-templates/05_json_payload_templates.md) | JSON payload şablonları (broker API'leri için) |
| [`06_viop_bist30_alerts.pine`](webhook-templates/06_viop_bist30_alerts.pine) | VİOP / BIST30 spesifik alert stratejisi |

---

## 🔄 v5 → v6 Migration (10)

TR: v5 kodlarını v6'ya taşımanız gereken en yaygın değişiklikler.
EN: Most common changes needed when migrating v5 code to v6.

| Dosya | Konu / Topic |
|-------|-------------|
| [`01_study_to_indicator.md`](v5-to-v6-migration/01_study_to_indicator.md) | `study()` → `indicator()` |
| [`02_security_to_request.md`](v5-to-v6-migration/02_security_to_request.md) | `security()` → `request.security()` |
| [`03_strategy_syntax.md`](v5-to-v6-migration/03_strategy_syntax.md) | Strategy declaration changes |
| [`04_type_system.md`](v5-to-v6-migration/04_type_system.md) | Type system & explicit declarations |
| [`05_arrays_and_collections.md`](v5-to-v6-migration/05_arrays_and_collections.md) | Array / map / matrix updates |
| [`06_input_functions.md`](v5-to-v6-migration/06_input_functions.md) | `input()` → `input.*` |
| [`07_drawing_objects.md`](v5-to-v6-migration/07_drawing_objects.md) | line / label / box updates |
| [`08_pine_logs.md`](v5-to-v6-migration/08_pine_logs.md) | New: `log.info()` / `log.warning()` |
| [`09_methods_and_udt.md`](v5-to-v6-migration/09_methods_and_udt.md) | New: User-defined methods & types |
| [`10_common_migration_errors.md`](v5-to-v6-migration/10_common_migration_errors.md) | Errors you will hit during migration |

---

## 📁 Dosya Yapısı / File Structure

```
pinescriptv6/
│
├── CLAUDE.md                    → Claude Code + Claude Projects
├── AGENTS.md                    → Devin, OpenAI Codex, autonomous agents
├── LESSONS_LEARNED.md           Hata hafızası / Error memory (AI auto-updates)
├── LLM_MANIFEST.md              Sorgu yönlendirme / Query routing map
├── SKILL.md                     AI yazma protokolü / AI writing protocol
│
├── assets/
│   ├── demo_chart.png           XU030 live demo screenshot
│   └── lessons_flow.png         System flow diagram
│
├── .cursor/rules/
│   └── pinescriptv6.mdc         → Cursor v0.44+
├── .cursorrules                 → Cursor (legacy fallback)
├── .windsurfrules               → Windsurf / Cascade
├── .clinerules                  → Cline, Roo, Continue, Aider
├── .zed/rules                   → Zed editor
├── .github/
│   └── copilot-instructions.md  → GitHub Copilot
│
├── concepts/
│   ├── execution_model.md       var, varip, barstate
│   ├── common_errors.md         max_bars_back, series type
│   ├── timeframes.md            request.security, repainting
│   ├── colors_and_display.md    color.new, gradients
│   ├── methods.md               user-defined methods
│   ├── objects.md               UDT, type system
│   └── signal_quality.md        Fakeout filters, volume, MTF, ATR
│
├── reference/
│   ├── variables.md
│   ├── constants.md
│   ├── types.md
│   ├── keywords.md
│   ├── annotations.md
│   └── functions/
│       ├── ta.md                RSI, EMA, MACD, ATR, crossover
│       ├── strategy.md          entry, exit, close, position
│       ├── drawing.md           plot, line, box, label, table
│       ├── request.md           security, financial, MTF
│       ├── collections.md       array, map, matrix
│       └── general.md           math, str, input, alert
│
├── writing_scripts/
│   ├── style_guide.md
│   ├── debugging.md
│   ├── profiling_and_optimization.md
│   └── limitations.md
│
├── examples/
│   ├── indicators/   (18 — copy-paste ready, tested in TradingView)
│   └── strategies/   (13 — copy-paste ready, tested in TradingView)
│
├── global-markets/   (22 strategies — ES, NQ, BTC, ETH, Gold, Forex, DAX, Nikkei)
├── webhook-templates/ (7 files — Telegram, Discord, JSON, VIOP)
└── v5-to-v6-migration/ (10 files — full migration guide)
```

---

## 📜 Lisans / License

MIT — [LICENSE](LICENSE) · Copyright © 2025 [Ugur Pala](https://github.com/trugurpala)

**Author / Yazar:**
[TradingView](https://tr.tradingview.com/u/trugurpala/) · [X / Twitter](https://x.com/trugurpala) · mail@ugurpala.com

> TR: TradingView'ın resmi Pine Script v6 dokümantasyonu temel referans materyali olarak kullanılmıştır. TradingView bu projeyle hiçbir resmi bağlantısı veya onayı bulunmamaktadır.
>
> EN: The official TradingView Pine Script v6 documentation was used as primary reference material. TradingView is not affiliated with or endorsing this project.

---

<div align="center">

⭐ TR: İşinize yaradıysa lütfen yıldız verin! / EN: If this saved you time, please star it! ⭐

[![Star History Chart](https://api.star-history.com/svg?repos=trugurpala/pinescriptv6&type=Date)](https://star-history.com/#trugurpala/pinescriptv6&Date)

</div>
