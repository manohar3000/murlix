import click
import asyncio
import sys
from dotenv import load_dotenv
from dataclasses import dataclass
from typing import Callable, Optional

from .slash_commands import handle_slash_command

from .utils import supress_warnings
from .utils.console import console
from .utils.helper import clear_screen

from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from rich import box
from rich.markdown import Markdown

from .session import SessionManager

from google.genai.types import Content, Part

load_dotenv()

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

async def interactive_mode() -> None:
    """Interactive mode for Murlix CLI."""
    clear_screen()
    display_welcome()
    input()
    clear_screen()

    ready_panel = Panel(
                "🚀 [bold green]Murlix[/bold green] is ready to chat!",
                border_style="green",
                padding=(0, 2)
            )
    
    session_manager = SessionManager()

    runner, session_id = await session_manager.create_session()

    console.print(ready_panel)
    
    try:
        while True:
            user_input = input("You: ")

            if user_input.startswith('/'):
                # Handle slash commands
                command = user_input.split()[0]
                handle_slash_command(command)
                continue

            message = Content(role='user', parts=[Part(text=user_input)])
            
            async for event in runner.run_async(
                            user_id=session_manager.user_id, 
                            session_id=session_id, 
                            new_message=message
                        ):
                show_agent_response(event)

    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)
    finally:
        if runner:
            await runner.close()
    
@click.group(invoke_without_command=True)
@click.option('--query', '-q', default=None, help='Query to process')
@click.pass_context
def main(ctx, query) -> None:
    """Murlix CLI tool"""
    if ctx.invoked_subcommand is None:
        if query:
            print(f"Query: {query}")
        else:
            asyncio.run(interactive_mode())
        
@main.command()
def continue_chat() -> None:
    """Continue the last session."""
    try:
        asyncio.run(resume_last_session())
    except KeyboardInterrupt:
        console.print("\n👋 [yellow]Goodbye![/yellow]")
    except Exception as e:
        console.print(f"[red]Error:[/red] {str(e)}")

@main.command()
def load_chat() -> None:
    """Show session picker and resume selected session."""
    try:
        asyncio.run(show_session_picker())
    except KeyboardInterrupt:
        console.print("\n👋 [yellow]Goodbye![/yellow]")
    except Exception as e:
        console.print(f"[red]Error:[/red] {str(e)}")

