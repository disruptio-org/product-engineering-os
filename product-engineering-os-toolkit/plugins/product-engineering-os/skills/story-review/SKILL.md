---
name: story-review
description: Review a story implementation independently for engineering quality and fidelity to requirements.
user-invocable: false
---

# Story Review

Fix the review base: story, current diff, BRD, ADRs, and agent rules.

Run in parallel when possible:

- `product-engineering-os:quality-reviewer`
- `product-engineering-os:requirements-reviewer`

Synthesize blocking, important, and advisory findings. Include file location, violated rule or criterion, consequence, and smallest fix.

Do not waive blocking findings without an explicit recorded decision. After fixes, rerun the relevant review.
