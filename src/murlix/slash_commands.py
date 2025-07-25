import sys

from typing import Dict, Callable, Optional, Any
from dataclasses import dataclass

from rich.panel import Panel
from rich import box

from .utils.console import console

@dataclass
class SlashCommand:
    """Represents a slash command."""
    name: str
    description: str
    handler: Callable
    usage: str = ""

def handle_help() -> None:
    """Display help information for slash commands."""
    help_text = "Available commands:\n"
    for cmd in slash_commands.values():
        help_text += f"- {cmd.name}: {cmd.description} (Usage: {cmd.usage})\n"
    
    console.print(Panel(
        help_text,
        title="Help",
        border_style="blue",
        box=box.ROUNDED,
        padding=(0, 2)
    ))
def handle_quit() -> None:
    """Handle the /quit command."""
    farewell_panel = Panel(
        "👋 [yellow]Thanks for using Murlix![/yellow]\n[dim]Session saved automatically[/dim]",
        border_style="yellow",
        box=box.MINIMAL,
        padding=(0, 1)
    )
    console.print(farewell_panel)
    sys.exit(0)    

def handle_slash_command(command: str) -> None:
    """Handle a slash command."""
    if command in slash_commands:
        slash_command = slash_commands[command]
        slash_command.handler()
    else:
        console.print(f"[red]Unknown command:[/red] {command}")

slash_commands = {
            "/help": SlashCommand(
                name="help",
                description="Show list of available commands",
                handler=handle_help,
                usage="/help"
            ),
            "/quit": SlashCommand(
                name="quit",
                description="Exit the interactive mode",
                handler=handle_quit,
                usage="/quit"
            ),
        }

