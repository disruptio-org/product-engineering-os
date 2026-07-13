---
name: idea
description: Develop a rough product idea through user, UX, business, technical, and QA perspectives, then save a grounded idea brief.
disable-model-invocation: true
argument-hint: [idea or feature name]
---

# Explore an Idea

Require `.product-os/config.yml`.

Derive a feature slug and read relevant personas, research, product documents, ADRs, and current behavior.

Delegate independent analysis, preferably in parallel, to:

- `product-engineering-os:user-advocate`
- `product-engineering-os:ux-designer`
- `product-engineering-os:business-stakeholder`
- `product-engineering-os:technical-stakeholder`
- `product-engineering-os:qa-stakeholder`

Ask each for strongest value, most dangerous assumption, what not to build, one load-bearing question, and the smallest useful version.

Synthesize without dumping raw agent output. Ask one load-bearing question at a time. Prioritize target user, painful job, evidence, smallest outcome, adoption, permissions, data, failures, and non-goals.

Label unsupported claims as assumptions. Simulated perspectives do not replace research.

Write `docs/product/<feature>/idea.md` using `${CLAUDE_PLUGIN_ROOT}/templates/idea.md.template`.

Do not write the BRD or stories. Recommend `grill-me`.
