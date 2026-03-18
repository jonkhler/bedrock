# Progress

## Current state

Python CLI (click + rich, installed via `uv tool install`):
- `bedrock new <dir> [prompt]` — scaffolds project, optionally launches `/stack`
- `bedrock sync [--force]` — inject/upgrade bedrock in any project
- `bedrock update` — pull latest templates, reinstall CLI
- `bedrock version` — show installed version
- `curl | sh` installer using `uv tool install`
- Flags: `--name`, `--bare`, `--headless`, `--force`
- Commands: `/qa`, `/progress`, `/stack`, `/remind`

Architecture:
- `.bedrock/rules/` — engineering principles injected every turn via hook
- `.bedrock/stack.yml` — project stack config (read by /qa and /stack)
- `UserPromptSubmit` hook injects rules into Claude context
- CLAUDE.md is user's space (never overwritten by sync)
- First-time sync warns on existing files, `--force` overwrites

Documentation:
- MkDocs Material site at jonkhler.github.io/bedrock
- Auto-deploys via GitHub Actions on push to main
- Covers architecture, rules, commands, CLI reference, extending

## Next

- Test end-to-end: fresh scaffold, sync into existing project, upgrade after update
- Consider: PyPI publishing for `uv tool install bedrock-cli` without git clone
