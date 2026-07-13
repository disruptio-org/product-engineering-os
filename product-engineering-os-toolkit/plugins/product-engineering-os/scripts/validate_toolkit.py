#!/usr/bin/env python3
from pathlib import Path
import json, sys

PLUGIN = Path(__file__).resolve().parents[1]
REPO = PLUGIN.parents[1]
errors = []

def fm(path):
    text = path.read_text()
    if not text.startswith("---\n"):
        return {}, "missing frontmatter"
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}, "unterminated frontmatter"
    data = {}
    for line in text[4:end].splitlines():
        if line and not line.startswith(" ") and ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip()
    return data, None

for path in [REPO / ".claude-plugin/marketplace.json", PLUGIN / ".claude-plugin/plugin.json"]:
    try:
        json.loads(path.read_text())
    except Exception as exc:
        errors.append(f"{path}: {exc}")

skills = sorted((PLUGIN / "skills").glob("*/SKILL.md"))
agents = sorted((PLUGIN / "agents").glob("*.md"))

for path in skills:
    data, error = fm(path)
    if error: errors.append(f"{path}: {error}"); continue
    if data.get("name") != path.parent.name: errors.append(f"{path}: name mismatch")
    if not data.get("description") or data.get("description") == "todo": errors.append(f"{path}: bad description")
    if len(path.read_text().splitlines()) > 500: errors.append(f"{path}: exceeds 500 lines")

for path in agents:
    data, error = fm(path)
    if error: errors.append(f"{path}: {error}"); continue
    if not data.get("name") or not data.get("description"): errors.append(f"{path}: missing name/description")

required_templates = [
    "AGENTS.md.template", "CLAUDE.md.template", "config.yml.template",
    "workflow.md.template", "idea.md.template", "brd.md.template",
    "story.md.template", "persona.md.template", "decision.md.template",
    "acceptance-report.md.template"
]
for name in required_templates:
    if not (PLUGIN / "templates" / name).exists(): errors.append("missing template: " + name)

cli = PLUGIN / "bin/product-os"
if not cli.exists() or not cli.stat().st_mode & 0o111: errors.append("CLI missing or not executable")

if errors:
    print("VALIDATION FAILED")
    print("\n".join("- " + e for e in errors))
    sys.exit(1)
print(f"VALID: {len(skills)} skills, {len(agents)} agents, manifests, templates, and CLI")
