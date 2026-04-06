# Pine Script v6 — Agent Instructions
> Author: Ugur Pala · mail@ugurpala.com · github.com/trugurpala/pinescriptv6

TR: Bu dosya Devin, OpenAI Codex ve diğer otonom AI agent sistemleri tarafından okunur.
EN: This file is read by Devin, OpenAI Codex, and other autonomous AI agent systems.

---

## Task Protocol / Görev Protokolü

**Step 1 — Read before acting / Yazmadan önce oku:**
```
LESSONS_LEARNED.md   → known errors / bilinen hatalar
LLM_MANIFEST.md      → routing map / yönlendirme haritası
```

**Step 2 — Find the right reference / Doğru referansı bul:**
Use `LLM_MANIFEST.md` to identify which file to read for the task.
`LLM_MANIFEST.md` kullanarak göreve uygun dosyayı belirle.

**Step 3 — Write / Yaz:**
Every Pine Script v6 script starts with `//@version=6`.

**Step 4 — On error / Hata olunca:**
1. Solve the error
2. Append to `LESSONS_LEARNED.md` using the format in that file

---

## What This Repo Contains / Bu Repoda Ne Var

```
LESSONS_LEARNED.md        Error memory / Hata hafızası
LLM_MANIFEST.md           Query routing / Sorgu yönlendirme
reference/                v6 API reference (ta, strategy, drawing, request...)
concepts/                 Core concepts (execution model, timeframes, errors)
writing_scripts/          Style, debug, optimization, limits
examples/indicators/      17 ready-to-use indicators
examples/strategies/      12 ready-to-use strategies
webhook-templates/        Telegram, Discord, JSON webhook templates
v5-to-v6-migration/       v5 → v6 migration guide (10 files)
```

---

## Non-Negotiable Rules / Kesinlikle Uyulacak Kurallar

1. Every script: `//@version=6` — first line, no exceptions
2. Never use: `study()`, `security()`, bare `input()` — these are v5
3. Never invent function names not in the reference docs
4. After solving any error: update `LESSONS_LEARNED.md`
5. Use `ta.*` functions — never reimplement them manually

---

## Source Note / Kaynak Notu

> TR: TradingView resmi Pine Script v6 dokümantasyonu temel referans materyalidir.
> TradingView bu projeyle hiçbir bağlantısı bulunmamaktadır.
>
> EN: TradingView official Pine Script v6 documentation is the primary reference.
> TradingView is not affiliated with this project.
