# Progress

## Current state

Python CLI (click + rich, installed via `uv tool install`):
- `bedrock new <dir> [prompt]` — scaffolds project, optionally launches `/stack`
- `bedrock sync` — inject/upgrade bedrock in any project (new or existing)
- `bedrock update` — pull latest templates to ~/.bedrock
- `bedrock version` — show installed version
- `curl | sh` installer using `uv tool install`
- Flags: `--name`, `--bare`, `--headless`
- Commands: `/qa`, `/progress`, `/stack`, `/remind`

Architecture:
- `.bedrock/rules/` — engineering principles (consent, testing, code-quality, epistemic, iteration)
- `.bedrock/stack.yml` — project stack config (read by /qa and /stack)
- `UserPromptSubmit` hook injects rules every turn via `.claude/settings.json`
- `/remind` command for manual rule re-injection
- CLAUDE.md is user's space only (project name placeholder, never touched by sync)
- `bedrock sync` merges hook into existing settings.json without clobbering

## Next

- Push to GitHub (github.com/jonkhler/bedrock)
- Test end-to-end: fresh scaffold, sync into existing project, upgrade after update
- Consider: LICENSE?
