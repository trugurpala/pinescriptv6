# Pine Script v6 Reference

<div align="center">

![Pine Script](https://img.shields.io/badge/Pine%20Script-v6-1E88E5?style=for-the-badge&logo=tradingview&logoColor=white)
![TradingView](https://img.shields.io/badge/TradingView-Compatible-131722?style=for-the-badge&logo=tradingview)
![License](https://img.shields.io/badge/License-MIT-22C55E?style=for-the-badge)
![Maintained](https://img.shields.io/badge/Maintained%20by-Uğur%20Pala-F59E0B?style=for-the-badge)
![Contributions](https://img.shields.io/badge/Contributions-Welcome-8B5CF6?style=for-the-badge)

**A complete Pine Script v6 reference, restructured for AI-assisted development.**  
Built by [Uğur Pala](https://github.com/trugurpala) · Includes an auto-updating error memory system via `LESSONS_LEARNED.md`

[Quick Start](#quick-start) · [File Structure](#file-structure) · [Use with Cursor / Windsurf](#use-with-cursor--windsurf--copilot) · [Use with Claude](#use-with-claude-projects) · [Contributing](#contributing) · [License](#license)

</div>

---

## What is this?

This repository contains the TradingView Pine Script v6 documentation,
restructured for use as an AI knowledge base (RAG — Retrieval Augmented Generation).

**Created and maintained by [Uğur Pala](https://github.com/trugurpala) · mail@ugurpala.com**

Key features:
- **Complete v6 reference** — ta.*, strategy.*, drawing, request, collections, math/string/input
- **LESSONS_LEARNED.md** — auto-updated by Claude when it solves errors, preventing repetition
- **LLM_MANIFEST.md** — routing map so the AI fetches only the relevant file per query
- **SKILL.md** — the AI's writing protocol for this codebase
- Open to the community — use it with Claude, Cursor, Windsurf, GitHub Copilot, or any AI editor

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

Clone the repo and reference files directly in your AI chat:

| Task | Reference file |
|------|---------------|
| Building an indicator | `@reference/functions/ta.md` + `@reference/functions/drawing.md` |
| Building a strategy | `@reference/functions/strategy.md` |
| Multi-timeframe data | `@reference/functions/request.md` |
| Getting an error | `@concepts/common_errors.md` |
| Before writing any code | `@LESSONS_LEARNED.md` (always first) |

Or add the whole repo as context in your `.cursorrules` / `copilot-instructions.md`:

```
Always check LESSONS_LEARNED.md before writing Pine Script v6 code.
Use LLM_MANIFEST.md to find the correct reference file for the task.
All scripts must start with //@version=6.
```

---

## Use with Custom GPTs / Other LLMs

1. Download this repo as a ZIP
2. Upload the relevant files to your Custom GPT Knowledge or any RAG system
3. Recommended minimum upload: `LLM_MANIFEST.md` + `LESSONS_LEARNED.md` + the `reference/functions/` folder

---

## File Structure

```
pinescriptv6/
│
├── LESSONS_LEARNED.md          ← Auto-updated error log (AI writes here on every fix)
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
    ├── style_guide.md          ← Naming, ordering, comment conventions
    ├── debugging.md            ← Pine Logs, plot debug, table panels
    ├── profiling_and_optimization.md
    └── limitations.md          ← Drawing limits, request limits, buffer limits
```

---

## How LESSONS_LEARNED Works

When an AI using this repo solves a Pine Script v6 error:

1. The error and its fix are documented
2. **`LESSONS_LEARNED.md` is updated automatically**
3. Next session: the AI reads it first
4. The same mistake is never repeated

This is the core feature of this repo — a living, growing error log that makes the AI smarter over time.

---

## Credits

| Contribution | Author |
|---|---|
| Original Pine Script v6 documentation | [TradingView](https://www.tradingview.com/pine-script-docs/) |
| v6 RAG restructuring & chunking | [codenamdevan](https://github.com/codenamedevan/pinescriptv6) |
| Ownership, Turkish adaptation, LESSONS_LEARNED system, SKILL protocol, community release | [Uğur Pala](https://github.com/trugurpala) · mail@ugurpala.com |

---

## Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## License

MIT — see [LICENSE](LICENSE) for details.  
Copyright © 2025 [Uğur Pala](https://github.com/trugurpala)
