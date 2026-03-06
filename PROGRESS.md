# Progress

## Current state

Complete scaffold with CLI:
- `bedrock <dir> [prompt]` — copies templates, optionally launches `/stack`
- `curl | sh` installer to `~/.bedrock` + `~/.local/bin`
- Commands: `/qa`, `/progress`, `/stack`, `/remind`
- Templates: CLAUDE.md, PROGRESS.md, all commands

Rule enforcement architecture:
- Engineering principles in `.bedrock/rules/` (consent, testing, code-quality, epistemic, iteration)
- `UserPromptSubmit` hook in `.claude/settings.json` injects rules every turn
- `/remind` command for manual rule re-injection
- CLAUDE.md is user's space (project name, commands, stack config only)

## Next

- Push to GitHub (github.com/jonkhler/bedrock)
- Test end-to-end: install + scaffold a fresh project (verify hook fires)
- Consider: `.gitignore` template? LICENSE?
- Update README to document rule enforcement architecture

## Open decisions

- GitHub username in install.sh — currently `jonkhler`, verify correct
