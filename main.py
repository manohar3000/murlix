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

# Load environment variables
load_dotenv()

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

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

async def create_attractive_input(console, prompt_text, slash_handler):
    """Create an attractive input prompt with styling and autocomplete"""
    # Create a styled prompt
    prompt = Text()
    prompt.append("╭─ ", style="cyan")
    prompt.append(f"{prompt_text}", style="bold bright_cyan")
    prompt.append(" ─╮", style="cyan")
    
    console.print(prompt)
    
    # Create input line with cursor styling
    input_prompt = Text()
    input_prompt.append("│ ", style="cyan")
    console.print(input_prompt, end="")
    
    # Get all available commands and their descriptions
    choices = []
    for cmd, info in slash_handler.commands.items():
        choices.append(cmd)
    # Get input with autocomplete
    user_input = await questionary.autocomplete(
        "",
        choices=choices,
        default="",
        qmark="▶ ",
        match_middle=True,
        ignore_case=True,
        complete_style="COLUMN",
        meta_information={cmd: info.description for cmd, info in slash_handler.commands.items()},
        style=questionary.Style([
            ('qmark', '#00FF00'),  # Bright green arrow
            ('completion-menu', 'bg:#2a2a2a #87ceeb'),  # Dark gray bg, light blue text
            ('completion-menu-selection', 'bg:#404040 #ffffff'),  # Medium gray selection
            ('answer', '#87ceeb bold'),  # Light blue for user input
            ('question', '#87ceeb'),  # Light blue for prompt
        ])
    ).ask_async()
    
    if user_input is None:  # Handle Ctrl+C
        return "exit"
    
    # Create closing line
    closing = Text()
    closing.append("╰─", style="cyan")
    closing.append("─" * (len(user_input) + 4), style="cyan")
    closing.append("─╯", style="cyan")
    console.print(closing)
    
    return user_input

def show_agent_response(console, event):
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

async def run_chat_loop(console, runner, user_id, session_id, mcp_toolsets):
    """Run the main chat loop with the agent"""
    slash_handler = SlashCommandHandler(console)
    
    try:
        while True:
            console.print()
            user_input = await create_attractive_input(console, user_id or "You", slash_handler)
            
            if user_input.lower() in ['exit', 'quit', 'bye']:
                farewell_panel = Panel(
                    "👋 [yellow]Thanks for using Murlix![/yellow]\n[dim]Session saved automatically[/dim]",
                    border_style="yellow",
                    box=box.MINIMAL,
                    padding=(0, 1)
                )
                console.print(farewell_panel)
                break
            
            if not user_input.strip():
                continue

            # Handle slash commands
            result = await slash_handler.handle_command(user_input)
            if result is None:  # Command was handled
                continue
                
            # Regular message
            console.print()
            message = Content(role='user', parts=[Part(text=user_input)])
                        
            try:
                with console.status("[bold cyan]Thinking...[/bold cyan]", spinner="material"):
                    async for event in runner.run_async(
                        user_id=user_id, 
                        session_id=session_id, 
                        new_message=message
                    ):                    
                        show_agent_response(console, event)
                    
            except Exception as e:
                error_panel = Panel(
                    f"❌ [red]Error processing request:[/red] {str(e)}",
                    border_style="red",
                    box=box.ROUNDED,
                    padding=(0, 2)
                )
                console.print(error_panel)
                
    except KeyboardInterrupt:
        console.print("\n👋 [yellow]Chat interrupted. Goodbye![/yellow]")
    finally:
        # Clean up toolsets
        if mcp_toolsets:
            for toolset in mcp_toolsets:
                await toolset.close()

async def main():
    """Main function to run Murlix"""
    console = Console()
    
    try:
        # Show welcome screen
        clear_screen()
        display_welcome()
        input()
        clear_screen()
        
        # Show ready message
        ready_panel = Panel(
            "✨ [bold cyan]Murlix[/bold cyan] is ready to chat.\nType [green]/help[/green] to see available commands.",
            box=box.ROUNDED,
            border_style="bright_cyan",
            expand=False,
            padding=(0, 0)
        )
        
        # Initialize session
        session_manager = SessionManager(console)
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
    try:
        # Import and run CLI
        from cli import cli
        cli()
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
    except Exception as e:
        print(f"💥 Exiting with error: {e}")