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

[Hızlı Başlangıç / Quick Start](#-hızlı-başlangıç--quick-start) ·
[Editör Entegrasyonu / Editor Setup](#-editör-entegrasyonu--editor-setup) ·
[Nasıl Çalışır / How It Works](#-nasıl-çalışır--how-it-works) ·
[Katkı / Contributing](CONTRIBUTING.md)

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
| 1 | Kodu yazmadan önce `LESSONS_LEARNED.md` okunur | `LESSONS_LEARNED.md` is read before writing |
| 2 | `LLM_MANIFEST.md` ile doğru referans dosyası bulunur | Correct reference file is found via `LLM_MANIFEST.md` |
| 3 | Temiz, v6 uyumlu kod yazılır | Clean, v6-compliant code is written |
| 4 | Hata oluşursa çözülür ve **otomatik kaydedilir** | On error: solved and **auto-saved** to `LESSONS_LEARNED.md` |
| 5 | Sonraki oturumda aynı hata bir daha yapılmaz | Next session: same mistake never repeated |

---

## 🚀 Hızlı Başlangıç / Quick Start

```bash
git clone https://github.com/trugurpala/pinescriptv6.git
```

---

## 🔌 Editör Entegrasyonu / Editor Setup

### Claude Projects

```
1. Claude.ai → Projects → projeniz / your project
2. Files → + → GitHub → yapıştır / paste:
   https://github.com/trugurpala/pinescriptv6
3. Tüm dosyaları seç / Select all → Add files
4. Sohbette / In chat: /pinescript-v6
```

### Cursor / Windsurf

TR: Repoyu klonlayın. `.cursorrules` ve `.windsurfrules` otomatik yüklenir.
EN: Clone the repo. `.cursorrules` and `.windsurfrules` load automatically.

```bash
git clone https://github.com/trugurpala/pinescriptv6.git
# Cursor veya Windsurf ile klasörü açın / Open the folder in Cursor or Windsurf
```

### GitHub Copilot

TR: `.github/copilot-instructions.md` dosyası otomatik devreye girer.
EN: `.github/copilot-instructions.md` is picked up automatically.

### Custom GPT / Diğer LLM'ler / Other LLMs

TR: Repoyu ZIP olarak indirin. `LLM_MANIFEST.md` + `LESSONS_LEARNED.md` + `reference/functions/` klasörünü yükleyin.
EN: Download as ZIP. Upload `LLM_MANIFEST.md` + `LESSONS_LEARNED.md` + `reference/functions/` folder.

---

## 📁 Dosya Yapısı / File Structure

```
pinescriptv6/
│
├── LESSONS_LEARNED.md        TR: Hata hafızası (AI otomatik günceller)
│                             EN: Error memory (AI auto-updates)
├── LLM_MANIFEST.md           TR: Sorgu yönlendirme haritası
│                             EN: Query routing map
├── SKILL.md                  TR: AI yazma protokolü
│                             EN: AI writing protocol
│
├── assets/
│   ├── demo_chart.png        TR: XU030 canlı demo ekranı
│   │                         EN: XU030 live demo screenshot
│   └── lessons_flow.png      TR: Sistem akış diyagramı
│                             EN: System flow diagram
│
├── .cursorrules              → Cursor / Windsurf
├── .windsurfrules            → Windsurf (dedicated)
├── .github/
│   └── copilot-instructions.md → GitHub Copilot
│
├── concepts/
│   ├── execution_model.md    var / varip / barstate
│   ├── common_errors.md      max_bars_back, series type
│   ├── timeframes.md         request.security, repainting
│   ├── colors_and_display.md color.new, gradients
│   ├── methods.md            user-defined methods
│   └── objects.md            UDT, type system
│
├── reference/
│   ├── variables.md          open, close, bar_index, syminfo
│   ├── constants.md          color.*, shape.*, plot.style_*
│   ├── types.md              series, simple, input, const
│   ├── keywords.md           if, for, var, varip, switch
│   ├── annotations.md        @version, @param, @returns
│   └── functions/
│       ├── ta.md             RSI, EMA, MACD, ATR, crossover
│       ├── strategy.md       entry, exit, close, position
│       ├── drawing.md        plot, line, box, label, table
│       ├── request.md        security, financial, MTF
│       ├── collections.md    array, map, matrix
│       └── general.md        math, str, input, alert
│
└── writing_scripts/
    ├── style_guide.md
    ├── debugging.md
    ├── profiling_and_optimization.md
    └── limitations.md
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
