# Pine Script v5 to v6 migration

This folder is a study guide for common Pine v5-to-v6 syntax and behavior
changes. It provides focused examples for review; it does not automatically
rewrite a script or save compiler errors.

## Evidence and limits

The migration notes are educational and remain `structural-only` until a person
checks the exact file in TradingView. Use the [manual verification guide](../docs/tradingview-manual-verification.md)
when a stronger claim is needed. Remove private code and credentials before
asking for help; see the [support guide](../SUPPORT.md).

## Files

| File | Topic |
| --- | --- |
| `01_study_to_indicator.md` | `study()` to `indicator()` |
| `02_security_to_request.md` | `security()` to `request.security()` |
| `03_strategy_syntax.md` | Strategy declaration changes |
| `04_type_system.md` | Types and explicit declarations |
| `05_arrays_and_collections.md` | Arrays, maps, and matrices |
| `06_input_functions.md` | Input function changes |
| `07_drawing_objects.md` | Lines, labels, and boxes |
| `08_pine_logs.md` | `log.info()` and `log.warning()` |
| `09_methods_and_udt.md` | Methods and user-defined types |
| `10_common_migration_errors.md` | Common migration failures |

## Suggested workflow

1. Identify the v5 construct and the intended behavior.
2. Read the focused note and its registered source references.
3. Make the smallest v6 change in your own copy.
4. Test the exact result in Pine Editor and on the intended chart context.
5. Record what was checked and what remains uncertain.
