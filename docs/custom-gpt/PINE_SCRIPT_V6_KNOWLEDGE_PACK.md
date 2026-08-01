# Custom GPT knowledge-pack bridge

This path is preserved for existing links, but its former bundled snapshot is no
longer an active knowledge source. It duplicated repository content and contained
Pine claims that became stale.

Use the deterministic current pack instead:

- [`generated/custom-gpt/INSTRUCTIONS.md`](../../generated/custom-gpt/INSTRUCTIONS.md)
- [`generated/custom-gpt/KNOWLEDGE.md`](../../generated/custom-gpt/KNOWLEDGE.md)
- [`knowledge/catalog.json`](../../knowledge/catalog.json)
- [`knowledge/sources.json`](../../knowledge/sources.json)

Regenerate and verify it with:

```bash
python tools/psak.py render
python tools/psak.py render --check
python tools/psak.py check
```

This project is independent and is not affiliated with or endorsed by TradingView.
