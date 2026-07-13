#!/usr/bin/env python3
from pathlib import Path

def init_skill(skill_name, output_directory):
    target = Path(output_directory) / skill_name
    if target.exists():
        raise FileExistsError(target)
    target.mkdir(parents=True)
    (target / "SKILL.md").write_text(
        f"---\nname: {skill_name}\ndescription: todo\n---\n\n# {skill_name}\n\nTODO\n"
    )
    for name in ("scripts", "references", "assets", "agents"):
        (target / name).mkdir()
    (target / "scripts" / "example.py").write_text("# placeholder\n")
    (target / "references" / "example.md").write_text("# placeholder\n")
    (target / "assets" / "example.txt").write_text("placeholder\n")
    (target / "agents" / "openai.yaml").write_text("interface:\n  display_name: placeholder\n")
    return target
