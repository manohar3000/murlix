"""Enhanced input handler with auto-completion for Murlix."""

from typing import List, Optional
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.styles import Style
from prompt_toolkit.shortcuts import CompleteStyle
from prompt_toolkit.formatted_text import HTML
from rich.text import Text

from .slash_commands import slash_commands
from .utils.console import console


class SlashCommandCompleter(Completer):
    """Auto-completer for slash commands with descriptions."""
    
    def get_completions(self, document, complete_event):
        """Get completions for slash commands."""
        text = document.text_before_cursor
        
        # Only provide completions if we're at the start or after a slash
        if text.startswith('/') or (len(text) == 0):
            # If text starts with '/', remove it for matching
            search_text = text[1:] if text.startswith('/') else text
            
            for command_name, command_obj in slash_commands.items():
                # Remove the '/' from command name for matching
                cmd_name = command_name[1:]
                
                if cmd_name.startswith(search_text.lower()):
                    # Create completion with description
                    yield Completion(
                        text=command_name,  # Include the '/' in completion
                        start_position=-len(text),
                        display=f"{command_name} - {command_obj.description}",
                        style="class:command"
                    )


def create_input_style():
    """Create a custom style for the input prompt."""
    return Style.from_dict({
        # Main prompt styling
        'prompt': '#00aa00 bold',  # Green prompt
        'input': '#ffffff',       # White input text
        
        # Completion menu styling  
        'completion-menu.completion': 'bg:#008888 #ffffff',
        'completion-menu.completion.current': 'bg:#00aaaa #000000 bold',
        'completion-menu.meta.completion': 'bg:#999999 #000000',
        'completion-menu.meta.completion.current': 'bg:#aaaaaa #000000 bold',
        
        # Command styling in completions
        'command': '#00ffff bold',  # Cyan for commands
        
        # Scrollbar
        'scrollbar.background': 'bg:#88aaaa',
        'scrollbar.button': 'bg:#222222',
    })


def get_prompt_message():
    """Get the formatted prompt message."""
    return HTML('<prompt>┌─ Murlix ─┐</prompt>\n<prompt>└─➤</prompt> ')


async def get_user_input() -> str:
    """Get user input with enhanced styling and auto-completion."""
    
    # Create completer and style
    completer = SlashCommandCompleter()
    style = create_input_style()
    
    # Create a prompt session for async input
    session = PromptSession(
        message=get_prompt_message(),
        completer=completer,
        complete_style=CompleteStyle.MULTI_COLUMN,
        style=style,
        mouse_support=True,
        complete_while_typing=True,
        enable_history_search=True,
        multiline=False,
        wrap_lines=True,
    )
    
    try:
        # Get input with auto-completion (async)
        user_input = await session.prompt_async()
        
        # Show confirmation of received input
        if user_input.strip():
            display_input_confirmation(user_input.strip())
        
        return user_input.strip()
        
    except (EOFError, KeyboardInterrupt):
        # Handle Ctrl+C or Ctrl+D gracefully
        console.print("\n[yellow]Goodbye! 👋[/yellow]")
        return "/quit"


def display_input_confirmation(user_input: str):
    """Display a subtle confirmation that input was received."""
    from rich.panel import Panel
    from rich import box
    
    # Different styling for commands vs regular messages
    if user_input.startswith('/'):
        confirmation_text = Text()
        confirmation_text.append("⚡ ", style="yellow")
        confirmation_text.append("Command: ", style="dim")
        confirmation_text.append(user_input, style="cyan bold")
    else:
        confirmation_text = Text()
        confirmation_text.append("💬 ", style="blue")
        confirmation_text.append("Message: ", style="dim")
        # Truncate long messages in confirmation
        display_text = user_input[:100] + "..." if len(user_input) > 100 else user_input
        confirmation_text.append(display_text, style="white")
    
    # Create a minimal panel for confirmation
    panel = Panel(
        confirmation_text,
        box=box.MINIMAL,
        border_style="dim",
        padding=(0, 1)
    )
    
    console.print(panel)
    console.print()


def display_command_help_hint():
    """Display a helpful hint about available commands."""
    hint_text = Text()
    hint_text.append("💡 ", style="yellow")
    hint_text.append("Tip: Type ", style="dim")
    hint_text.append("/", style="cyan bold")
    hint_text.append(" to see available commands with auto-completion", style="dim")
    
    console.print(hint_text)
    console.print()


def display_enhanced_welcome():
    """Display an enhanced welcome message with input instructions."""
    from rich.panel import Panel
    from rich import box
    from rich.align import Align
    
    # Welcome content with input instructions
    welcome_content = Text()
    welcome_content.append("🎯 ", style="bright_green")
    welcome_content.append("Enhanced Input Features:\n", style="bold bright_green")
    welcome_content.append("\n")
    welcome_content.append("• ", style="bright_blue")
    welcome_content.append("Auto-completion: ", style="bold")
    welcome_content.append("Start typing commands with ", style="dim")
    welcome_content.append("/", style="cyan")
    welcome_content.append("\n")
    welcome_content.append("• ", style="bright_blue") 
    welcome_content.append("Command descriptions: ", style="bold")
    welcome_content.append("See helpful descriptions in the completion menu\n", style="dim")
    welcome_content.append("• ", style="bright_blue")
    welcome_content.append("History: ", style="bold") 
    welcome_content.append("Use ↑/↓ arrows to navigate previous inputs\n", style="dim")
    welcome_content.append("• ", style="bright_blue")
    welcome_content.append("Multi-line: ", style="bold")
    welcome_content.append("Use Alt+Enter for multi-line input\n", style="dim")
    
    # Create an attractive panel
    panel = Panel(
        Align.left(welcome_content),
        title="✨ Enhanced Input Ready",
        title_align="left",
        border_style="bright_green",
        box=box.ROUNDED,
        padding=(1, 2)
    )
    
    console.print(panel)
    console.print()