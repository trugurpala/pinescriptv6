# Evidence-first operating protocol

You are working with Pine Script v6. Treat `knowledge/catalog.json` as the
canonical rule index and `knowledge/sources.json` as the canonical source index.

1. Establish the user's indicator, strategy, library, migration, or review intent.
2. Establish timeframe relationships, repaint expectations, strategy execution
   semantics, data availability, and alert/webhook risk before choosing a pattern.
3. Apply only rules whose scope matches. Preserve each rule's exceptions.
4. Cite the registered official source ID when behavior depends on Pine semantics.
5. Label local static results `structural-only`. Do not describe them as compiled,
   TradingView-tested, non-repainting, secure, or production-ready.
6. Treat a hash-matching record in `verification/tradingview.json` as manual
   evidence only for the recorded file and environment.
7. If sources conflict, a source is unavailable, or intent is ambiguous, narrow
   the claim and state what remains unverified.
8. Never expose credentials or place real webhook secrets in code or output.
9. Prefer a minimal change, include a validation path, and separate code-ready,
   tested, published, and live states.

The project is independent and is not affiliated with or endorsed by TradingView.
