# Pine Script v6 — GitHub Copilot Instructions
# Repo: github.com/trugurpala/pinescriptv6
# Maintainer: Ugur Pala · mail@ugurpala.com

## Protocol
1. Read LESSONS_LEARNED.md before writing any Pine Script v6 code
2. Use LLM_MANIFEST.md to find the correct reference file
3. Read that file, then write

## Hard Rules
- Every script must start with //@version=6
- Use ta.* functions — never reimplement manually
- Never invent function signatures not found in the reference files
- No Pine Script v5 syntax

## On Error
Append fix to LESSONS_LEARNED.md:
error · cause · fix · minimal //@version=6 example
