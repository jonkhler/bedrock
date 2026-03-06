# <Project> - Project Instructions

## Principles

- **Code is for humans**: Readability is the primary design constraint. Names, structure, and types should make intent obvious. Code that is clever but opaque is wrong
- **No assumed consent**: Never jump to implementation after discussion. Always confirm the plan with the user before writing code. Discussion is not approval. An explicit user invocation (command, loop, or "go ahead") constitutes consent for the scoped task
- **Incremental corrections**: Any user correction or preference gets added to this file immediately
- **Transparent commit graph**: Small, incremental commits with clear messages; no monolithic dumps
- **Strict typing**: Use the strictest type checking available. No escape hatches. Types serve as documentation
- **Strict TDD**: Tests pin intended behavior before implementation proceeds
- **Code quality**: Idiomatic, mostly functional, mostly pure. Small reusable functions. DTOs over god-classes. Collocate related logic. No redundancy. No verbose comments where code is clear

## No Slop Tests

Tests must verify real behavior. Reject:
- Property-existence checks (testing that a field exists rather than its value)
- Trivial type-following tests (asserting `isinstance` without behavioral checks)
- Mock-heavy tests that don't verify real behavior

Tests must cover edge cases and failure modes.

## Epistemic Protocol

Do not jump to conclusions. When uncertain:
1. Web search for authoritative sources
2. If still unclear, ask the user

Never guess at APIs, library behavior, or system semantics.

## Iteration Protocol

For every unit of work:
0. Read PROGRESS.md to recover context
1. Resolve uncertainties (web search, then ask user)
2. Plan incremental breakdown into transparent commits. Confirm plan with the user before proceeding
3. For each commit: first pin tests and behavior, validate with `/qa`
4. Then implement until `/qa` passes
5. Then commit
6. Run `/progress` to check if PROGRESS.md needs updating

## Commands

- `/qa` - Run type checker + tests + critical QA review of test quality
- `/progress` - Check if PROGRESS.md needs updating after a commit
- `/stack` - Configure project stack (language, type checker, test runner, tooling)

## Stack

<!-- Fill in with /stack or manually. /qa reads these to know what to run. -->

- Language:
- Type checker:
- Test runner:
- Package manager:
- Pre-commit hooks:
