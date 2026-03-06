# bedrock

Engineering discipline scaffold for Claude Code projects. Language-agnostic.

## What you get

- **CLAUDE.md** — Principles (code is for humans, strict typing, TDD), epistemic protocol, iteration protocol
- **Commands** — `/qa` (type checker + tests + test quality review), `/progress` (context-recovery updates), `/stack` (project configuration)
- **PROGRESS.md** — Lean context-recovery document for session starts

## Install

```sh
curl -sSf https://raw.githubusercontent.com/jonkhler/bedrock/main/install.sh | sh
```

Make sure `~/.local/bin` is on your `PATH`.

## Usage

```sh
# With a stack description — launches /stack automatically
bedrock ~/dev/my-project "Python 3.13, uv, pyright strict, pytest"

# Interactive — asks questions until it has enough info, then launches /stack
bedrock ~/dev/my-project

# Bare scaffold only — configure later with /stack
bedrock --bare ~/dev/my-project
```

## Update

```sh
bedrock update
```

## How it works

1. **Scaffold**: copies CLAUDE.md, PROGRESS.md, and commands into your project
2. **Gather stack info**: from the prompt argument, or interactively via a question loop
3. **Configure**: launches Claude Code with `/stack`, which fills in CLAUDE.md and sets up language-specific tooling (type checker, test runner, pre-commit hooks, package config)

The iteration protocol enforces: resolve uncertainties, pin tests, validate with `/qa`, commit, update `/progress`. Every commit passes strict type checking and tests via pre-commit hooks.
