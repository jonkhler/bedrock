"""Merge bedrock hooks into .claude/settings.json without clobbering user settings."""

import json
from pathlib import Path

HOOK_CMD = 'cat "$CLAUDE_PROJECT_DIR/.bedrock/rules/"*.md 2>/dev/null || true'


def merge_hook(settings_file: Path) -> None:
    settings_file.parent.mkdir(parents=True, exist_ok=True)

    hook_entry = {
        "matcher": "",
        "hooks": [{"type": "command", "command": HOOK_CMD}],
    }

    if not settings_file.exists():
        settings = {"hooks": {"UserPromptSubmit": [hook_entry]}}
        settings_file.write_text(json.dumps(settings, indent=2) + "\n")
        return

    text = settings_file.read_text()
    if ".bedrock/rules/" in text:
        return

    settings = json.loads(text)
    hooks = settings.setdefault("hooks", {})
    ups = hooks.setdefault("UserPromptSubmit", [])
    ups.append(hook_entry)

    settings_file.write_text(json.dumps(settings, indent=2) + "\n")
