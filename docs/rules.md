# Rules

Rules live in `.bedrock/rules/` and are injected into every Claude interaction via the `UserPromptSubmit` hook. They shape how Claude approaches your project.

## Built-in rules

### consent

> Never jump to implementation after discussion. Explain, propose, wait for explicit approval.

This is the most impactful rule. Without it, Claude will see a problem and immediately "fix" it -- often making unwanted changes. With this rule, Claude diagnoses, proposes, and waits.

### testing

> Strict TDD. Tests pin intended behavior before implementation.

Rejects "slop tests" -- tests that check property existence, assert `isinstance`, or mock everything without verifying real behavior. Tests must catch real regressions.

### code-quality

> Code is for humans. Readability is the primary design constraint.

Enforces strict typing, small pure functions, DTOs over god-classes, no redundancy. Any user correction gets added to CLAUDE.md immediately.

### epistemic

> Do not jump to conclusions. When uncertain: search, then ask.

Prevents Claude from guessing at APIs, library behavior, or system semantics. Forces it to look things up or ask you.

### iteration

> For every unit of work: recover context, resolve uncertainties, plan, test, implement, commit, update progress.

The full workflow protocol:

```mermaid
flowchart LR
    A["Read PROGRESS.md"] --> B["Resolve uncertainties"]
    B --> C["Plan + confirm"]
    C --> D["Pin tests"]
    D --> E["Implement until /qa passes"]
    E --> F["Commit"]
    F --> G["Run /progress"]
```

## How rules get injected

Rules aren't suggestions -- they're injected as system context on every prompt via the `UserPromptSubmit` hook. Claude sees them as instructions, not guidelines.

```
You send a prompt
  --> hook fires
    --> reads .bedrock/rules/*.md
      --> text prepended to Claude's context
        --> Claude responds following the rules
```

This means rules are active even if Claude's context window has been compressed and earlier instructions are lost. They're re-injected every single turn.
