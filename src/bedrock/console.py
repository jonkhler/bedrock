import sys

from rich.console import Console

console = Console(highlight=False)
err_console = Console(highlight=False, stderr=True)

def info(msg: str) -> None:
    console.print(f"[bold]bedrock:[/bold] {msg}")

def warn(msg: str) -> None:
    err_console.print(f"[bold yellow]bedrock:[/bold yellow] {msg}")

def error(msg: str) -> None:
    err_console.print(f"[bold red]bedrock:[/bold red] {msg}")
