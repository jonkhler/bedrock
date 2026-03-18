# bedrock

Engineering discipline scaffold for [Claude Code](https://docs.anthropic.com/en/docs/claude-code) projects. Language-agnostic.

## The problem

Claude Code is powerful but permissive. Without guardrails it will:

- Jump straight to implementation without confirming the plan
- Write tests that check structure instead of behavior
- Guess at APIs instead of looking them up
- Make large, monolithic commits

**bedrock** fixes this by injecting engineering rules into every Claude interaction via hooks, and providing commands that enforce the workflow.

## What you get

- **Rules** injected every turn -- consent, testing, code quality, epistemic discipline, iteration protocol
- **Commands** -- `/qa`, `/stack`, `/progress`, `/remind`
- **Stack config** -- declares your language, type checker, test runner, package manager
- **PROGRESS.md** -- lean context-recovery document for session starts

## Quick install

```sh
curl -sSf https://raw.githubusercontent.com/jonkhler/bedrock/main/install.sh | sh
```

Requires [uv](https://docs.astral.sh/uv/getting-started/installation/).

## 30-second demo

```sh
# Scaffold a new project
bedrock new ~/dev/my-app "Python 3.13, uv, pyright strict, pytest"

# Or inject into an existing project
cd existing-project
bedrock sync
```

That's it. Open the project with `claude` and the rules are active.
