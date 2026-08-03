# Governance

Pine Script Agent Kit is an independent, community-oriented project maintained
in public. This document explains how decisions are made, how responsibility is
assigned, and how maintainership can evolve.

## Maintainer

The current maintainer is [Uğur Pala](https://github.com/trugurpala). The
maintainer is responsible for:

- reviewing and merging contributions;
- protecting the evidence boundary between local structural checks and
  TradingView or live-use claims;
- maintaining releases, documentation, community spaces, and CI;
- coordinating private security reports;
- applying the Code of Conduct.

Repository ownership is not a claim that every contribution is authored or
endorsed by the maintainer. Git history and release notes remain the source of
attribution.

## How decisions are made

Routine documentation, test, adapter, and maintenance changes are decided
through review against the repository's published rules and checks. Pine
semantics require traceable evidence from `knowledge/sources.json`; manual
TradingView evidence remains hash-bound to the recorded file and environment.

For changes with broad user impact, the maintainer should:

1. state the problem and the affected users;
2. invite discussion when multiple reasonable directions exist;
3. record the decision in the pull request, issue, discussion, or changelog;
4. preserve compatibility when practical and explain intentional breaks;
5. keep local, TradingView-tested, published, and live states separate.

The maintainer has final merge and release authority. Decisions may be revisited
when official documentation, reproducible evidence, security needs, or user
experience changes.

## Contribution and review

Anyone may propose a change through GitHub Discussions, an issue, or a pull
request. Contributions are evaluated on relevance, evidence quality, test
coverage, clarity, maintenance cost, and safety—not on contributor status.

The repository's `CODEOWNERS` file requests maintainer review. Approval does not
replace required automated checks or evidence records. Sensitive reports follow
`SECURITY.md` and must not be discussed publicly before coordinated disclosure.

## Releases

The maintainer publishes releases from the default branch after required checks
pass. User-visible changes are recorded under `Unreleased` before they receive a
version tag and GitHub Release. Security fixes may use an expedited review path,
but their scope and validation must still be documented safely.

## Maintainer succession

If the maintainer expects to become unavailable, they should identify a trusted
successor with a sustained contribution record, document the transition
publicly, and transfer only the minimum repository access required. Until a
transition is complete, no contributor should represent themselves as a
maintainer.

If the project becomes inactive without a planned handoff, community members may
fork it under the MIT License. A fork must not imply ownership of this
repository, its release history, or its community accounts.

## Divan's role

This project was planned and delivered with
[Divan](https://github.com/trugurpala/divan), a development infrastructure for
coding hosts. Divan does not make governance decisions, hold maintainer
authority, or create a requirement for contributors.

## Türkçe kısa özet

Projenin mevcut bakım sorumlusu
[Uğur Pala](https://github.com/trugurpala)'dır. Katkılar; ilgi, kanıt kalitesi,
test kapsamı, açıklık, bakım maliyeti ve güvenlik ölçütleriyle değerlendirilir.
Birleştirme ve sürüm yetkisi bakım sorumlusundadır; geniş etkili kararlar kamusal
issue, discussion, pull request veya changelog kaydıyla gerekçelendirilir. Divan
geliştirme altyapısıdır, yönetişim yetkisi taşımaz. Hassas bildirimler
`SECURITY.md` üzerinden özel olarak yapılır.
