# Pine Script v6 Reference

<div align="center">

![Pine Script](https://img.shields.io/badge/Pine%20Script-v6-1E88E5?style=for-the-badge&logo=tradingview&logoColor=white)
![TradingView](https://img.shields.io/badge/TradingView-Compatible-131722?style=for-the-badge&logo=tradingview)
![License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)
![Author](https://img.shields.io/badge/Author-Ugur%20Pala-F59E0B?style=for-the-badge)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-8B5CF6?style=for-the-badge)
![Language](https://img.shields.io/badge/Dil%20%2F%20Language-TR%20%7C%20EN-lightgrey?style=for-the-badge)

**TradingView Pine Script v6 — AI destekli geliştirme ortamı**
**TradingView Pine Script v6 — AI-assisted development reference**

Tasarım ve geliştirme / Designed & built by [Ugur Pala](https://github.com/trugurpala) · mail@ugurpala.com

</div>

---

## TR | Türkçe

### Bu Repo Nedir?

Bu repo; TradingView'ın resmi Pine Script v6 dokümantasyonunu temel kaynak alarak,
yapay zeka destekli geliştirme için baştan tasarlanmış özgün bir bilgi tabanıdır.

Tüm içerik, sistem tasarımı ve yapı **Uğur Pala** tarafından oluşturulmuştur.

Bu repoya özgü sistem:

- **LESSONS_LEARNED.md** — AI her hata çözümünde buraya yazar. Bir dahaki oturumda önce bunu okur, aynı hatayı bir daha yapmaz.
- **LLM_MANIFEST.md** — Hangi soruda hangi dosyanın okunacağını belirleyen yönlendirme haritası. Tüm repoyu bağlam penceresine yüklemek yerine yalnızca ilgili dosyayı çeker.
- **SKILL.md** — AI'ın bu repodaki yazma protokolü.
- **Claude / Cursor / Windsurf / Copilot entegrasyonu** — Kutu açılır açılmaz çalışır.

> **Kaynak notu:** Temel referans materyali olarak TradingView'ın resmi Pine Script v6
> dokümantasyonundan yararlanılmıştır. TradingView bu projeyle hiçbir bağlantısı veya
> onayı bulunmamaktadır.

### Hızlı Başlangıç

```bash
git clone https://github.com/trugurpala/pinescriptv6.git
```

### Claude Projects ile Kullanım

1. [Claude.ai](https://claude.ai) → Projects → Projeniz
2. Files → **+** → GitHub → Yapıştır:
   `https://github.com/trugurpala/pinescriptv6`
3. Tüm dosyaları seç → **Add files**
4. Sohbette `/pinescript-v6` yazarak skill'i aktifleştir

### Cursor / Windsurf / Copilot ile Kullanım

Repoyu klonlayın — `.cursorrules` ve `.github/copilot-instructions.md` otomatik devreye girer.

| Görev | Dosya |
|-------|-------|
| İndikatör yazıyorum | `@reference/functions/ta.md` + `@reference/functions/drawing.md` |
| Strateji yazıyorum | `@reference/functions/strategy.md` |
| Çoklu zaman dilimi | `@reference/functions/request.md` |
| Hata alıyorum | `@concepts/common_errors.md` |
| **Her şeyden önce** | `@LESSONS_LEARNED.md` |

### LESSONS_LEARNED Nasıl Çalışır?

Bu repoya özgü ve en değerli özelliği.

AI bir Pine Script v6 hatasını çözdüğünde:
1. Hata, sebebi ve çözümü belgelenir
2. **`LESSONS_LEARNED.md` bu repoda otomatik güncellenir**
3. Sonraki oturumda AI kod yazmadan önce bunu okur
4. Aynı hata bir daha yapılmaz

Zaman içinde bu dosya gerçek dünya hatalarından oluşan, büyüyen bir bilgi tabanına dönüşür.

### Lisans

MIT — detaylar için [LICENSE](LICENSE) dosyasına bakın.
Telif Hakkı © 2025 [Uğur Pala](https://github.com/trugurpala) · mail@ugurpala.com

---

## EN | English

### What is this?

This repository takes the official TradingView Pine Script v6 documentation as its
primary source and builds an original, purpose-built knowledge base for AI-assisted development.

All content, system design, and structure were created by **Ugur Pala**.

What makes this repo unique:

- **LESSONS_LEARNED.md** — The AI appends every solved error here. Next session it reads this first and never repeats the same mistake.
- **LLM_MANIFEST.md** — A routing map that tells the AI which file to read for which query, instead of loading the entire repo into the context window.
- **SKILL.md** — The AI's writing protocol for this codebase.
- **Claude / Cursor / Windsurf / Copilot integration** — Works out of the box.

> **Source note:** The official TradingView Pine Script v6 documentation was used as the
> primary reference material. TradingView is not affiliated with or endorsing this project.

### Quick Start

```bash
git clone https://github.com/trugurpala/pinescriptv6.git
```

### Use with Claude Projects

1. [Claude.ai](https://claude.ai) → Projects → your project
2. Files → **+** → GitHub → paste:
   `https://github.com/trugurpala/pinescriptv6`
3. Select all files → **Add files**
4. Type `/pinescript-v6` in chat to activate the skill

### Use with Cursor / Windsurf / Copilot

Clone the repo — `.cursorrules` and `.github/copilot-instructions.md` are picked up automatically.

| Task | File |
|------|------|
| Writing an indicator | `@reference/functions/ta.md` + `@reference/functions/drawing.md` |
| Writing a strategy | `@reference/functions/strategy.md` |
| Multi-timeframe data | `@reference/functions/request.md` |
| Fixing an error | `@concepts/common_errors.md` |
| **Before anything** | `@LESSONS_LEARNED.md` |

### How LESSONS_LEARNED Works

The core and most unique feature of this repo.

When the AI solves a Pine Script v6 error:
1. The error, cause, and fix are documented
2. **`LESSONS_LEARNED.md` is automatically updated in this repo**
3. Next session: the AI reads it before writing any code
4. The same mistake is never made twice

Over time this becomes a living, growing knowledge base of real-world errors and solutions.

### File Structure

```
pinescriptv6/
├── LESSONS_LEARNED.md          TR: Hata hafızası / EN: Auto-updated error log
├── SKILL.md                    TR: AI yazma protokolü / EN: AI writing protocol
├── LLM_MANIFEST.md             TR: Sorgu yönlendirme / EN: Query routing map
├── concepts/
│   ├── execution_model.md
│   ├── common_errors.md
│   ├── timeframes.md
│   ├── colors_and_display.md
│   ├── methods.md
│   └── objects.md
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
└── writing_scripts/
    ├── style_guide.md
    ├── debugging.md
    ├── profiling_and_optimization.md
    └── limitations.md
```

### License

MIT — see [LICENSE](LICENSE) for details.
Copyright © 2025 [Ugur Pala](https://github.com/trugurpala) · mail@ugurpala.com
