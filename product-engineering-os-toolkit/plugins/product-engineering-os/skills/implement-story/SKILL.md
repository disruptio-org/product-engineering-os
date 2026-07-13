---
name: implement-story
description: Implement exactly one ready vertical story using an agreed test seam, TDD, independent review, and repository verification.
disable-model-invocation: true
argument-hint: [story path or STORY-ID]
---

# Implement One Story

Resolve and validate the story. Proceed only when state is `ready`.

Read agent instructions, the story, BRD, ADRs, dependencies, surrounding code, and tests. Confirm the primary testing seam. Correct the story before coding if the seam is wrong.

Move to `in-progress`. Delegate to `product-engineering-os:story-developer` when useful.

Apply `tdd`: one behavior, failing proof, minimum implementation, passing proof, refactor, repeat.

Keep contracts stable unless the story changes them. Do not implement other stories opportunistically.

Run targeted and relevant full tests, lint, type-check, build, and runtime verification where practical. Do not claim unexecuted checks passed.

Apply `story-review`, fix blocking findings, rerun checks, and move to `in-review`, not `done`. Record exact evidence. Recommend `accept-story`.
