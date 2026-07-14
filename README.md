# Product Engineering OS

Claude Code plugin marketplace for product discovery, grilling, BRDs, vertical user stories, TDD, implementation, review, and acceptance.

## Install in Claude Code

```text
/plugin marketplace add disruptio-org/product-engineering-os
/plugin install product-engineering-os@product-os-tools
/reload-plugins
```

Then initialize the current project:

```text
/product-engineering-os:setup-project
```

## Local development

```bash
git clone https://github.com/disruptio-org/product-engineering-os.git
cd product-engineering-os
claude --plugin-dir ./product-engineering-os-toolkit/plugins/product-engineering-os
```

The marketplace manifest lives at `.claude-plugin/marketplace.json`. The plugin manifest lives inside the plugin directory at `product-engineering-os-toolkit/plugins/product-engineering-os/.claude-plugin/plugin.json`.
