# Product Engineering OS

A Claude Code–only toolkit that turns a rough product idea into a tested, reviewable vertical delivery.

```text
setup-project → idea → grill-me → write-brd → create-stories
              → manage-stories → implement-story → accept-story
```

Supporting disciplines: `grilling`, `tdd`, and `story-review`.

## Install from GitHub

Push this repository to GitHub, then run:

```text
/plugin marketplace add OWNER/REPOSITORY
/plugin install product-engineering-os@product-os-tools
/product-engineering-os:setup-project
```

## Test locally

```bash
claude --plugin-dir ./plugins/product-engineering-os
```

## Project files created by setup

```text
AGENTS.md
CLAUDE.md
.product-os/config.yml
docs/agents/
docs/adr/
docs/personas/
docs/product/
```

Stories are local Markdown files:

```text
docs/product/<feature>/stories/STORY-###-<slug>.md
```

States:

```text
draft → needs-discovery → ready → in-progress → in-review → acceptance → done
```

Use `blocked` for an unresolved external dependency.

The bundled CLI supports:

```bash
product-os doctor
product-os story-list
product-os story-next
product-os validate-story <story>
product-os set-state <story> <state>
product-os refresh-index docs/product/<feature>
```

## Principles

- Build vertical user outcomes, not layer-only task piles.
- Ask one load-bearing question at a time.
- Separate facts, assumptions, decisions, and risks.
- Agree one primary testing seam before implementation.
- Never mark a story done without acceptance evidence.
- Keep durable product truth in the repository.
- Treat simulated personas as thinking lenses, not customer research.

## Acknowledgement

Inspired by the small, composable engineering-skill philosophy popularized by Matt Pocock's public skills repository. This toolkit is independently written.
