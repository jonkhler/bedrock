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
# Scaffold with a stack description
bedrock ~/dev/my-project "Python 3.13, uv, pyright strict, pytest"

# Scaffold without — configure interactively with /stack
bedrock ~/dev/my-project
cd ~/dev/my-project
claude
> /stack
```

## Update

```sh
bedrock update
```

## How it works

`bedrock` copies template files into your project and optionally launches Claude Code with `/stack` to set up language-specific tooling (type checker, test runner, pre-commit hooks, package config).

The iteration protocol enforces: resolve uncertainties, pin tests, validate with `/qa`, commit, update `/progress`. Every commit passes strict type checking and tests via pre-commit hooks.
