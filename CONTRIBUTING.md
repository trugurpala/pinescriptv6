# Contributing to pinescriptv6

Thank you for your interest in contributing!  
This project is maintained by **Uğur Pala** ([@trugurpala](https://github.com/trugurpala)) · mail@ugurpala.com

---

## Ways to Contribute

### 1. Add a Solved Error to LESSONS_LEARNED.md

This is the most valuable contribution. If you encountered and fixed a Pine Script v6 error:

```markdown
### [Short Error Title]
- **Error message:** Exact text from TradingView's error panel
- **Cause:** Why does it happen?
- **Fix:** How to resolve it
- **Example:**
```pine
//@version=6
// ❌ Wrong
...
// ✅ Correct
...
```
---
```

### 2. Improve a Reference File

Each file under `reference/` and `concepts/` covers a specific namespace.
If you find a missing function, incorrect signature, or a better example:

1. Fork the repo
2. Edit the relevant `.md` file
3. Open a pull request with a clear title and description

### 3. Add Examples

Practical, runnable examples are always welcome.
All code blocks must start with `//@version=6` and be tested in TradingView.

---

## File Conventions

- Use Markdown (`.md`) for all documentation
- Code blocks must use ```pine syntax highlighting
- Keep examples minimal and self-contained
- Do not add v5-only syntax
- Do not add untested or hallucinated function signatures

---

## Pull Request Guidelines

- One PR per topic / fix
- Clear commit messages: `docs: add ta.wma example` / `fix: correct strategy.exit signature`
- Reference the relevant file in your PR description

---

## Questions

Open an issue or reach out: **mail@ugurpala.com**
