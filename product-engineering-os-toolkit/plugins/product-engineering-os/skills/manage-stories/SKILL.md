---
name: manage-stories
description: Manage local Markdown stories: status, readiness, next work, state transitions, and blockers.
disable-model-invocation: true
argument-hint: [status|ready|next|start|review|acceptance|block|done] [story]
---

# Manage Stories

Manage planning state only. Do not implement code.

Modes:

- `status`: list stories, refresh indexes, summarize flow and blockers.
- `ready`: validate outcome, criteria, permissions, dependencies, seam, and size; otherwise set `needs-discovery`.
- `next`: recommend one unblocked ready story.
- `start`: require `ready`, then set `in-progress`.
- `review`: require implementation evidence, then set `in-review`.
- `acceptance`: require independent review, then set `acceptance`.
- `block`: set `blocked` and record the exact unblock condition.
- `done`: require an accepted report, then set `done`.

Use `product-os validate-story`, `set-state`, and `refresh-index`.

Never bypass a state gate to make the board look complete.
