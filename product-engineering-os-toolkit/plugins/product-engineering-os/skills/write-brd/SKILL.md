---
name: write-brd
description: Turn a developed and grilled idea into a business requirements document stored in the repository.
disable-model-invocation: true
argument-hint: [feature slug or idea path]
---

# Write the BRD

Require an idea brief and prefer a completed grill summary. Read related personas, research, ADRs, and current-process evidence.

Use `${CLAUDE_PLUGIN_ROOT}/templates/brd.md.template`. Write `docs/product/<feature>/brd.md`.

Explain the problem, outcome, users, current and proposed journeys, scope, non-goals, business rules, permissions, data, compliance, success measures, dependencies, risks, and release phases.

Use requirement IDs when useful. Separate confirmed facts, assumptions, and open decisions.

Do not prescribe layer-by-layer implementation tasks. If a load-bearing contradiction remains, mark it and recommend another grilling pass.

Quality gate: success is observable, scope is smaller than the vision, permission and failure behavior is explicit, and non-goals prevent scope creep.
