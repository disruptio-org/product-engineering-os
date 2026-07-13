---
name: setup-project
description: Configure the current repository for Product Engineering OS using local Markdown tracking. Use once per project before the other workflow skills.
disable-model-invocation: true
argument-hint: [optional project name]
---

# Setup Project

Inspect the repository before asking questions: root docs, manifests, lockfiles, build files, tests, CI, existing agent instructions, architecture docs, and executable commands.

Use local Markdown as the tracker. Do not ask which tracker to use.

Present detected stack, commands, existing instructions, and material gaps. Recommend defaults. Ask only for commands or boundaries that cannot be inferred safely.

Create or carefully merge:

- `AGENTS.md` from `${CLAUDE_PLUGIN_ROOT}/templates/AGENTS.md.template`;
- `CLAUDE.md` from `${CLAUDE_PLUGIN_ROOT}/templates/CLAUDE.md.template`;
- `.product-os/config.yml`;
- `docs/agents/workflow.md`;
- `docs/adr/README.md`;
- `docs/personas/README.md`;
- `docs/product/README.md`.

Preserve useful existing content. Never overwrite wholesale without reconciling it. Replace every command placeholder with a real command or `not-configured`.

Keep `AGENTS.md` concise. Put procedures in skills.

Run `product-os doctor`, read the generated files, and fix inconsistencies.

Finish by recommending `/product-engineering-os:idea <idea>`.
