"""Rich console output utilities."""

from rich.console import Console

console = Console()


def info(message):
    console.print(f"[cyan][INFO][/cyan] {message}")


def warn(message):
    console.print(f"[yellow][WARN][/yellow] {message}")


def error(message):
    console.print(f"[red][ERROR][/red] {message}")


def success(message):
    console.print(f"[green][SUCCESS][/green] {message}")
