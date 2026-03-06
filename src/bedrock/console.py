from rich.console import Console

console = Console(highlight=False)

def info(msg: str) -> None:
    console.print(f"[bold]bedrock:[/bold] {msg}")

def warn(msg: str) -> None:
    console.print(f"[bold yellow]bedrock:[/bold yellow] {msg}", stderr=True)

def error(msg: str) -> None:
    console.print(f"[bold red]bedrock:[/bold red] {msg}", stderr=True)
