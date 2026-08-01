# Custom GPT error-memory bridge

This compatibility path now points to the evidence-first generated pack:

- [`generated/custom-gpt/INSTRUCTIONS.md`](../../generated/custom-gpt/INSTRUCTIONS.md)
- [`generated/custom-gpt/KNOWLEDGE.md`](../../generated/custom-gpt/KNOWLEDGE.md)
- [`knowledge/lessons/`](../../knowledge/lessons/)
- [`verification/tradingview.json`](../../verification/tradingview.json)

Errors become active guidance only after sanitization, source registration,
scoped rule metadata, evidence classification, regression coverage, and
deterministic rendering. A local structural check is not a TradingView compilation
result.

Run:

```bash
python tools/psak.py validate
python tools/psak.py render --check
python tools/psak.py check
```
