# Source provenance

Pine Script Agent Kit separates where a claim came from, what the claim says,
where it applies, and what has actually been verified.

```text
Official source registry -> scoped catalog rule -> validator -> renderer
-> host adapter -> AI answer
                     |
                     +-> structural/manual evidence label
```

## 1. Source registry

`knowledge/sources.json` stores a stable source ID, title, HTTPS URL, publisher,
source kind, access date, Pine applicability, and precise locator. Official
TradingView documentation, release notes, and the v6 reference are authoritative.
Community posts can start research but cannot activate a rule by themselves.

## 2. Scoped rules

`knowledge/catalog.json` stores a stable ID, claim, rationale, scope, exceptions,
source IDs, evidence level, verification date, status, explanation path, and tags.
IDs are sorted deterministically and are not reused for a different claim.

The validator rejects unknown sources, missing bodies, invalid dates/evidence,
active unverified rules, conflicting active values, and absolute language without
scope and exceptions.

## 3. Evidence boundary

- `official`: current official documentation supports the scoped claim;
- `tradingview-verified`: a dated manual record matches the file SHA-256;
- `structural-only`: local checks confirm repository structure, not compilation;
- `unverified`: excluded from generated guidance.

Changing a Pine file invalidates a manual record whose stored hash no longer
matches. Network link checking is separate from offline validation. An unavailable
source is reported for review rather than silently deleting guidance.

## 4. Deterministic adapters

`agents/protocol.md`, host templates in `adapters/`, and active distributable
rules produce every AI surface. `python tools/psak.py render --check` fails if a
committed output differs, so hand-edited drift cannot masquerade as canonical
knowledge.

## 5. Example inventory

`examples/manifest.json` covers every tracked `.pine` file, even outside the
`examples/` directory. Each record includes path, hash, evidence, check date,
optional TradingView record, and limitations. The current inventory is
`structural-only` for all 56 files.

## 6. Updating a claim

1. Register or refresh the official source and access date.
2. Narrow the claim, scope, and exceptions.
3. Add a human explanation and a failing regression test.
4. Validate, render, and confirm no generated drift.
5. Update public documentation when behavior or status changes.
6. Keep local, tested, pushed, released, and live states separate.

This project references official documentation; it does not republish the Pine
manual. It is independent and is not affiliated with or endorsed by TradingView.
