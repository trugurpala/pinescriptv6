# TradingView Manual Verification

Use this process only when a person has checked the exact Pine file in
TradingView Pine Editor. Local repository checks remain `structural-only`.

## Record a Manual Check

1. Confirm the file is tracked in `examples/manifest.json`.
2. Copy the file's current SHA-256 from the manifest.
3. Test that exact file in TradingView Pine Editor.
4. Add a record to `verification/tradingview.json` with the file path, SHA-256,
   Pine version, test date, result, environment, reviewer, and notes.
5. Update the matching `examples/manifest.json` entry to use
   `tradingview-verified` and the new `tradingview_record` ID only when the
   record result is `pass` and the hash still matches.
6. Run the repository checks before opening a pull request.

Do not record a TradingView check from a filename alone. Do not reuse a record
after the Pine file changes. Do not turn a compile result into a claim about
profitability, security, data access, non-repainting behavior, live-trading
suitability, or every chart and account.

## Commands

```bash
python tools/psak.py manifest
python tools/psak.py validate
python tools/psak.py check
```

`python tools/psak.py manifest --write` rebuilds all example hashes. Use it only
when the manifest should intentionally change, then review the diff.
