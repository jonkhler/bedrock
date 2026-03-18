# CLI Reference

## bedrock new

Scaffold a new project.

```
bedrock new [OPTIONS] DIRECTORY [PROMPT]
```

| Argument | Description |
|---|---|
| `DIRECTORY` | Target directory (created if needed) |
| `PROMPT` | Optional stack description, e.g. `"Python 3.13, uv, pyright strict, pytest"` |

| Option | Description |
|---|---|
| `--name TEXT` | Project name (defaults to directory basename) |
| `--bare` | Copy scaffold files only, skip stack configuration |
| `--headless` | Run `/stack` non-interactively and exit |
| `--force` | Overwrite existing `CLAUDE.md` and `PROGRESS.md` |

**Examples:**

```sh
bedrock new ~/dev/my-app "Python 3.13, uv, pyright strict, pytest"
bedrock new --name myapp ~/dev/my-app
bedrock new --bare ~/dev/my-app
```

## bedrock sync

Sync bedrock files into a project directory.

```
bedrock sync [OPTIONS] [DIRECTORY]
```

| Argument | Description |
|---|---|
| `DIRECTORY` | Target directory (defaults to `.`) |

| Option | Description |
|---|---|
| `--force` | Overwrite existing `CLAUDE.md` and `PROGRESS.md` |

**Examples:**

```sh
cd my-project && bedrock sync
bedrock sync ~/dev/my-project
bedrock sync --force
```

## bedrock update

Pull latest bedrock templates and reinstall the CLI.

```
bedrock update
```

After updating, run `bedrock sync` in your projects to pick up new rules and commands.

## bedrock version

Show installed version (git short hash).

```
bedrock version
```
