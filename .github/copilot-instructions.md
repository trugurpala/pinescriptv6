# Pine Script v6 — GitHub Copilot Instructions
# Maintained by Ugur Pala — mail@ugurpala.com
# github.com/trugurpala/pinescriptv6

You are assisting with Pine Script v6 development.

## Before writing code
- Always check LESSONS_LEARNED.md first
- Use LLM_MANIFEST.md to find the relevant reference file
- Read that file before writing

## Hard rules
- Every Pine Script must start with //@version=6
- Use ta.* functions, never reimplement them manually
- Never invent function signatures — only use what is in the reference files
- No Pine Script v5 syntax

## On error
- Solve the error
- Append the fix to LESSONS_LEARNED.md (message / cause / fix / example)
