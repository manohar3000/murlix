"""
Slash command handlers for Murlix interactive chat.
"""
from typing import Dict, Callable, Optional, Any
from dataclasses import dataclass
import questionary
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.markdown import Markdown

from core_agent.models import model_manager

@dataclass
class SlashCommand:
    """Represents a slash command."""
    name: str
    description: str
    handler: Callable
    usage: str = ""

class SlashCommandHandler:
    """Handles slash commands in interactive chat."""
    
    def __init__(self, console: Console):
        self.console = console
        self.commands: Dict[str, SlashCommand] = {}
        self._register_commands()
    
    def _register_commands(self):
        """Register available slash commands."""
        self.commands = {
            "/help": SlashCommand(
                name="help",
                description="Show list of available commands",
                handler=self.handle_help,
                usage="/help"
            ),
            "/model": SlashCommand(
                name="model",
                description="Show/select AI model",
                handler=self.handle_model,
                usage="/model list|set <model_name>"
            ),
            "/clear": SlashCommand(
                name="clear",
                description="Clear current conversation history",
                handler=self.handle_clear
            )
        }
    
    async def handle_command(self, command: str, *args) -> Optional[str]:
        """
        Handle a slash command. Returns None if command was handled,
        or the original input if it wasn't a command.
        """
        if not command.startswith("/"):
            return command
            
        parts = command.split()
        cmd = parts[0].lower()
        args = parts[1:] if len(parts) > 1 else []
        
        if cmd in self.commands:
            await self.commands[cmd].handler(*args)
            return None
            
        self.console.print(f"[red]Unknown command: {cmd}[/red]")
        return None
    
    async def handle_help(self, *args):
        """Show help information."""
        table = Table(title="Murlix Help", border_style="cyan")
        table.add_column("Command", style="bold cyan", no_wrap=True)
        table.add_column("Description", style="white")
        table.add_column("Usage", style="dim")
        
        for cmd, info in self.commands.items():
            usage = info.usage if info.usage else "N/A"
            table.add_row(cmd, info.description, usage)
        
        self.console.print(table)
    
    async def handle_model(self, *args):
        """Handle model selection."""
        if not args:
            # Show current model
            model = model_manager.current_model
            self.console.print(Panel(
                f"Current model: [cyan]{model.display_name}[/cyan]\n"
                f"[dim]{model.description}[/dim]",
                title="Model Info",
                border_style="cyan"
            ))
            return
            
        if args[0] == "list":
            # List available models
            models_text = "# Available Models\n\n"
            for model in model_manager.available_models:
                models_text += f"## {model.display_name}\n"
                models_text += f"{model.description}\n"
                if model.is_default:
                    models_text += "*Default model*\n"
                models_text += "\n"
            
            self.console.print(Panel(
                Markdown(models_text),
                title="Available Models",
                border_style="cyan"
            ))
            return
            
        if args[0] == "set" and len(args) > 1:
            # Set model
            model_name = args[1]
            new_model = model_manager.set_model(model_name)
            
            if new_model:
                self.console.print(
                    f"[green]Switched to model:[/green] {new_model.display_name}"
                )
            else:
                self.console.print(f"[red]Unknown model: {model_name}[/red]")
            return
            
        self.console.print("[yellow]Invalid usage. Try /help for usage info.[/yellow]")
    
    async def handle_clear(self, *args):
        """Clear conversation history."""
        # Note: Actual history clearing is handled by the session manager
        self.console.print("[green]Conversation history cleared.[/green]") 