# Decision Policy

Pine Script Agent Kit uses a small Divan decision vocabulary for project-shaping
choices. The goal is simple: keep useful ideas, adapt ideas that need local
constraints, cite ideas that should remain context, and reject ideas that would
make the kit unsafe or misleading.

The public decision register lives in `governance/decisions.json`. It is part of
the offline validation gate, so broken records, unsupported dispositions, invalid
dates, duplicate IDs, and dead local references fail `python tools/psak.py
validate`.

## Dispositions

| Disposition | Meaning | When to use it |
| --- | --- | --- |
| `adopt` | Use the idea as a project rule or maintained surface. | The evidence is strong, the scope is clear, and the change belongs in the kit. |
| `adapt` | Keep the intent but reshape it for this repository. | The idea is useful but needs scope, caveats, language parity, or a lighter implementation. |
| `reference` | Keep it as context without turning it into a rule. | The information helps reviewers but is not enough to drive generated agent behavior. |
| `reject` | Do not ship the idea. | It would add false confidence, unnecessary dependency weight, privacy risk, or unsupported claims. |

## Review Rules

Every active decision records a stable ID, a title, one disposition, status,
decision date, summary, rationale, user impact, source references, and
implementation references. A source reference explains why the decision exists.
An implementation reference shows where the decision affects the public kit.

Do not use the register as a private work diary. It should describe durable
product decisions, not the messy path taken to reach them.

When a new Pine source, adapter, example, visual asset, or public claim is added,
review it through this order:

1. Can the source be named and checked?
2. Does the claim have a narrow scope and preserved exceptions?
3. Is the evidence level strong enough for generated guidance?
4. Does the change keep English and Turkish public surfaces aligned?
5. Does it avoid implying TradingView compilation, profit, security, or
   non-repainting behavior without matching evidence?

If any answer is no, choose `adapt`, `reference`, or `reject` instead of forcing
the idea into the active catalog.
