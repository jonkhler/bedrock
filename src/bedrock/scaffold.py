"""Scaffold and sync operations."""

import shutil
import subprocess
from pathlib import Path

from bedrock.console import info, warn
from bedrock.paths import bedrock_home
from bedrock.settings import merge_hook


def sync(target: Path, force: bool = False) -> None:
    """Sync bedrock files into a project directory."""
    home = bedrock_home()
    target = target.resolve()
    first_time = not (target / ".bedrock").exists()

    # Rules (bedrock owns entirely)
    rules_dir = target / ".bedrock" / "rules"
    rules_dir.mkdir(parents=True, exist_ok=True)
    for src in sorted((home / ".bedrock" / "rules").glob("*.md")):
        shutil.copy2(src, rules_dir / src.name)

    # Stack config template (only if missing)
    stack_yml = target / ".bedrock" / "stack.yml"
    if not stack_yml.exists():
        shutil.copy2(home / ".bedrock" / "stack.yml", stack_yml)

    # Commands (bedrock owns entirely)
    commands_dir = target / ".claude" / "commands"
    commands_dir.mkdir(parents=True, exist_ok=True)
    for src in sorted((home / ".claude" / "commands").glob("*.md")):
        shutil.copy2(src, commands_dir / src.name)

    # Merge hook into .claude/settings.json
    merge_hook(target / ".claude" / "settings.json")

    # Template files: copy on first sync, skip on upgrades (unless --force)
    for filename in ("PROGRESS.md", "CLAUDE.md"):
        dest = target / filename
        if force:
            shutil.copy2(home / filename, dest)
        elif not dest.exists():
            shutil.copy2(home / filename, dest)
        elif first_time:
            warn(f"{filename} already exists, skipping (use --force to overwrite)")

    info(f"synced {target}")


def init_git(target: Path) -> None:
    """Git init if not already a repo."""
    if not (target / ".git").exists():
        subprocess.run(["git", "init", str(target)], check=True, capture_output=True)


def gather_stack_interactive(target: Path) -> str:
    """Interactively gather stack info by asking questions via claude CLI."""
    home = bedrock_home()
    template = (home / "prompts" / "gather-stack.md").read_text()
    gathered = ""

    info("interactive stack setup (ctrl-c to abort)")
    print()

    while True:
        prompt = template.replace("{{gathered}}", gathered or "Nothing yet.")
        result = subprocess.run(
            ["claude", "-p", prompt],
            capture_output=True, text=True,
        )
        response = result.stdout.strip()

        if response.startswith("READY:"):
            stack_desc = response[len("READY:"):].strip()
            print()
            info(f"stack determined: {stack_desc}")
            return stack_desc

        print(response)
        answer = input("> ")
        gathered += f"\nQ: {response}\nA: {answer}"


def launch_claude(target: Path, headless: bool) -> None:
    """Launch claude with /stack in the target directory."""
    if headless:
        info("running /stack headless...")
        subprocess.run(
            ["claude", "-p", "--dangerously-skip-permissions", "/stack"],
            cwd=target,
        )
    else:
        info("launching claude with /stack...")
        subprocess.run(["claude", "/stack"], cwd=target)
