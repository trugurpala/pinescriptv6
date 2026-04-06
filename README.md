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

[Ugur Pala](https://github.com/trugurpala) · mail@ugurpala.com

[Demo](#-demo--xu030-bist-30-futures) ·
[Claude](#-claude--claude-code) ·
[Cursor](#️-cursor) ·
[Windsurf](#-windsurf) ·
[Copilot](#-github-copilot) ·
[Cline / Roo](#-cline--roo--aider) ·
[Örnekler](#-örnekler--examples) ·
[Global Markets](#-global-markets) ·
[Dosya Yapısı](#-dosya-yapısı--file-structure)

</div>

---

## 📺 Demo — XU030 (BIST 30 Futures)

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

## 🚀 Hızlı Başlangıç / Quick Start

```bash
git clone https://github.com/trugurpala/pinescriptv6.git
```

---

## 🤖 Claude / Claude Code

> TR: Claude Projects ve Claude Code ile entegrasyon. En tam deneyim için önerilen yöntem.
> EN: Integration with Claude Projects and Claude Code. Recommended for the fullest experience.

### TR | Türkçe

**Claude Projects**

[claude.ai/projects](https://claude.ai/projects) → projenizi açın → **Files** → **+** → **GitHub**

```
https://github.com/trugurpala/pinescriptv6
```

Tüm dosyaları seçin → **Add files** → proje sohbetinde:

```
/pinescript-v6
```

**Claude Code**

```bash
git clone https://github.com/trugurpala/pinescriptv6.git
cd pinescriptv6
claude
```

`CLAUDE.md` otomatik okunur. Claude artık Pine Script v6 kurallarını ve hata hafızasını biliyor.

---

### EN | English

**Claude Projects**

[claude.ai/projects](https://claude.ai/projects) → open your project → **Files** → **+** → **GitHub**

```
https://github.com/trugurpala/pinescriptv6
```

Select all files → **Add files** → in project chat:

```
/pinescript-v6
```

**Claude Code**

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

### TR | Türkçe

```bash
git clone https://github.com/trugurpala/pinescriptv6.git
cd pinescriptv6
cursor .
```

Kurallar otomatik devreye girer. Chat'te kullan:

```
@LESSONS_LEARNED.md EMA cross stratejisi yaz, XU030 için
```
```
@reference/functions/ta.md RSI divergence indikatörü yaz
```
```
@concepts/common_errors.md Bu hatanın sebebi ne?
```

---

### EN | English

```bash
git clone https://github.com/trugurpala/pinescriptv6.git
cd pinescriptv6
cursor .
```

Rules load automatically. Use in chat:

```
@LESSONS_LEARNED.md write an EMA cross strategy for XU030
```
```
@reference/functions/ta.md write an RSI divergence indicator
```
```
@concepts/common_errors.md what causes this error?
```

---

## 🌊 Windsurf

> TR: `.windsurfrules` dosyası Windsurf / Cascade tarafından otomatik okunur.
> EN: `.windsurfrules` is picked up automatically by Windsurf / Cascade.

### TR | Türkçe

```bash
git clone https://github.com/trugurpala/pinescriptv6.git
cd pinescriptv6
windsurf .
```

`.windsurfrules` otomatik yüklenir. Cascade artık Pine Script v6 kurallarını biliyor.

Chat'te kullan:

```
@LESSONS_LEARNED.md Supertrend stratejisi yaz
```
```
@reference/functions/strategy.md ATR tabanlı SL/TP nasıl yazılır?
```

---

### EN | English

```bash
git clone https://github.com/trugurpala/pinescriptv6.git
cd pinescriptv6
windsurf .
```

`.windsurfrules` loads automatically. Cascade now knows Pine Script v6 rules.

Use in Cascade chat:

```
@LESSONS_LEARNED.md write a Supertrend strategy
```
```
@reference/functions/strategy.md how to write ATR-based SL/TP?
```

---

## 🐙 GitHub Copilot

> TR: `.github/copilot-instructions.md` VS Code, JetBrains ve Copilot destekli editörlerde otomatik devreye girer.
> EN: `.github/copilot-instructions.md` activates automatically in VS Code, JetBrains, and any Copilot-enabled editor.

### TR | Türkçe

```bash
git clone https://github.com/trugurpala/pinescriptv6.git
code pinescriptv6
```

Copilot Chat'te kullan:

```
LESSONS_LEARNED.md dosyasını kontrol et, sonra bir RSI mean reversion stratejisi yaz.
```
```
reference/functions/ta.md dosyasına göre ta.pivothigh() imzası nedir?
```

---

### EN | English

```bash
git clone https://github.com/trugurpala/pinescriptv6.git
code pinescriptv6
```

Use in Copilot Chat:

```
Check LESSONS_LEARNED.md, then write an RSI mean reversion strategy.
```
```
According to reference/functions/ta.md, what is the ta.pivothigh() signature?
```

---

## 🔧 Cline / Roo / Aider

> TR: `.clinerules` dosyası Cline, Roo, Continue ve Aider tarafından otomatik okunur.
> EN: `.clinerules` is read automatically by Cline, Roo, Continue, and Aider.

```bash
git clone https://github.com/trugurpala/pinescriptv6.git
cd pinescriptv6
# Cline, Roo veya Aider ile bu klasörü aç
# Open this folder with Cline, Roo, or Aider
```

`.clinerules` otomatik yüklenir. / `.clinerules` loads automatically.

---

## 🤗 Custom GPT / Diğer LLM'ler / Other LLMs

### TR | Türkçe

ZIP olarak indir:

[https://github.com/trugurpala/pinescriptv6/archive/refs/heads/main.zip](https://github.com/trugurpala/pinescriptv6/archive/refs/heads/main.zip)

Minimum önerilen yükleme: `LESSONS_LEARNED.md` + `LLM_MANIFEST.md` + `reference/functions/`

Sistem promptuna ekle:

```
Bu proje Pine Script v6 geliştirme için optimize edilmiş bir bilgi tabanıdır.
Kod yazmadan önce her zaman LESSONS_LEARNED.md içeriğini kontrol et.
Hangi dosyayı okuyacağını belirlemek için LLM_MANIFEST.md'ye başvur.
Tüm scriptler //@version=6 ile başlamalıdır.
```

---

### EN | English

Download as ZIP:

[https://github.com/trugurpala/pinescriptv6/archive/refs/heads/main.zip](https://github.com/trugurpala/pinescriptv6/archive/refs/heads/main.zip)

Minimum recommended upload: `LESSONS_LEARNED.md` + `LLM_MANIFEST.md` + `reference/functions/`

Add to system prompt:

```
This project is a knowledge base optimised for Pine Script v6 development.
Always check LESSONS_LEARNED.md before writing any code.
Consult LLM_MANIFEST.md to determine which file to read for each task.
All scripts must start with //@version=6.
```

---

## 📦 Örnekler / Examples

TR: 30+ hazır Pine Script v6 örneği — copy-paste hazır, TradingView'da test edilmiş.
EN: 30+ ready-to-use Pine Script v6 examples — copy-paste ready, tested in TradingView.

### 📊 İndikatörler / Indicators

| # | Dosya | Açıklama / Description |
|---|-------|------------------------|
| 01 | [`examples/indicators/01_ema_cross.pine`](examples/indicators/01_ema_cross.pine) | EMA 9/21 Cross + bgcolor + alerts |
| 02 | [`examples/indicators/02_rsi_ob_os.pine`](examples/indicators/02_rsi_ob_os.pine) | RSI 14 Gradient — OB/OS zones |
| 03 | [`examples/indicators/03_macd_histogram.pine`](examples/indicators/03_macd_histogram.pine) | MACD 12/26/9 — colored histogram |
| 04 | [`examples/indicators/04_bollinger_bands.pine`](examples/indicators/04_bollinger_bands.pine) | Bollinger Bands + squeeze |
| 05 | [`examples/indicators/05_supertrend.pine`](examples/indicators/05_supertrend.pine) | Supertrend ATR-based |
| 06 | [`examples/indicators/06_vwap_session.pine`](examples/indicators/06_vwap_session.pine) | VWAP + StDev bands |
| 07 | [`examples/indicators/07_atr_levels.pine`](examples/indicators/07_atr_levels.pine) | ATR dynamic S/R levels |
| 08 | [`examples/indicators/08_pivot_points.pine`](examples/indicators/08_pivot_points.pine) | Classic Pivot Points (Daily) |
| 09 | [`examples/indicators/09_volume_profile.pine`](examples/indicators/09_volume_profile.pine) | Volume analysis + OBV |
| 10 | [`examples/indicators/10_stoch_rsi.pine`](examples/indicators/10_stoch_rsi.pine) | Stochastic RSI K/D |
| 11 | [`examples/indicators/11_ichimoku.pine`](examples/indicators/11_ichimoku.pine) | Ichimoku Cloud — all components |
| 12 | [`examples/indicators/12_mtf_ema.pine`](examples/indicators/12_mtf_ema.pine) | Multi-Timeframe EMA D/W/M |
| 13 | [`examples/indicators/13_session_highlight.pine`](examples/indicators/13_session_highlight.pine) | Session highlight (VIOP saatli) |
| 14 | [`examples/indicators/14_rsi_divergence.pine`](examples/indicators/14_rsi_divergence.pine) | RSI Divergence detector |
| 15 | [`examples/indicators/15_ema_ribbon.pine`](examples/indicators/15_ema_ribbon.pine) | EMA Ribbon 8/13/21/34/55/89/144/233 |
| 16 | [`examples/indicators/16_chandelier_exit.pine`](examples/indicators/16_chandelier_exit.pine) | Chandelier Exit trailing stop |
| 17 | [`examples/indicators/17_squeeze_momentum.pine`](examples/indicators/17_squeeze_momentum.pine) | Squeeze Momentum |

### 🎯 Stratejiler / Strategies

| # | Dosya | Açıklama / Description |
|---|-------|------------------------|
| 01 | [`examples/strategies/01_ema_cross_strategy.pine`](examples/strategies/01_ema_cross_strategy.pine) | EMA Cross — ATR SL/TP |
| 02 | [`examples/strategies/02_rsi_mean_reversion.pine`](examples/strategies/02_rsi_mean_reversion.pine) | RSI Mean Reversion |
| 03 | [`examples/strategies/03_supertrend_strategy.pine`](examples/strategies/03_supertrend_strategy.pine) | Supertrend trend following |
| 04 | [`examples/strategies/04_bb_breakout.pine`](examples/strategies/04_bb_breakout.pine) | Bollinger Band Breakout |
| 05 | [`examples/strategies/05_macd_strategy.pine`](examples/strategies/05_macd_strategy.pine) | MACD + EMA trend filter |
| 06 | [`examples/strategies/06_rsi_atr_strategy.pine`](examples/strategies/06_rsi_atr_strategy.pine) | RSI + ATR — **VIOP/BIST30 optimized** |
| 07 | [`examples/strategies/07_mtf_trend_strategy.pine`](examples/strategies/07_mtf_trend_strategy.pine) | Multi-Timeframe trend |
| 08 | [`examples/strategies/08_triple_ema_strategy.pine`](examples/strategies/08_triple_ema_strategy.pine) | Triple EMA 5/13/34 |
| 09 | [`examples/strategies/09_stoch_strategy.pine`](examples/strategies/09_stoch_strategy.pine) | Stochastic + EMA filter |
| 10 | [`examples/strategies/10_adx_trend_strategy.pine`](examples/strategies/10_adx_trend_strategy.pine) | ADX Trend Strength |
| 11 | [`examples/strategies/11_viop_session_strategy.pine`](examples/strategies/11_viop_session_strategy.pine) | VIOP Session — seans bazlı |
| 12 | [`examples/strategies/12_chandelier_strategy.pine`](examples/strategies/12_chandelier_strategy.pine) | Chandelier Exit Strategy |

---

## 🌍 Global Markets

TR: Dünyanın en çok işlem gören enstrümanları için hazır stratejiler — doğru seans saatleri ve komisyon ayarları dahil.
EN: Ready strategies for the world's most actively traded instruments — correct session times and commission settings included.

| Enstrüman | Sembol | Dosya |
|-----------|--------|-------|
| 🇺🇸 S&P 500 Futures | `CME_MINI:ES1!` | [`global-markets/01_es_sp500.pine`](global-markets/01_es_sp500.pine) |
| 🇺🇸 Nasdaq-100 Futures | `CME_MINI:NQ1!` | [`global-markets/02_nq_nasdaq.pine`](global-markets/02_nq_nasdaq.pine) |
| 🥇 Gold Futures | `COMEX:GC1!` | [`global-markets/03_gc_gold.pine`](global-markets/03_gc_gold.pine) |
| 🛢️ Crude Oil | `NYMEX:CL1!` | [`global-markets/04_cl_crude_oil.pine`](global-markets/04_cl_crude_oil.pine) |
| 💱 EUR/USD | `FX:EURUSD` | [`global-markets/05_eurusd_forex.pine`](global-markets/05_eurusd_forex.pine) |
| 💱 GBP/USD | `FX:GBPUSD` | [`global-markets/06_gbpusd_forex.pine`](global-markets/06_gbpusd_forex.pine) |
| 💱 USD/JPY | `FX:USDJPY` | [`global-markets/07_usdjpy_forex.pine`](global-markets/07_usdjpy_forex.pine) |
| 🪙 Bitcoin | `BINANCE:BTCUSDT` | [`global-markets/08_btc_crypto.pine`](global-markets/08_btc_crypto.pine) |
| 🪙 Ethereum | `BINANCE:ETHUSDT` | [`global-markets/09_eth_crypto.pine`](global-markets/09_eth_crypto.pine) |
| 🇩🇪 DAX Germany | `XETR:DAX` | [`global-markets/10_dax_germany.pine`](global-markets/10_dax_germany.pine) |
| 🇯🇵 Nikkei 225 | `TVC:NI225` | [`global-markets/11_nikkei_japan.pine`](global-markets/11_nikkei_japan.pine) |
| 🌍 Universal | `syminfo.tickerid` | [`global-markets/12_universal_strategy.pine`](global-markets/12_universal_strategy.pine) |

---

## 📁 Dosya Yapısı / File Structure

```
pinescriptv6/
│
├── CLAUDE.md                   → Claude Code + Claude Projects
├── AGENTS.md                   → Devin, OpenAI Codex, autonomous agents
├── LESSONS_LEARNED.md          TR: Hata hafızası / EN: Error memory (AI auto-updates)
├── LLM_MANIFEST.md             TR: Sorgu yönlendirme / EN: Query routing map
├── SKILL.md                    TR: AI yazma protokolü / EN: AI writing protocol
│
├── assets/
│   ├── demo_chart.png          XU030 live demo screenshot
│   └── lessons_flow.png        System flow diagram
│
├── .cursor/rules/
│   └── pinescriptv6.mdc        → Cursor v0.44+
├── .cursorrules                → Cursor (legacy fallback)
├── .windsurfrules              → Windsurf / Cascade
├── .clinerules                 → Cline, Roo, Continue, Aider
├── .zed/rules                  → Zed editor
├── .github/
│   ├── copilot-instructions.md → GitHub Copilot
│   ├── pull_request_template.md
│   └── ISSUE_TEMPLATE/
│
├── concepts/
│   ├── execution_model.md
│   ├── common_errors.md
│   ├── timeframes.md
│   ├── colors_and_display.md
│   ├── methods.md
│   └── objects.md
│
├── reference/
│   ├── variables.md
│   ├── constants.md
│   ├── types.md
│   ├── keywords.md
│   ├── annotations.md
│   └── functions/
│       ├── ta.md
│       ├── strategy.md
│       ├── drawing.md
│       ├── request.md
│       ├── collections.md
│       └── general.md
│
├── writing_scripts/
│   ├── style_guide.md
│   ├── debugging.md
│   ├── profiling_and_optimization.md
│   └── limitations.md
│
├── examples/
│   ├── indicators/             17 indicators — copy-paste ready
│   └── strategies/             12 strategies — copy-paste ready
│
├── global-markets/             12 instruments (ES, NQ, GC, CL, EUR/USD, BTC...)
├── webhook-templates/          Telegram, Discord, JSON payload, VIOP alerts
└── v5-to-v6-migration/         10 files — v5 to v6 migration guide
```

---

## 📜 Lisans / License

MIT — [LICENSE](LICENSE) · Copyright © 2025 [Ugur Pala](https://github.com/trugurpala)

> TR: TradingView'ın resmi Pine Script v6 dokümantasyonu temel referans materyali olarak kullanılmıştır. TradingView bu projeyle hiçbir bağlantısı veya onayı bulunmamaktadır.
>
> EN: The official TradingView Pine Script v6 documentation was used as primary reference material. TradingView is not affiliated with or endorsing this project.

---

<div align="center">

⭐ TR: İşinize yaradıysa lütfen yıldız verin! / EN: If this saved you time, please star it! ⭐

[![Star History Chart](https://api.star-history.com/svg?repos=trugurpala/pinescriptv6&type=Date)](https://star-history.com/#trugurpala/pinescriptv6&Date)

</div>