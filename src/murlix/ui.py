"""UI components and display utilities for Murlix."""

from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from rich import box
from rich.markdown import Markdown

from .utils.console import console


def create_ascii_logo():
    """Create the MURLIX ASCII art logo with flute"""
    logo = """
┌────────┬───────────────────┬───┐
│        │  ●   ●   ●   ●   ● │   │  ♪♫♪ ♪♫♪
└────────┴───────────────────┴───┘

███╗   ███╗██╗   ██╗██████╗ ██╗     ██╗██╗  ██╗
████╗ ████║██║   ██║██╔══██╗██║     ██║╚██╗██╔╝
██╔████╔██║██║   ██║██████╔╝██║     ██║ ╚███╔╝ 
██║╚██╔╝██║██║   ██║██╔══██╗██║     ██║ ██╔██╗ 
██║ ╚═╝ ██║╚██████╔╝██║  ██║███████╗██║██╔╝ ██╗
╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═╝
"""
    return logo


def display_welcome():
    """Display the beautiful welcome screen"""
    
    # Create welcome message
    welcome_text = Text("✨ Welcome to Murlix", style="bold cyan")
    
    # Create the ASCII logo with gradient colors
    logo = create_ascii_logo()
    logo_text = Text()
    
    # Apply gradient colors to the logo
    colors = ["bright_cyan", "cyan", "blue", "bright_blue"]
    lines = logo.strip().split('\n')
    
    for i, line in enumerate(lines):
        color = colors[i % len(colors)]
        logo_text.append(line + '\n', style=color)
    
    # Create continue message
    continue_text = Text("Press Enter to continue", style="dim white")
    
    # Create panels
    welcome_panel = Panel(
        Align.left(welcome_text),
        box=box.ROUNDED,
        border_style="bright_cyan",
        expand=False,
        padding=(0, 2)
    )
    
    logo_panel = Panel(
        Align.left(logo_text),
        box=box.MINIMAL,
        padding=(0, 0),
    )
    
    continue_panel = Panel(
        Align.left(continue_text),
        box=box.MINIMAL,
        padding=(0, 0)
    )
    
    # Display everything
    console.print()
    console.print(welcome_panel)
    console.print(logo_panel)
    console.print(continue_panel)


def show_agent_response(event):
    """Display agent responses with beautiful formatting"""
    
    if event.content and event.content.parts:
        for part in event.content.parts:
            if hasattr(part, 'function_call') and part.function_call:
                # Show tool calls with nice formatting
                tool_panel = Panel(
                    f"[cyan]{part.function_call.name}[/cyan]([dim]{part.function_call.args}[/dim])",
                    title="Tool Call",
                    title_align="left",
                    border_style="yellow",
                    box=box.ROUNDED,
                    padding=(0, 2),
                )
                console.print(tool_panel)
                console.print()

            elif hasattr(part, 'function_response') and part.function_response:
                if part.function_response.response['result'].isError:
                    error_panel = Panel(
                        f"❌ [red]Error in tool call[/red]",
                        border_style="red",
                        box=box.ROUNDED,
                        padding=(0, 2)
                    )
                    console.print(error_panel)
                    console.print()

                else:
                    tool_success_panel = Panel(
                    f"[cyan] Tool Called Successfully [/cyan]",
                    border_style="green",
                    box=box.ROUNDED,
                    padding=(0, 2),
                )
                    console.print(tool_success_panel)
                    console.print()

    if event.is_final_response():
        if (
            event.content
            and event.content.parts
            and hasattr(event.content.parts[0], "text")
            and event.content.parts[0].text
        ):
            final_response = event.content.parts[0].text.strip()
            
            # Display final response in an attractive panel
            response_panel = Panel(
                Markdown(final_response),
                title="Murlix",
                title_align="left",
                border_style="bright_green",
                box=box.ROUNDED,
                padding=(0, 2)
            )
            console.print(response_panel)


def show_ready_message():
    """Display the ready message when chat starts."""
    ready_panel = Panel(
        "🚀 [bold green]Murlix[/bold green] is ready to chat!\n[dim]Enhanced input with auto-completion enabled[/dim]",
        border_style="green",
        padding=(0, 2)
    )
    console.print(ready_panel)


def show_input_separator():
    """Show a subtle separator before user input."""
    separator_text = Text("─" * 50, style="dim blue")
    console.print(separator_text)