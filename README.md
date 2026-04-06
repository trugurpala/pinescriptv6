# Pine Script v6 — AI Reference with Error Memory

<div align="center">

![Pine Script v6](https://img.shields.io/badge/Pine%20Script-v6-1E88E5?style=for-the-badge&logo=tradingview&logoColor=white)
![AI Ready](https://img.shields.io/badge/AI%20Ready-9%20Editors-7C3AED?style=for-the-badge)
![Examples](https://img.shields.io/badge/Examples-55%2B-22C55E?style=for-the-badge)
![MIT License](https://img.shields.io/badge/License-MIT-F59E0B?style=for-the-badge)
![Stars](https://img.shields.io/github/stars/trugurpala/pinescriptv6?style=for-the-badge&color=yellow)
![TR | EN](https://img.shields.io/badge/TR%20%7C%20EN-Bilingual-8B5CF6?style=for-the-badge)

### TR: AI editörünüz artık Pine Script v6'yı doğru yazar — ve hatalarını unutmaz.
### EN: Your AI editor now writes Pine Script v6 correctly — and never forgets its mistakes.

[Ugur Pala](https://github.com/trugurpala) · [TradingView](https://tr.tradingview.com/u/trugurpala/) · [X / Twitter](https://x.com/trugurpala) · mail@ugurpala.com

---

**[🚀 Hızlı Başlangıç](#-hızlı-başlangıç--quick-start)** · **[💡 Neden?](#-neden-var--why-this-exists)** · **[⚙️ Nasıl Çalışır?](#️-nasıl-çalışır--how-it-works)** · **[🤖 Claude](#-claude--claude-code)** · **[⌨️ Cursor](#️-cursor)** · **[🌊 Windsurf](#-windsurf)** · **[🐙 Copilot](#-github-copilot)** · **[🔧 Cline/Roo](#-cline--roo--aider)** · **[📦 Örnekler](#-örnekler--examples)** · **[🌍 Global Markets](#-global-markets-22)** · **[🔔 Webhook](#-webhook-templates-7)** · **[🔄 v5→v6](#-v5--v6-migration-10)**

</div>

---

## 💡 Neden Var / Why This Exists

> **TR: Çünkü AI editörler Pine Script v6 çıktıktan sonra bile v5 yazmaya devam etti.**
> **EN: Because AI editors kept writing v5 code even after Pine Script v6 launched.**

### TR | Türkçe — Gerçek Problem

TradingView Pine Script v6'yı yayınladığında her şey değişti. Ama AI editörler bunu bilmiyordu:

```pine
// ❌ AI'ın v6'da yazdığı — TradingView'da hata verir
//@version=6
study("My Indicator", overlay=true)           // study() v6'da YOK
htf = security(syminfo.tickerid, "D", close)  // security() v6'da YOK
len = input(14, type=input.integer)           // eski input() v6'da YOK
```

```pine
// ✅ Bu repo bağlıyken AI'ın yazdığı — ilk seferde çalışır
//@version=6
indicator("My Indicator", overlay=true)
htf = request.security(syminfo.tickerid, "D", close[1], lookahead=barmerge.lookahead_on)
int len = input.int(14, "Length")
```

**Bu repo üç sorunu çözdü:**

| # | Sorun | Çözüm | Nasıl? |
|---|-------|-------|--------|
| 1 | **AI'ın hafızası yok** — her oturumda sıfırdan başlar, aynı hataları tekrarlar | `LESSONS_LEARNED.md` | Çözülen her hata kalıcı kaydedilir, AI bir sonraki oturumda okur |
| 2 | **v6 referansı çok büyük** — tüm doküman context'e sığmaz | `LLM_MANIFEST.md` | AI sadece o göreve gereken dosyayı okur, token israfı olmaz |
| 3 | **Her editör farklı format bekler** — Claude, Cursor, Windsurf hepsi ayrı | 9 kural dosyası | `CLAUDE.md`, `.cursor/rules/`, `.windsurfrules`, `.clinerules`... hepsi hazır |

---

### EN | English — The Real Problem

When TradingView launched Pine Script v6, everything changed. But AI editors didn't know this.

**Three problems existed. This repo solved all three:**

| # | Problem | Solution | How? |
|---|---------|----------|------|
| 1 | **AI has no memory** — starts from zero each session, repeats mistakes | `LESSONS_LEARNED.md` | Every solved error saved permanently, AI reads it next session |
| 2 | **v6 reference is too large** — full docs won't fit in context | `LLM_MANIFEST.md` | AI reads only the file needed for that task |
| 3 | **Every editor expects different format** — Claude, Cursor, Windsurf all differ | 9 rule files | `CLAUDE.md`, `.cursor/rules/`, `.windsurfrules`, `.clinerules`... all ready |

---

## ⚙️ Nasıl Çalışır / How It Works

> **TR: Repo bağlandıktan sonra arka planda tam olarak neler oluyor?**
> **EN: What exactly happens under the hood after connecting the repo?**

---

### TR | Türkçe — 5 Adım

**Adım 1 — AI önce `LESSONS_LEARNED.md`'yi okur**

Sen: *"XU030 için EMA cross stratejisi yaz"* dediğinde AI önce hata hafızasını kontrol eder:

```
AI: "LESSONS_LEARNED.md okudum. Bilinen hatalar:
     ⚠ ta.stoch() v6'da tuple döndürmez, sadece K döner
     ⚠ math.avg() v6'da yok, (a+b)/2 kullan
     ⚠ Hacim onayı olmadan EMA cross = muhtemelen fakeout
     Şimdi kodu yazıyorum..."
```

> Bu dosya olmadan AI bu hataları bilmez ve tekrarlar.
> `LESSONS_LEARNED.md` zamanla büyür → repo daha akıllı olur.

---

**Adım 2 — `LLM_MANIFEST.md` ile doğru referans dosyası bulunur**

Görev "EMA cross stratejisi" → AI sadece gerekli 2 dosyayı okur:

```
AI: "LLM_MANIFEST.md'ye baktım.
     Bu görev için: reference/functions/ta.md + reference/functions/strategy.md
     Dosyaları okuyorum... hazır."
```

> Tüm doküman yerine 2 dosya okunur. Context korunur. Yanıt kalitesi artar.

---

**Adım 3 — `//@version=6` ile başlayan temiz, çalışan kod yazılır**

```pine
//@version=6
// github.com/trugurpala/pinescriptv6 — Ugur Pala
strategy("EMA Cross [trugurpala]", overlay=true,
    initial_capital   = 10000,
    default_qty_type  = strategy.percent_of_equity,
    default_qty_value = 10,
    commission_type   = strategy.commission.percent,
    commission_value  = 0.03)   // VİOP komisyon oranı

int   fastLen = input.int(9,  "Fast EMA", minval=1)
int   slowLen = input.int(21, "Slow EMA", minval=1)
float slMult  = input.float(2.0, "SL Mult", step=0.1)
float tpMult  = input.float(3.0, "TP Mult", step=0.1)

float fast   = ta.ema(close, fastLen)
float slow   = ta.ema(close, slowLen)
float atrVal = ta.atr(14)
bool  inSes  = not na(time(timeframe.period, "0930-1815", "UTC+3"))

if ta.crossover(fast, slow) and inSes
    strategy.entry("Long", strategy.long)
    strategy.exit("LE", "Long",
        stop  = close - slMult * atrVal,
        limit = close + tpMult * atrVal)

if ta.crossunder(fast, slow) and inSes
    strategy.close("Long")

plot(fast, "Fast", fast > slow ? color.green : color.red,    linewidth=2)
plot(slow, "Slow", fast > slow ? color.lime  : color.orange, linewidth=2)
```

> v5 syntax yok. Seans filtresi var. ATR SL/TP var. **İlk seferde çalışır.**

---

**Adım 4 — Hata alınırsa çözülür ve `LESSONS_LEARNED.md`'ye eklenir**

TradingView'da hata: `"Cannot call 'ta.stoch' with these arguments"`

```
Sen: "Bu hata ne anlama geliyor?"

AI: "ta.stoch() v6'da tuple döndürmüyor. Çözüm şu:
     float rawK = ta.stoch(high, low, close, 14)
     float k    = ta.sma(rawK, 3)
     
     Bu hatayı LESSONS_LEARNED.md'ye ekliyorum
     ki bir daha sorman gerekmesin."
```

`LESSONS_LEARNED.md` otomatik güncellenir — bir daha o hata tekrarlanmaz.

---

**Adım 5 — Bir sonraki oturumda aynı hata sıfırdan anlatılmaz**

Yarın yeni bir oturum. Farklı bir strateji istiyorsun.

```
Sen: "Stochastic + EMA stratejisi yaz"

AI: "LESSONS_LEARNED.md okudum.
     NOT: ta.stoch() v6'da sadece K döndürür, tuple değil.
     Bu bilgiyle yazıyorum..."
```

> **Bir kez öğrenildi. Sonsuza kadar hatırlandı.**

---

### Kullandığını Nasıl Anlarsın? / How Do You Know It's Working?

| ✅ Repo Aktif | ❌ Repo Bağlı Değil |
|--------------|---------------------|
| AI "LESSONS_LEARNED.md okudum" diyor | AI direkt koda giriyor |
| `//@version=6` ile başlıyor | `study()` veya `security()` yazıyor |
| `indicator()` + `request.security()` + `input.int()` kullanıyor | v5 syntax var |
| Hata alınınca "LESSONS_LEARNED.md'ye ekliyorum" diyor | Aynı hata tekrarlanıyor |
| Seans filtresi, ATR SL/TP, komisyon var | Basit, filtresiz kod |
| Yorumda `// github.com/trugurpala/pinescriptv6` var | Kaynak yok |

---

### EN | English — 5 Steps

**Step 1 — AI reads `LESSONS_LEARNED.md` first**

You say *"Write an EMA cross strategy for ES futures"*. AI checks error memory first:

```
AI: "Read LESSONS_LEARNED.md. Known issues:
     ⚠ ta.stoch() returns only K in v6, not a tuple
     ⚠ math.avg() removed — use (a+b)/2
     ⚠ EMA cross without volume = likely fakeout
     Now writing the code..."
```

> Without this file, AI doesn't know these and repeats them.
> `LESSONS_LEARNED.md` grows over time → repo gets smarter.

---

**Step 2 — `LLM_MANIFEST.md` routes to the correct reference file**

Task is "EMA cross strategy" → AI reads only 2 files:

```
AI: "Checked LLM_MANIFEST.md.
     For this task: reference/functions/ta.md + reference/functions/strategy.md
     Reading... ready."
```

> 2 files instead of full documentation. Context preserved. Quality higher.

---

**Step 3 — Clean code written starting with `//@version=6`**

> No v5 syntax. Session filter included. ATR SL/TP included. **Works first time.**

---

**Step 4 — On error: solved and saved to `LESSONS_LEARNED.md`**

```
You: "What does this error mean?"
AI:  "ta.stoch() doesn't return a tuple in v6. Here's the fix...
     Adding this to LESSONS_LEARNED.md so you never have to ask again."
```

---

**Step 5 — Next session: same error never explained from scratch**

> **Learned once. Remembered forever.**

---

## 🚀 Hızlı Başlangıç / Quick Start

```bash
git clone https://github.com/trugurpala/pinescriptv6.git
```

Hangi editörü kullanıyorsun? / Which editor are you using?
→ Aşağıdaki ilgili bölüme git / Jump to the relevant section below.

---

## 🤖 Claude / Claude Code

> **TR: En derin entegrasyon — `CLAUDE.md` aracılığıyla tüm kurallar ve hata hafızası otomatik yüklenir.**
> **EN: Deepest integration — all rules and error memory auto-loaded via `CLAUDE.md`.**

### TR | Türkçe

**Seçenek A — Claude Projects (tarayıcı, önerilen)**

1. [claude.ai/projects](https://claude.ai/projects) adresine git
2. **+ New project** veya mevcut projeyi aç
3. Sağ panel: **Files** → **+** → **GitHub**
4. URL kutusuna:
   ```
   https://github.com/trugurpala/pinescriptv6
   ```
5. **pinescriptv6** checkbox → **Add files**
6. Proje sohbetinde artık doğrudan yaz:
   ```
   XU030 için EMA cross stratejisi yaz
   ```

Claude otomatik olarak `LESSONS_LEARNED.md` → `LLM_MANIFEST.md` → referans dosyası sırasını takip eder.

**Seçenek B — Claude Code (terminal)**

```bash
git clone https://github.com/trugurpala/pinescriptv6.git
cd pinescriptv6
claude
```

`CLAUDE.md` otomatik okunur. Artık her istekte Claude hata hafızasını bilir, v5 yazmaz.

---

### EN | English

**Option A — Claude Projects (browser, recommended)**

1. Go to [claude.ai/projects](https://claude.ai/projects)
2. **+ New project** or open existing
3. Right panel: **Files** → **+** → **GitHub**
4. Paste:
   ```
   https://github.com/trugurpala/pinescriptv6
   ```
5. **pinescriptv6** checkbox → **Add files**
6. Just chat:
   ```
   Write an EMA cross strategy for ES futures
   ```

**Option B — Claude Code (terminal)**

```bash
git clone https://github.com/trugurpala/pinescriptv6.git
cd pinescriptv6
claude
```

`CLAUDE.md` is read automatically. Claude now knows error memory, never writes v5.

---

## ⌨️ Cursor

> **TR: `.cursor/rules/pinescriptv6.mdc` (v0.44+) veya `.cursorrules` (eski) otomatik yüklenir.**
> **EN: `.cursor/rules/pinescriptv6.mdc` (v0.44+) or `.cursorrules` (older) loads automatically.**

```bash
git clone https://github.com/trugurpala/pinescriptv6.git
cd pinescriptv6
cursor .
```

**TR** — Klasör açılınca kurallar devreye girer. Chat'te `@` ile dosyaları etiketle:

```
@LESSONS_LEARNED.md EMA cross stratejisi yaz, XU030 için
@reference/functions/ta.md RSI divergence indikatörü nasıl yazılır?
@concepts/common_errors.md Bu Pine Script v6 hatasının sebebi ne?
@concepts/signal_quality.md Fakeout filtrelemeli bir strateji yaz
```

**EN** — Rules activate on folder open. Tag files with `@` in chat:

```
@LESSONS_LEARNED.md write an EMA cross strategy for XU030
@reference/functions/ta.md how to write an RSI divergence indicator?
@concepts/common_errors.md what causes this Pine Script v6 error?
@concepts/signal_quality.md write a strategy with fakeout filtering
```

---

## 🌊 Windsurf

> **TR: `.windsurfrules` Windsurf / Cascade tarafından otomatik okunur — sıfır kurulum.**
> **EN: `.windsurfrules` is read automatically by Windsurf / Cascade — zero setup.**

```bash
git clone https://github.com/trugurpala/pinescriptv6.git
cd pinescriptv6
windsurf .
```

**TR** — Cascade chat'te:

```
@LESSONS_LEARNED.md Supertrend + hacim filtreli strateji yaz
@reference/functions/strategy.md ATR tabanlı SL/TP nasıl yazılır?
@concepts/signal_quality.md Fakeout nedir, nasıl filtrerim?
```

**EN** — In Cascade chat:

```
@LESSONS_LEARNED.md write a Supertrend strategy with volume filter
@reference/functions/strategy.md how to write ATR-based SL/TP?
@concepts/signal_quality.md what is a fakeout and how do I filter it?
```

---

## 🐙 GitHub Copilot

> **TR: `.github/copilot-instructions.md` VS Code, JetBrains ve tüm Copilot destekli editörlerde otomatik devreye girer.**
> **EN: `.github/copilot-instructions.md` activates in VS Code, JetBrains, and all Copilot-enabled editors.**

```bash
git clone https://github.com/trugurpala/pinescriptv6.git
code pinescriptv6
```

**TR** — Copilot Chat'te:

```
LESSONS_LEARNED.md dosyasını önce kontrol et, sonra RSI mean reversion stratejisi yaz.
reference/functions/ta.md dosyasına göre ta.pivothigh() fonksiyonunun imzası nedir?
Bu Pine Script v6 hatasını açıkla: "Cannot use 'series' type as argument"
concepts/signal_quality.md'ye göre hacim onaylı bir EMA cross stratejisi yaz.
```

**EN** — In Copilot Chat:

```
Check LESSONS_LEARNED.md first, then write an RSI mean reversion strategy.
According to reference/functions/ta.md, what is the ta.pivothigh() signature?
Explain this Pine Script v6 error: "Cannot use 'series' type as argument"
According to concepts/signal_quality.md, write a volume-confirmed EMA cross strategy.
```

---

## 🔧 Cline / Roo / Aider

> **TR: `.clinerules` Cline, Roo, Continue ve Aider tarafından otomatik okunur.**
> **EN: `.clinerules` is read automatically by Cline, Roo, Continue, and Aider.**

```bash
git clone https://github.com/trugurpala/pinescriptv6.git
cd pinescriptv6
# Cline veya Roo ile VS Code'dan aç / Open with Cline or Roo from VS Code
```

`.clinerules` otomatik yüklenir. / `.clinerules` loads automatically.

**Aider için / For Aider:**
```bash
aider --read LESSONS_LEARNED.md --read LLM_MANIFEST.md
```

---

## 🤗 Custom GPT / Diğer LLM'ler / Other LLMs

ZIP: [main.zip](https://github.com/trugurpala/pinescriptv6/archive/refs/heads/main.zip)

**TR** — Minimum yükleme + sistem promptu:

```
Bu proje Pine Script v6 geliştirme için optimize edilmiş bir bilgi tabanıdır.
Kod yazmadan önce her zaman LESSONS_LEARNED.md içeriğini kontrol et.
Hangi dosyayı okuyacağını belirlemek için LLM_MANIFEST.md'ye başvur.
Tüm scriptler //@version=6 ile başlamalıdır.
v5 syntax kullanma: study(), security(), bare input() yasak.
Hata alınca LESSONS_LEARNED.md formatında kaydet.
```

**EN** — Minimum upload + system prompt:

```
This project is a knowledge base optimised for Pine Script v6 development.
Always check LESSONS_LEARNED.md before writing any code.
Consult LLM_MANIFEST.md to determine which file to read for each task.
All scripts must start with //@version=6.
Never use v5 syntax: study(), security(), bare input() are forbidden.
On error: save in LESSONS_LEARNED.md format.
```

---

## 📦 Örnekler / Examples

**TR: 55+ hazır Pine Script v6 örneği — TradingView'da test edilmiş, copy-paste hazır.**
**EN: 55+ ready-to-use Pine Script v6 examples — tested in TradingView, copy-paste ready.**

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
| 13 | [`13_session_highlight.pine`](examples/indicators/13_session_highlight.pine) | Session highlight (VIOP/BIST30) |
| 14 | [`14_rsi_divergence.pine`](examples/indicators/14_rsi_divergence.pine) | RSI Divergence detector |
| 15 | [`15_ema_ribbon.pine`](examples/indicators/15_ema_ribbon.pine) | EMA Ribbon 8/13/21/34/55/89/144/233 |
| 16 | [`16_chandelier_exit.pine`](examples/indicators/16_chandelier_exit.pine) | Chandelier Exit trailing stop |
| 17 | [`17_squeeze_momentum.pine`](examples/indicators/17_squeeze_momentum.pine) | Squeeze Momentum |
| 18 | [`18_fakeout_filter.pine`](examples/indicators/18_fakeout_filter.pine) | **Fakeout Filter — 4-Layer Signal Quality** |

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
| 13 | [`13_fakeout_confirmed_strategy.pine`](examples/strategies/13_fakeout_confirmed_strategy.pine) | **Fakeout-Confirmed — Hacim+HTF+ATR+Bar** |

---

## 🌍 Global Markets (22)

**TR: Dünyanın en çok işlem gören enstrümanları. Her dosyada doğru seans saati, komisyon ve slippage dahil.**
**EN: World's most actively traded instruments. Correct session times, commission and slippage in every file.**

### Temel Stratejiler / Base Strategies (12)

| # | Enstrüman | Sembol | Dosya |
|---|-----------|--------|-------|
| 01 | 🇺🇸 S&P 500 Futures | `CME_MINI:ES1!` / `MES1!` | [`01_es_sp500.pine`](global-markets/01_es_sp500.pine) |
| 02 | 🇺🇸 Nasdaq-100 Futures | `CME_MINI:NQ1!` / `MNQ1!` | [`02_nq_nasdaq.pine`](global-markets/02_nq_nasdaq.pine) |
| 03 | 🥇 Gold Futures | `COMEX:GC1!` / `XAUUSD` | [`03_gc_gold.pine`](global-markets/03_gc_gold.pine) |
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

**TR: TradingView alertlerini Telegram, Discord ve broker API'lerine iletmek için hazır şablonlar.**
**EN: Ready templates for forwarding TradingView alerts to Telegram, Discord, and broker APIs.**

| Dosya | Açıklama / Description |
|-------|------------------------|
| [`01_alert_message_templates.md`](webhook-templates/01_alert_message_templates.md) | `{{ticker}}`, `{{close}}`, `{{strategy.order.action}}` — tüm dinamik değişkenler |
| [`02_pine_alert_conditions.pine`](webhook-templates/02_pine_alert_conditions.pine) | `alertcondition()` + `alert()` — tam çalışan örnekler |
| [`03_telegram_webhook.md`](webhook-templates/03_telegram_webhook.md) | Telegram Bot + Python server — adım adım kurulum |
| [`04_discord_webhook.md`](webhook-templates/04_discord_webhook.md) | Discord webhook + embed mesajlar |
| [`05_json_payload_templates.md`](webhook-templates/05_json_payload_templates.md) | Broker API JSON — buy/sell/position şablonları |
| [`06_viop_bist30_alerts.pine`](webhook-templates/06_viop_bist30_alerts.pine) | VİOP / BIST30 — seans filtreli, komisyon ayarlı |

---

## 🔄 v5 → v6 Migration (10)

**TR: v5 kodlarını v6'ya taşırken en sık karşılaşılan değişiklikler.**
**EN: Most common changes when migrating v5 code to v6.**

| Dosya | Konu / Topic |
|-------|-------------|
| [`01_study_to_indicator.md`](v5-to-v6-migration/01_study_to_indicator.md) | `study()` → `indicator()` — en yaygın hata |
| [`02_security_to_request.md`](v5-to-v6-migration/02_security_to_request.md) | `security()` → `request.security()` |
| [`03_strategy_syntax.md`](v5-to-v6-migration/03_strategy_syntax.md) | Strategy declaration değişiklikleri |
| [`04_type_system.md`](v5-to-v6-migration/04_type_system.md) | Explicit type — `int`, `float`, `bool` |
| [`05_arrays_and_collections.md`](v5-to-v6-migration/05_arrays_and_collections.md) | `array.new_float()` → `array.new<float>()` |
| [`06_input_functions.md`](v5-to-v6-migration/06_input_functions.md) | `input()` → `input.int()`, `input.float()`... |
| [`07_drawing_objects.md`](v5-to-v6-migration/07_drawing_objects.md) | `line`, `label`, `box` — `chart.point` yeniliği |
| [`08_pine_logs.md`](v5-to-v6-migration/08_pine_logs.md) | Yeni: `log.info()`, `log.warning()`, `log.error()` |
| [`09_methods_and_udt.md`](v5-to-v6-migration/09_methods_and_udt.md) | Yeni: User-defined types + methods |
| [`10_common_migration_errors.md`](v5-to-v6-migration/10_common_migration_errors.md) | 7 yaygın geçiş hatası ve çözümleri |

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
│   ├── execution_model.md       var, varip, barstate — nasıl çalışır
│   ├── common_errors.md         max_bars_back, series type — yaygın hatalar
│   ├── timeframes.md            request.security, repainting — MTF
│   ├── colors_and_display.md    color.new, gradients — renk sistemi
│   ├── methods.md               user-defined methods — metodlar
│   ├── objects.md               UDT, type system — nesneler
│   └── signal_quality.md        Fakeout filters — volume, MTF, ATR, bar confirm
│
├── reference/
│   ├── variables.md             open, close, bar_index, syminfo
│   ├── constants.md             color.*, shape.*, plot.style_*
│   ├── types.md                 series, simple, input, const
│   ├── keywords.md              if, for, var, varip, switch
│   ├── annotations.md           @version, @param, @returns
│   └── functions/
│       ├── ta.md                RSI, EMA, MACD, ATR, crossover, pivot
│       ├── strategy.md          entry, exit, close, position_size
│       ├── drawing.md           plot, line, box, label, table, fill
│       ├── request.md           security, financial, MTF
│       ├── collections.md       array, map, matrix
│       └── general.md           math, str, input, alert, timestamp
│
├── writing_scripts/
│   ├── style_guide.md           Kod stili, isimlendirme, girintileme
│   ├── debugging.md             Pine Logs, debug teknikleri
│   ├── profiling_and_optimization.md  Performans optimizasyonu
│   └── limitations.md           Script limitleri, max_bars_back
│
├── examples/
│   ├── indicators/   (18 — copy-paste ready, tested in TradingView)
│   └── strategies/   (13 — copy-paste ready, tested in TradingView)
│
├── global-markets/   (22 — ES, NQ, BTC, ETH, Gold, Forex, DAX, Nikkei)
├── webhook-templates/ (7 — Telegram, Discord, JSON, VIOP)
└── v5-to-v6-migration/ (10 — full migration guide)
```

---

## 📜 Lisans / License

MIT — [LICENSE](LICENSE) · Copyright © 2025 [Ugur Pala](https://github.com/trugurpala)

**Yazar / Author:**
[TradingView](https://tr.tradingview.com/u/trugurpala/) · [X / Twitter](https://x.com/trugurpala) · mail@ugurpala.com

> TR: TradingView'ın resmi Pine Script v6 dokümantasyonu temel referans materyali olarak kullanılmıştır. TradingView bu projeyle hiçbir resmi bağlantısı veya onayı bulunmamaktadır.
>
> EN: The official TradingView Pine Script v6 documentation was used as primary reference material. TradingView is not affiliated with or endorsing this project.

---

<div align="center">

**TR: Bu repo işinize yaradıysa, bir yıldız vermek başkalarının bulmasını kolaylaştırır.**
**EN: If this repo saved you time, starring it helps others find it.**

⭐ **[Star this repo](https://github.com/trugurpala/pinescriptv6)** ⭐

[![Star History Chart](https://api.star-history.com/svg?repos=trugurpala/pinescriptv6&type=Date)](https://star-history.com/#trugurpala/pinescriptv6&Date)

</div>
