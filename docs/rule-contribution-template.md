# Rule contribution template

Copy the sections below into an issue or pull-request description. Keep the claim
narrow enough for the named official source to support it.

## Rule ID

`PSAK-FAMILY-NNN`

## Claim

One source-supported sentence.

## Scope

The Pine version, script type, API, timeframe relationship, or execution context.

## Rationale

Why an agent needs this rule and what error it prevents.

## Exceptions

Cases where the claim does not apply or requires a narrower interpretation.

## Official source ID

The stable ID registered in `knowledge/sources.json`.

## Official source locator

The document section that supports the claim.

## Verified date

`YYYY-MM-DD`

## Example

A minimal use that stays inside the claim's scope.

## Counterexample

A nearby case where applying the rule mechanically would be wrong.

## Local test

The failing-first test and commands that validate structure, references, and
generated output. Report the result as `structural-only`.

## TradingView manual verification required

Yes or no, with the behavior and environment that need checking. If a Pine file
is checked, follow the [manual verification guide](tradingview-manual-verification.md)
and bind the record to its current hash.

Official source support and TradingView file verification are different evidence
types. A source can support a general rule without proving that one file compiles
or behaves as intended. A hash-bound TradingView record applies only to the file
and environment it names; it does not replace a source for a general Pine claim.
