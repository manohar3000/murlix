"""
Main entry point for Murlix.
"""
import os
import sys
import asyncio
from dotenv import load_dotenv
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from rich import box
from rich.markdown import Markdown
from google.genai.types import Content, Part
import questionary

import utils
from cli import SessionManager, SlashCommandHandler
from cli.chat_loop import run_chat_loop, clear_screen

# Load environment variables
load_dotenv()

def create_ascii_logo():
    """Create the MURLIX ASCII art logo"""
    logo = """
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
    console = Console()
    
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
        expand=False,
        border_style="bright_cyan",
        padding=(0, 2)
    )
    
    logo_panel = Panel(
        Align.left(logo_text),
        box=box.MINIMAL,
        padding=(0, 1),
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

async def main():
    """Main entry point."""
    console = Console()

    try:
        clear_screen()
        # Display welcome screen
        display_welcome()
        input()  # Wait for Enter
        clear_screen()
    
    
    # Initialize session manager
        session_manager = SessionManager(console)
        ready_panel = Panel(
                "🚀 [bold green]Murlix[/bold green] is ready to chat!",
                border_style="green",
                padding=(0, 2)
            )

        with console.status("[bold cyan]Murlix[/bold cyan] is initializing \n", spinner="material"):
                runner, session_id = await session_manager.create_session()

        console.print(ready_panel)
        

        if runner:
            await run_chat_loop(console, runner, session_manager.user_id, session_id, None)
        else:
            console.print("❌ [red]Failed to initialize. Exiting...[/red]")        
        
    except Exception as e:
            error_panel = Panel(
                f"❌ [red]Unexpected error:[/red] {str(e)}",
                title="💥 Fatal Error",
                border_style="red",
                box=box.ROUNDED,
                padding=(0, 2)
            )
            console.print(error_panel)
            sys.exit(1)

if __name__ == "__main__":
    asyncio.run(main())