---
name: accept-story
description: Prove a reviewed story works end to end, record evidence, and mark it done only when every gate passes.
disable-model-invocation: true
argument-hint: [story path or STORY-ID]
---

# Accept a Story

Require state `in-review` and no unresolved blocking review findings. Move to `acceptance`.

Create `docs/product/<feature>/acceptance/<STORY-ID>-acceptance.md` using `${CLAUDE_PLUGIN_ROOT}/templates/acceptance-report.md.template`.

Map every acceptance criterion to evidence. Run focused tests, required lint/type-check/build, runtime or UI verification, permission/error/recovery scenarios, and relevant regressions.

Never invent evidence.

On failure: mark report `rejected`, return story to `in-progress`, and record the gap.

On success: mark report `accepted`, move story to `done`, and refresh the index.

A unit test alone is not acceptance for a user-visible story.
