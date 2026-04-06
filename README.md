# Pine Script v6 Reference

<div align="center">

![Pine Script](https://img.shields.io/badge/Pine%20Script-v6-blue?style=for-the-badge&logo=tradingview&logoColor=white)
![TradingView](https://img.shields.io/badge/TradingView-Indicator%20%26%20Strategy-131722?style=for-the-badge&logo=tradingview)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Maintained](https://img.shields.io/badge/Maintained-Yes-brightgreen?style=for-the-badge)

**A comprehensive Pine Script v6 reference optimised for AI-assisted development.**
Built for use with Claude AI — includes an auto-updating error memory system.

[Getting Started](#getting-started) · [File Structure](#file-structure) · [Contributing](#contributing) · [License](#license)

</div>

---

## What is this?

This repository contains the official TradingView Pine Script v6 documentation,
restructured and optimised for use as an AI knowledge base (RAG).

Key features:
- **Complete v6 reference** — ta.*, strategy.*, drawing, request, collections, math
- **LESSONS_LEARNED.md** — Claude automatically appends solved errors here, preventing repetition
- **LLM_MANIFEST.md** — routing map so Claude fetches only the relevant file per query
- **SKILL.md** — Claude's writing protocol for this repo
- **Turkish-adapted** — descriptions written for the Turkish VIOP/BIST30 trading context

---

## Getting Started

### Use with Claude Projects

1. Open [Claude.ai](https://claude.ai) → Projects → your project
2. Files → **+** → GitHub → paste this repo URL:
   ```
   https://github.com/trugurpala/pinescriptv6
   ```
3. Select all files → **Add files**
4. In your conversation, trigger the skill with `/pinescript-v6`

### Use with Cursor / Windsurf / Copilot

```bash
git clone https://github.com/trugurpala/pinescriptv6.git
```

Reference files directly in your AI chat:
- Building an indicator? → `@reference/functions/ta.md` + `@reference/functions/drawing.md`
- Building a strategy? → `@reference/functions/strategy.md`
- Getting errors? → `@concepts/common_errors.md`
- Always first → `@LESSONS_LEARNED.md`

---

## File Structure

```
pinescriptv6/
│
├── LESSONS_LEARNED.md          ← Auto-updated error log (Claude writes here)
├── SKILL.md                    ← Claude's Pine Script v6 writing protocol
├── LLM_MANIFEST.md             ← Query routing map for AI retrieval
│
├── concepts/
│   ├── execution_model.md      ← Bar-by-bar model, var/varip, barstate
│   ├── common_errors.md        ← max_bars_back, series type, repainting fixes
│   ├── timeframes.md           ← Multi-timeframe, request.security, repainting
│   ├── colors_and_display.md   ← color.new, from_gradient, bgcolor
│   ├── methods.md              ← User-defined methods
│   └── objects.md              ← UDT, type system
│
├── reference/
│   ├── variables.md            ← open, close, high, low, bar_index, syminfo
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
    ├── style_guide.md          ← Naming conventions, ordering, comments
    ├── debugging.md            ← Pine Logs, plot debug, table panels
    ├── profiling_and_optimization.md
    └── limitations.md          ← Drawing limits, request limits, buffer limits
```

---

## How the Error Memory Works

When Claude solves a Pine Script v6 error while using this repo as context:

1. Claude identifies the error and its fix
2. Claude **automatically updates `LESSONS_LEARNED.md`** in this repo
3. On the next session, Claude reads `LESSONS_LEARNED.md` first
4. The same error is never made twice

---

## Credits

| Contribution | Author |
|---|---|
| Original Pine Script v6 documentation | TradingView |
| v6 restructuring & RAG chunking | [codenamdevan](https://github.com/codenamedevan/pinescriptv6) |
| Turkish adaptation, LESSONS_LEARNED system, SKILL protocol | [Uğur Pala](https://github.com/trugurpala) |

---

## License

MIT — see [LICENSE](LICENSE) for details.
