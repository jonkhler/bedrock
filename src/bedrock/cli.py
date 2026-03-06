"""Bedrock CLI — scaffold projects with engineering discipline."""

import subprocess
import sys
from pathlib import Path

import click

from bedrock.console import info, error
from bedrock.paths import bedrock_home
from bedrock.scaffold import gather_stack_interactive, init_git, launch_claude, sync


@click.group(invoke_without_command=True)
@click.pass_context
def main(ctx: click.Context) -> None:
    """Scaffold projects with engineering discipline for Claude Code."""
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())


@main.command()
@click.argument("directory", type=click.Path())
@click.argument("prompt", required=False, default=None)
@click.option("--name", default=None, help="Project name (defaults to directory basename).")
@click.option("--bare", is_flag=True, help="Copy scaffold files only, skip stack configuration.")
@click.option("--headless", is_flag=True, help="Run /stack non-interactively and exit.")
def new(directory: str, prompt: str | None, name: str | None, bare: bool, headless: bool) -> None:
    """Scaffold a new project.

    DIRECTORY is the target directory (created if it doesn't exist).
    PROMPT is an optional stack description, e.g. "Python 3.13, uv, pyright strict, pytest".
    """
    target = Path(directory).resolve()
    target.mkdir(parents=True, exist_ok=True)

    project_name = name or target.name

    init_git(target)
    sync(target)
    info(f"scaffolded {target}")

    if bare:
        info(f"bare mode — run 'claude' in {target} and use /stack to configure")
        return

    # Determine stack
    if prompt is None:
        stack_desc = gather_stack_interactive(target)
    else:
        stack_desc = prompt

    # Write init-prompt
    init_prompt_file = target / ".claude" / "init-prompt"
    init_prompt_file.parent.mkdir(parents=True, exist_ok=True)
    init_prompt_file.write_text(f"Project name: {project_name}\n{stack_desc}\n")

    launch_claude(target, headless)


@main.command(name="sync")
@click.argument("directory", default=".", type=click.Path(exists=True))
def sync_cmd(directory: str) -> None:
    """Sync bedrock files into a project directory."""
    sync(Path(directory))


@main.command()
def update() -> None:
    """Pull latest bedrock templates and reinstall CLI."""
    home = bedrock_home()
    info("pulling latest...")
    result = subprocess.run(
        ["git", "pull", "--ff-only"],
        cwd=home,
    )
    if result.returncode != 0:
        error("git pull failed")
        sys.exit(1)

    info("reinstalling CLI...")
    result = subprocess.run(
        ["uv", "tool", "install", "--force", str(home)],
    )
    if result.returncode != 0:
        error("uv tool install failed")
        sys.exit(1)
    info("done.")


@main.command()
def version() -> None:
    """Show installed version."""
    home = bedrock_home()
    result = subprocess.run(
        ["git", "rev-parse", "--short", "HEAD"],
        cwd=home,
        capture_output=True,
        text=True,
    )
    ver = result.stdout.strip() if result.returncode == 0 else "unknown"
    click.echo(f"bedrock {ver}")
