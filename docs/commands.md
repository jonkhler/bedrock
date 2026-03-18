# Commands

Commands are Claude Code slash commands that live in `.claude/commands/`. Use them inside a Claude session.

## /qa

**Type checker + tests + test quality review.**

Reads `.bedrock/stack.yml` to know which tools to run, then executes three checks in order:

1. **Type checker** -- run the configured type checker (e.g. `pyright --pythonversion 3.13`). Stop on errors.
2. **Test runner** -- run the configured test runner (e.g. `pytest`). Stop on failures.
3. **Critical QA review** -- review all test files for slop tests:
    - Property-existence checks instead of value checks
    - Mocks that don't verify real behavior
    - Missing edge cases and failure modes

Reports `PASS` or `FAIL` for each phase. Blocks progress if anything fails.

## /stack

**Configure project stack.**

Sets up language-specific tooling for the project:

1. Fills in `.bedrock/stack.yml` with concrete values
2. Sets the project name in `CLAUDE.md`
3. Initializes package config, type checker, test runner
4. Installs pre-commit hooks
5. Creates test directory scaffold
6. Makes incremental commits

Run automatically during `bedrock new`, or manually with `/stack` after `bedrock new --bare`.

## /progress

**Check if PROGRESS.md needs updating.**

Reviews recent commits against the current PROGRESS.md. Updates it if anything is stale -- current state, next steps, or open decisions. Keeps it under 30 lines.

PROGRESS.md is a context-recovery document, not a changelog. It tells Claude (and you) where the project stands right now.

## /remind

**Re-inject and acknowledge rules.**

Reads every file in `.bedrock/rules/` and confirms each rule. Useful when you feel Claude has drifted from the rules mid-session, or after context compression.
