---
name: stack
description: Configure project stack - fill in CLAUDE.md, set up tooling, initial commit
user_invocable: true
---

Configure this project's language-specific tooling. If `.claude/init-prompt` exists, read it as the stack description. Otherwise, ask the user what stack they want.

## Steps

1. **Determine the stack**: Read `.claude/init-prompt` or ask the user. Identify:
   - Language and version
   - Type checker (and strictness level)
   - Test runner
   - Package manager / build system
   - Any other tooling preferences

2. **Fill in CLAUDE.md**: Update the Stack section with concrete values. Replace `<Project>` in the title with the actual project name (infer from directory name or ask).

3. **Set up tooling**:
   - Initialize the package manager config if needed (e.g., `pyproject.toml`, `package.json`, `Cargo.toml`)
   - Configure the type checker for strict mode
   - Configure the test runner
   - Create a `.pre-commit-config.yaml` with local hooks for the type checker and test runner
   - Create the test directory scaffold
   - Install dependencies
   - Install pre-commit hooks

4. **Update PROGRESS.md** to reflect the configured state.

5. **Delete `.claude/init-prompt`** if it existed.

6. **Commit incrementally** following the iteration protocol:
   - Commit 1: CLAUDE.md with filled-in stack
   - Commit 2: Package config + dependencies
   - Commit 3: Pre-commit config + hooks
   - Commit 4: Test scaffold

After completion, report what was set up and confirm `/qa` passes.
