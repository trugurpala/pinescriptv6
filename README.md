# Pine Script v6 Reference

<div align="center">

![Pine Script](https://img.shields.io/badge/Pine%20Script-v6-1E88E5?style=for-the-badge&logo=tradingview&logoColor=white)
![TradingView](https://img.shields.io/badge/TradingView-Compatible-131722?style=for-the-badge&logo=tradingview)
![License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)
![Author](https://img.shields.io/badge/Author-Ugur%20Pala-F59E0B?style=for-the-badge)
![Stars](https://img.shields.io/github/stars/trugurpala/pinescriptv6?style=for-the-badge&color=yellow)
![Language](https://img.shields.io/badge/TR%20%7C%20EN-Bilingual-lightgrey?style=for-the-badge)

**TradingView Pine Script v6 — AI destekli geliştirme ortamı**
**TradingView Pine Script v6 — AI-assisted development reference**

Yapımcı / Author: [Ugur Pala](https://github.com/trugurpala) · mail@ugurpala.com

</div>

---

## 📺 Demo

> **XU030 BIST 30 Futures — EMA Cross**
> TR: Bu kod, repodaki referans dosyaları kullanılarak Claude ile yazıldı.
> EN: This code was written by Claude using the reference files in this repo.

![EMA Cross Demo on XU030](docs/demo_chart.png)

```pine
//@version=6
indicator("EMA Cross — pinescriptv6 demo", overlay=true)
fast = ta.ema(close, 9)
slow = ta.ema(close, 21)
plot(fast, "EMA 9",  color.green, 2)
plot(slow, "EMA 21", color.red,   2)
bgcolor(ta.crossover(fast, slow)  ? color.new(color.green, 90) :
        ta.crossunder(fast, slow) ? color.new(color.red,   90) : na)
```

---

## ⚙️ LESSONS_LEARNED Sistemi / System

![How LESSONS_LEARNED Works](docs/lessons_flow.png)

---

## TR | Türkçe

### Bu Repo Nedir?

TradingView'ın resmi Pine Script v6 dokümantasyonu temel kaynak alınarak,
yapay zeka destekli geliştirme için tasarlanmış bir bilgi tabanıdır.
Tüm içerik, sistem ve yapı **Uğur Pala** tarafından oluşturulmuştur.

| Özellik | Açıklama |
|---------|----------|
| `LESSONS_LEARNED.md` | AI her hata çözümünde buraya yazar. Sonraki oturumda önce okur, hatayı tekrar yapmaz. |
| `LLM_MANIFEST.md` | Hangi soruda hangi dosyanın okunacağını belirler. Tüm repo yerine sadece ilgili dosyayı çeker. |
| `SKILL.md` | AI'ın yazma protokolü. |

> Temel referans: TradingView Pine Script v6 resmi dokümantasyonu.
> TradingView bu projeyle hiçbir bağlantısı veya onayı bulunmamaktadır.

### 🚀 Hızlı Başlangıç

```bash
git clone https://github.com/trugurpala/pinescriptv6.git
```

---

### 🤖 Claude ile Kullanım

1. [Claude.ai](https://claude.ai) → Projects → Projeniz
2. **Files** → `+` → **GitHub** → yapıştır:
   ```
   https://github.com/trugurpala/pinescriptv6
   ```
3. Tüm dosyaları seç → **Add files**
4. Sohbette `/pinescript-v6` yaz → skill aktif

---

### ⌨️ Cursor ile Kullanım

Repoyu klonlayın — `.cursor/rules/pinescriptv6.mdc` otomatik yüklenir (Cursor v0.44+).
Eski sürümler için `.cursorrules` fallback olarak çalışır.

```bash
git clone https://github.com/trugurpala/pinescriptv6.git
cd pinescriptv6
# Cursor'ı bu klasörde açın — kurallar otomatik devreye girer
cursor .
```

Veya kod yazarken direkt referans edin:

| Görev | Dosya |
|-------|-------|
| İndikatör yazıyorum | `@reference/functions/ta.md` |
| Strateji yazıyorum | `@reference/functions/strategy.md` |
| Hata alıyorum | `@concepts/common_errors.md` |
| **Her şeyden önce** | `@LESSONS_LEARNED.md` |

---

### 🌊 Windsurf ile Kullanım

Repoyu klonlayın — `.windsurfrules` otomatik yüklenir.

```bash
git clone https://github.com/trugurpala/pinescriptv6.git
# Windsurf'ü bu klasörde açın
windsurf .
```

---

### 🐙 GitHub Copilot ile Kullanım

Repoyu klonlayın — `.github/copilot-instructions.md` otomatik devreye girer.
VS Code, JetBrains veya herhangi bir Copilot destekli editörde çalışır.

```bash
git clone https://github.com/trugurpala/pinescriptv6.git
# Editörünüzde bu klasörü açın — Copilot kuralları aktif olur
```

---

### 🤗 Diğer LLM'ler / Custom GPT

1. Repoyu ZIP olarak indirin
2. Custom GPT Knowledge veya RAG sisteminize yükleyin
3. Minimum yükleme önerisi:
   - `LLM_MANIFEST.md`
   - `LESSONS_LEARNED.md`
   - `reference/functions/` klasörü

---

## EN | English

### What is this?

A knowledge base purpose-built for AI-assisted Pine Script v6 development.
The official TradingView Pine Script v6 documentation is the primary source.
All content, system design and structure created by **Ugur Pala**.

| Feature | Description |
|---------|-------------|
| `LESSONS_LEARNED.md` | AI appends every solved error here. Next session reads it first — same mistake never repeated. |
| `LLM_MANIFEST.md` | Tells the AI which file to read for which query. Loads only relevant files, not the whole repo. |
| `SKILL.md` | AI's writing protocol. |

> Source: TradingView Pine Script v6 official documentation.
> TradingView is not affiliated with or endorsing this project.

### 🚀 Quick Start

```bash
git clone https://github.com/trugurpala/pinescriptv6.git
```

---

### 🤖 Use with Claude

1. [Claude.ai](https://claude.ai) → Projects → your project
2. **Files** → `+` → **GitHub** → paste:
   ```
   https://github.com/trugurpala/pinescriptv6
   ```
3. Select all files → **Add files**
4. Type `/pinescript-v6` in chat → skill active

---

### ⌨️ Use with Cursor

Clone the repo — `.cursor/rules/pinescriptv6.mdc` loads automatically (Cursor v0.44+).
`.cursorrules` works as fallback for older versions.

```bash
git clone https://github.com/trugurpala/pinescriptv6.git
cursor .
```

Or reference files directly in chat:

| Task | File |
|------|------|
| Writing an indicator | `@reference/functions/ta.md` |
| Writing a strategy | `@reference/functions/strategy.md` |
| Fixing an error | `@concepts/common_errors.md` |
| **Before anything** | `@LESSONS_LEARNED.md` |

---

### 🌊 Use with Windsurf

Clone the repo — `.windsurfrules` loads automatically.

```bash
git clone https://github.com/trugurpala/pinescriptv6.git
windsurf .
```

---

### 🐙 Use with GitHub Copilot

Clone the repo — `.github/copilot-instructions.md` activates automatically.
Works in VS Code, JetBrains, or any Copilot-enabled editor.

```bash
git clone https://github.com/trugurpala/pinescriptv6.git
# Open this folder in your editor — Copilot rules are active
```

---

### 🤗 Other LLMs / Custom GPT

1. Download the repo as ZIP
2. Upload to your Custom GPT Knowledge or RAG system
3. Recommended minimum upload:
   - `LLM_MANIFEST.md`
   - `LESSONS_LEARNED.md`
   - `reference/functions/` folder

---

## Dosya Yapısı / File Structure

```
pinescriptv6/
│
├── LESSONS_LEARNED.md      TR: Hata hafızası      EN: Auto-updated error log
├── SKILL.md                TR: AI yazma protokolü EN: AI writing protocol
├── LLM_MANIFEST.md         TR: Sorgu yönlendirme  EN: Query routing map
│
├── .cursor/
│   └── rules/
│       └── pinescriptv6.mdc   ← Cursor v0.44+
├── .cursorrules                ← Cursor (legacy)
├── .windsurfrules              ← Windsurf / Codeium
├── .github/
│   └── copilot-instructions.md ← GitHub Copilot
│
├── docs/
│   ├── demo_chart.png          ← XU030 demo
│   └── lessons_flow.png        ← System diagram
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
└── writing_scripts/
    ├── style_guide.md
    ├── debugging.md
    ├── profiling_and_optimization.md
    └── limitations.md
```

---

## Lisans / License

MIT — [LICENSE](LICENSE) dosyasına bakın.
Telif Hakkı / Copyright © 2025 [Ugur Pala](https://github.com/trugurpala) · mail@ugurpala.com

---

<div align="center">

⭐ TR: Bu repo işinize yaradıysa lütfen yıldız verin!
⭐ EN: If this repo saved you time, please give it a star!

[![Star History Chart](https://api.star-history.com/svg?repos=trugurpala/pinescriptv6&type=Date)](https://star-history.com/#trugurpala/pinescriptv6&Date)

</div>
