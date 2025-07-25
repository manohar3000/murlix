import sys
import asyncio

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
    help_text = "[bold cyan]Available Commands:[/bold cyan]\n\n"
    
    for cmd in slash_commands.values():
        help_text += f"[green]{cmd.usage}[/green]\n"
        help_text += f"  {cmd.description}\n\n"
    
    help_text += "[dim]Tip: Use Ctrl+C to exit at any time[/dim]"
    
    console.print(Panel(
        help_text,
        title="Help",
        border_style="blue",
        box=box.ROUNDED,
        padding=(1, 2)
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
    # Note: Exit is handled in the chat loop, not here

def handle_sessions() -> None:
    """Handle the /sessions command to list available sessions."""
    console.print("[yellow]Use 'murlix load-chat' to see and select from available sessions.[/yellow]")
    console.print("[dim]The /sessions command cannot list sessions from within a running chat session.[/dim]")

def handle_clear() -> None:
    """Handle the /clear command to clear the screen."""
    from .utils.helper import clear_screen
    clear_screen()

def handle_new() -> None:
    """Handle the /new command to start a new session."""
    console.print("[yellow]To start a new session, please exit and run 'murlix' again.[/yellow]")

def handle_slash_command(command: str) -> None:
    """Handle a slash command."""
    if command in slash_commands:
        slash_command = slash_commands[command]
        slash_command.handler()
    else:
        available_commands = ", ".join(slash_commands.keys())
        console.print(f"[red]Unknown command:[/red] {command}")
        console.print(f"[dim]Available commands: {available_commands}[/dim]")
        console.print("[dim]Use /help for more information[/dim]")

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
    "/sessions": SlashCommand(
        name="sessions",
        description="List all available chat sessions",
        handler=handle_sessions,
        usage="/sessions"
    ),
    "/clear": SlashCommand(
        name="clear",
        description="Clear the terminal screen",
        handler=handle_clear,
        usage="/clear"
    ),
    "/new": SlashCommand(
        name="new",
        description="Start a new chat session",
        handler=handle_new,
        usage="/new"
    ),
}

