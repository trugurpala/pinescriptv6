# Lessons learned compatibility bridge

Active, source-linked lessons now live in `knowledge/lessons/`; enforceable claims
live in `knowledge/catalog.json`. The first migrated lesson is
[`knowledge/lessons/stale-absolutes.md`](knowledge/lessons/stale-absolutes.md).

A lesson becomes distributed agent guidance only after it has:

1. a sanitized failure or official source;
2. a stable rule ID;
3. a scoped claim with exceptions;
4. an evidence level and verification date;
5. a regression test;
6. deterministic regenerated adapters.

Never store customer scripts, credentials, private prompts, or personal data in a
lesson. A local structural check is not a TradingView compilation result.
