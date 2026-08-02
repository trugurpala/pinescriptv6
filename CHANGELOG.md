# Changelog

All notable public changes to Pine Script Agent Kit are recorded here.

## [Unreleased]

### Added

- A standard, self-contained Codex skill bundle under
  `.agents/skills/pine-script-agent-kit/`, generated from the canonical Pine
  protocol, source catalog, rule explanations, example evidence, and manual
  verification guidance.
- Codex Desktop installation and smoke-test guidance using `$skill-installer`,
  with an explicit reminder that installation alone does not prove host loading
  or compliance.

## [1.1.0] — 2026-08-02

### Added

- Source-bound reliability rules for alerts, strategy recalculation and
  execution timing, backtesting assumptions, and repaint classification.
- Public alert, strategy execution, repainting, backtesting, adoption,
  coverage, roadmap, support, and rule-contribution guides.
- A hash-bound, user-reported Pine Editor check for
  `examples/indicators/01_ema_cross.pine`; runtime, repaint, alert delivery,
  data access, profitability, security, and live-trading remain unverified.
- A rule contribution template and linked contribution paths for source,
  rule, correction, example, verification, adapter, claim, and security reviews.

### Changed

- Made the offline CLI boundary explicit with six `NOT CHECKED` results after a
  successful `check` run.
- Reworked subdirectory guides with clear entry points, evidence limits, and
  safer TradingView, migration, market, and webhook workflows.
- Hardened EMA and related example comments with timing, fill, cost, alert, and
  mechanism-specific repaint disclosures without changing Pine behavior.
- Hardened Cline, Windsurf, Devin, and Zed host adoption around supported
  surfaces and first-match precedence while retaining generated artifacts.
- Corrected VİOP entry signals and session-close alert wording to distinguish
  the entry window, possible out-of-session exits and fills, and close requests.

### Security and maintenance

- Hardened catalog rule body validation so rule explanation paths must stay
  inside the repository.
- Added an advisory source-link workflow for scheduled or manual official URL
  freshness checks.
- Pinned GitHub Actions to immutable commit SHAs and added monthly Dependabot
  maintenance for GitHub Actions updates.

## [1.0.0] — 2026-08-01

### Added

- source-linked Pine Script v6 rules with explicit scope, exceptions, evidence
  levels, and verification dates;
- a complete SHA-256 inventory for 56 Pine v6 examples;
- deterministic guidance for Codex, Claude Code, Gemini CLI, Cursor, Cline,
  Windsurf, GitHub Copilot, Zed, and portable knowledge packs;
- Python standard-library validation, rendering, drift, manifest, and link
  checks;
- English and Turkish user guides, contribution and security policies, and the
  Verified Signal visual system;
- coverage of official Pine v6 changes documented through July 2026.

### Evidence boundary

Repository checks establish structure and consistency. They do not establish
TradingView compilation, runtime behavior, profitability, non-repainting
behavior, data entitlement, or live-trading suitability.

[Unreleased]: https://github.com/trugurpala/pinescriptv6/compare/v1.1.0...HEAD
[1.1.0]: https://github.com/trugurpala/pinescriptv6/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/trugurpala/pinescriptv6/releases/tag/v1.0.0
