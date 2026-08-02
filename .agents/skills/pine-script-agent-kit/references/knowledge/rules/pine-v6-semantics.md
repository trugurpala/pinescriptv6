# Pine v6 semantics

This page explains source-backed Pine v6 rules that are frequently flattened
into unsafe absolutes by AI coding tools. The canonical fields, source IDs, and
evidence levels live in `knowledge/catalog.json`.

## APIs are selected by behavior

`math.avg()` is documented. Generic `input()` is documented. Typed inputs add
type-specific controls and can improve clarity, but their existence does not make
the generic function invalid.

`barstate.islast` identifies the chart's last available bar; `barstate.isconfirmed`
identifies a confirmed update. Choose the condition that matches the script's
execution intent.

## Current release-note surface

The catalog tracks newer v6 features only to the extent supported by official
release notes and reference pages. Static repository checks can confirm that an
example is present and declares v6; they cannot confirm data entitlement,
compilation, or runtime behavior in TradingView.

## Syntax guidance changes over time

Multiline strings, wrapping inside parentheses, and automatic-parentheses changes
make older blanket formatting rules unreliable. Use the current grammar and keep
the release-note date attached to guidance about newly added syntax.
