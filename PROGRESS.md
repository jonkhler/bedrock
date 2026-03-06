# Progress

## Current state

Complete scaffold with CLI:
- `bedrock <dir> [prompt]` — copies templates, optionally launches `/stack`
- `curl | sh` installer to `~/.bedrock` + `~/.local/bin`
- Commands: `/qa`, `/progress`, `/stack`
- Templates: CLAUDE.md, PROGRESS.md, all commands
- README with install/usage docs

## Next

- Push to GitHub (github.com/jonkhler/bedrock)
- Test end-to-end: install + scaffold a fresh project
- Consider: `.gitignore` template? LICENSE?

## Open decisions

- GitHub username in install.sh — currently `jonkhler`, verify correct
