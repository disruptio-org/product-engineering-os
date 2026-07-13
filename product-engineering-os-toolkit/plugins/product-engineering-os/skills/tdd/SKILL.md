---
name: tdd
description: Test-driven development discipline for one vertical behavior at a time through the highest-value seam.
user-invocable: false
---

# TDD Discipline

Before production code: name the behavior and the highest single seam that proves it. Write and run the smallest meaningful failing proof. Make the minimum change, run it to green, refactor, then run the broader suite.

Prefer an orchestrator, public module, service boundary, or user-observable route over scattered internal tests.

Mock external systems behind the seam, not the behavior under test.

Add focused lower-level tests only for critical invariants such as authentication before access, permissions, schema validation, destructive-operation guards, transactions, or idempotency.

Do not backfill tests and call it TDD.
