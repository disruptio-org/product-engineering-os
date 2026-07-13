---
name: create-stories
description: Divide a BRD into small vertical user stories with dependencies, acceptance criteria, and one primary testing seam.
disable-model-invocation: true
argument-hint: [feature slug or BRD path]
---

# Create Vertical Stories

Require the feature BRD.

Find the thinnest end-to-end delivery spine. Split foundation work only when it independently reduces material risk or is a hard prerequisite.

Never create layer-only stories such as database, API, frontend, or tests. Those are tasks inside a vertical story.

Each story must produce one observable outcome, fit one focused agent session, state scope and non-goals, include permissions and failure states, declare dependencies, identify one primary testing seam, and list only critical invariant tests.

Use `${CLAUDE_PLUGIN_ROOT}/templates/story.md.template`. Write `STORY-###-<slug>.md` files plus `stories/README.md`.

Start stories as `draft` unless every readiness condition is proven. Use tracer-bullet ordering.

Run `product-os refresh-index docs/product/<feature>` and `product-os story-list`. Present sequence, foundations, first user value, risks, and discovery gaps. Do not implement.
