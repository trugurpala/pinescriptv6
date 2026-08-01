# Source provenance

Pine Script Agent Kit separates where a claim came from, what the claim says,
where it applies, and what has actually been verified.

```text
Official source registry -> scoped catalog rule -> decision register
-> validator -> renderer -> host adapter -> AI answer
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

## 3. Decision register

`governance/decisions.json` records durable project choices using four
dispositions: `adopt`, `adapt`, `reference`, and `reject`. Each decision names
its source references, implementation references, rationale, date, and user
impact. The register is validated with the rest of the canonical data.

Read [Decision policy](decision-policy.md) before turning a new idea, source, or
adapter behavior into public guidance.

## 4. Evidence boundary

- `official`: current official documentation supports the scoped claim;
- `tradingview-verified`: a dated manual record matches the file SHA-256;
- `structural-only`: local checks confirm repository structure, not compilation;
- `unverified`: excluded from generated guidance.

Changing a Pine file invalidates a manual record whose stored hash no longer
matches. Network link checking is separate from offline validation. An unavailable
source is reported for review rather than silently deleting guidance.

## 5. Deterministic adapters

`agents/protocol.md`, host templates in `adapters/`, and active distributable
rules produce every AI surface. `python tools/psak.py render --check` fails if a
committed output differs, so hand-edited drift cannot masquerade as canonical
knowledge.

## 6. Example inventory

`examples/manifest.json` covers every tracked `.pine` file, even outside the
`examples/` directory. Each record includes path, hash, evidence, check date,
optional TradingView record, and limitations. The current inventory is
`structural-only` for all 56 files.

## 7. Updating a claim

1. Register or refresh the official source and access date.
2. Narrow the claim, scope, and exceptions.
3. Decide whether the idea should be adopted, adapted, referenced, or rejected.
4. Add a human explanation and a failing regression test.
5. Validate, render, and confirm no generated drift.
6. Update public documentation when behavior or status changes.
7. Keep local, tested, pushed, released, and live states separate.

This project references official documentation; it does not republish the Pine
manual. It is independent and is not affiliated with or endorsed by TradingView.
