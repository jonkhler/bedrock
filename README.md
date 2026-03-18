# bedrock

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Docs](https://img.shields.io/badge/docs-jonkhler.github.io%2Fbedrock-blue)](https://jonkhler.github.io/bedrock)

Engineering discipline scaffold for [Claude Code](https://docs.anthropic.com/en/docs/claude-code) projects. Language-agnostic.

## What you get

- **Rules** (`.bedrock/rules/`) — Engineering principles injected every turn via hooks: consent, testing, code quality, epistemic discipline, iteration protocol
- **Commands** — `/qa` (type checker + tests + test quality review), `/progress` (context-recovery updates), `/stack` (project configuration), `/remind` (re-inject rules)
- **PROGRESS.md** — Lean context-recovery document for session starts
- **Stack config** (`.bedrock/stack.yml`) — Declares language, type checker, test runner, package manager

## Install

```sh
curl -sSf https://raw.githubusercontent.com/jonkhler/bedrock/main/install.sh | sh
```

Requires [uv](https://docs.astral.sh/uv/getting-started/installation/).

## Usage

```sh
# With a stack description — configures everything automatically
bedrock new ~/dev/my-app "Python 3.13, uv, pyright strict, pytest"

# With a custom project name
bedrock new --name myapp ~/dev/my-app "Python 3.13, uv, pyright strict, pytest"

# Interactive — asks questions until it has enough info
bedrock new ~/dev/my-app

# Bare scaffold only — configure later with /stack
bedrock new --bare ~/dev/my-app

# Inject bedrock into an existing project
bedrock sync

# Force overwrite CLAUDE.md and PROGRESS.md
bedrock sync --force

# Pull latest templates and reinstall CLI
bedrock update

# Show installed version
bedrock version
```

## How it works

1. **Scaffold**: copies CLAUDE.md, PROGRESS.md, and commands into your project
2. **Gather stack info**: from the prompt argument, or interactively via a question loop
3. **Configure**: launches Claude Code with `/stack`, which fills in CLAUDE.md and sets up language-specific tooling (type checker, test runner, pre-commit hooks, package config)

`/stack` runs headlessly when a complete init-prompt exists — no interactive prompting during automated setup.

The iteration protocol enforces: resolve uncertainties, pin tests, validate with `/qa`, commit, update `/progress`. Every commit passes strict type checking and tests via pre-commit hooks.

## Structure

```
src/bedrock/         # CLI (Python, installed via uv)
.bedrock/
  rules/             # Engineering rules (copied into new projects)
  stack.yml          # Stack config template
.claude/commands/    # Commands (copied into new projects)
  qa.md
  progress.md
  stack.md
  remind.md
prompts/             # Prompt templates read by the CLI
  gather-stack.md
CLAUDE.md            # Template (copied into new projects)
PROGRESS.md          # Template (copied into new projects)
install.sh           # curl | sh installer
pyproject.toml       # Package config
```

## Documentation

Full docs at [jonkhler.github.io/bedrock](https://jonkhler.github.io/bedrock) — architecture, rules reference, extending guide, and more.

## License

MIT
