# Security policy

## Scope

This repository contains Pine Script code, AI instruction content, Python quality
tools, webhook templates, and documentation. Relevant reports include:

- committed credentials, tokens, private keys, personal data, or private code;
- webhook examples that enable authentication bypass, replay, injection, or
  unsafe order routing;
- malicious or misleading agent instructions that could expose data or execute
  out-of-scope actions;
- validation bypasses that let unverified claims enter generated adapters;
- dependency/workflow changes that create a supply-chain risk.

Pine examples are educational and are not a promise of secure, profitable, or
production-safe trading behavior.

## Private reporting

Do not open a public issue for a sensitive vulnerability or exposed secret.
Email **mail@ugurpala.com** with the affected path, impact, reproduction steps,
and a safe contact method. Remove real credentials and personal data from the
report where possible.

General correctness questions that do not expose sensitive details may use
[GitHub Discussions](https://github.com/trugurpala/pinescriptv6/discussions).

## Supported versions

Security fixes target the current default branch and the latest published release
when the issue applies there. The current release is `v1.0.0`.

## Webhook and secret guidance

- keep tokens outside Pine source and Git history;
- use placeholders in committed templates;
- authenticate requests server-side and validate symbol, side, size, timestamp,
  nonce, and allowed account;
- use replay protection, least privilege, audit logging, kill switches, and risk
  limits before routing any order;
- rotate a credential immediately if it may have been exposed.

The local PSAK tools collect no telemetry. `python tools/psak.py links` contacts
only registered source URLs when explicitly run.
