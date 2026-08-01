# Contributing

Pine Script Agent Kit is free, open, community-built work. Contributions are
welcome when their confidence matches their evidence.

## Before opening a change

1. Read `agents/protocol.md` and `docs/provenance.md`.
2. Find or register the official source in `knowledge/sources.json`.
3. Give each new rule a stable `PSAK-*` ID, narrow claim, rationale, scope,
   exceptions, source IDs, evidence level, verification date, body, and tags.
4. Add a failing regression test before validator or renderer behavior changes.
5. Run the renderer instead of hand-editing generated instruction files.
6. Report Pine examples honestly: local static success is `structural-only`.
7. Use `docs/tradingview-manual-verification.md` before claiming
   `tradingview-verified` evidence.

Community material can suggest research, but an active distributed rule needs
official or hash-bound manual evidence. Sanitize compiler errors; do not submit
customer code, credentials, personal data, or private prompts.

## Pine examples

Every `.pine` file needs:

- `//@version=6` as its first line;
- an entry in `examples/manifest.json`;
- a truthful evidence level and limitations;
- a new hash-bound record if TradingView verification is claimed;
- explanation of repaint, strategy, timeframe, data, or webhook limitations when
  they are relevant.

No profitability, security, compatibility, or “non-repainting” claim is accepted
without evidence that supports that exact scope.

## Local checks

```bash
python -m unittest discover -s tests -v
python tools/psak.py validate
python tools/psak.py render
python tools/psak.py render --check
python tools/psak.py check
python tools/psak.py links
```

The link command uses the network and can be reported as not verified when access
is unavailable. The remaining commands are offline.

## Pull requests

Explain the problem, source/evidence change, affected rule/example IDs, test
results, and user-visible documentation impact. Keep unrelated formatting and
refactors out of the change. Never include a real secret.

Sensitive vulnerabilities follow [SECURITY.md](SECURITY.md), not the public issue
tracker. General proposals may use [GitHub Discussions](https://github.com/trugurpala/pinescriptv6/discussions).
