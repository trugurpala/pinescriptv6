# Pine Script v6 Reference

<div align="center">

![Pine Script](https://img.shields.io/badge/Pine%20Script-v6-1E88E5?style=for-the-badge&logo=tradingview&logoColor=white)
![TradingView](https://img.shields.io/badge/TradingView-Compatible-131722?style=for-the-badge&logo=tradingview)
![License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)
![Author](https://img.shields.io/badge/Author-Uğur%20Pala-F59E0B?style=for-the-badge)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-8B5CF6?style=for-the-badge)

**A complete Pine Script v6 reference, hand-built for AI-assisted development.**
Created by [Uğur Pala](https://github.com/trugurpala) · mail@ugurpala.com

[Quick Start](#quick-start) · [Use with Cursor / Windsurf](#use-with-cursor--windsurf--copilot) · [Use with Claude](#use-with-claude-projects) · [File Structure](#file-structure) · [Contributing](#contributing)

</div>

---

## What is this?

Every file in this repository was written from scratch by **Uğur Pala**, purpose-built for AI-assisted Pine Script v6 development.

The primary source is the official TradingView Pine Script v6 documentation — hand-translated, restructured, and optimised as an AI knowledge base (RAG).

On top of the reference material, this repo adds a unique system:

- **LESSONS_LEARNED.md** — the AI writes here every time it solves an error. Next session it reads this first and never repeats the same mistake.
- **LLM_MANIFEST.md** — a routing map so the AI fetches only the relevant file per query, not the whole repo.
- **SKILL.md** — the AI's writing protocol: check errors first, find the right reference, write clean v6 code.
- **Claude Project integration** — works out of the box with Claude.ai Projects.
- **Cursor / Windsurf / Copilot** — `.cursorrules` and `.github/copilot-instructions.md` included.

---

## Quick Start

```bash
git clone https://github.com/trugurpala/pinescriptv6.git
```

---

## Use with Claude Projects

1. Open [Claude.ai](https://claude.ai) → Projects → your project
2. Files → **+** → GitHub → paste:
   ```
   https://github.com/trugurpala/pinescriptv6
   ```
3. Select all files → **Add files**
4. In chat, type `/pinescript-v6` to activate the skill

---

## Use with Cursor / Windsurf / Copilot

Clone the repo — `.cursorrules` and `.github/copilot-instructions.md` are picked up automatically.

Or reference files directly:

| Task | File to reference |
|------|------------------|
| Writing an indicator | `@reference/functions/ta.md` + `@reference/functions/drawing.md` |
| Writing a strategy | `@reference/functions/strategy.md` |
| Multi-timeframe data | `@reference/functions/request.md` |
| Fixing an error | `@concepts/common_errors.md` |
| **Before anything** | `@LESSONS_LEARNED.md` — always read this first |

---

## Use with Custom GPTs or Other LLMs

1. Download this repo as a ZIP
2. Upload to your Custom GPT Knowledge or RAG pipeline
3. Recommended minimum: `LLM_MANIFEST.md` + `LESSONS_LEARNED.md` + `reference/functions/`

---

## File Structure

```
pinescriptv6/
│
├── LESSONS_LEARNED.md          ← Auto-updated error log (AI appends here on every fix)
├── SKILL.md                    ← AI writing protocol for this repo
├── LLM_MANIFEST.md             ← Query routing map — which file to read for which task
│
├── concepts/
│   ├── execution_model.md      ← Bar-by-bar model, var/varip, barstate
│   ├── common_errors.md        ← max_bars_back, series type errors, repainting
│   ├── timeframes.md           ← Multi-timeframe, request.security, repainting
│   ├── colors_and_display.md   ← color.new, from_gradient, bgcolor
│   ├── methods.md              ← User-defined methods
│   └── objects.md              ← UDT, type system
│
├── reference/
│   ├── variables.md            ← open, close, high, low, bar_index, syminfo.*
│   ├── constants.md            ← color.*, shape.*, plot.style_*, size.*
│   ├── types.md                ← int, float, bool, series, simple, input
│   ├── keywords.md             ← if, for, while, var, varip, switch, export
│   ├── annotations.md          ← @version, @param, @returns, @type
│   └── functions/
│       ├── ta.md               ← RSI, EMA, SMA, MACD, ATR, BB, crossover, pivot
│       ├── strategy.md         ← entry, exit, close, position_size, equity
│       ├── drawing.md          ← plot, line, box, label, table, fill
│       ├── request.md          ← request.security, financial, currency_rate
│       ├── collections.md      ← array, map, matrix
│       └── general.md          ← math, str, input, alert, timestamp
│
└── writing_scripts/
    ├── style_guide.md
    ├── debugging.md
    ├── profiling_and_optimization.md
    └── limitations.md
```

---

## How LESSONS_LEARNED Works

This is the core feature of this repo.

Every time an AI using this repo encounters and fixes a Pine Script v6 error:

1. The error, cause, and fix are documented
2. **`LESSONS_LEARNED.md` is updated in this repo automatically**
3. Next session: the AI reads it before writing any code
4. The same mistake is never made twice

Over time, this file becomes a personal, growing knowledge base of real-world Pine Script v6 errors and solutions.

---

## License

MIT — see [LICENSE](LICENSE) for details.
Copyright © 2025 [Uğur Pala](https://github.com/trugurpala) · mail@ugurpala.com
