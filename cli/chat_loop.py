"""
Chat loop functionality for Murlix.
"""
import os
import questionary
from rich.panel import Panel
from rich.text import Text
from rich.markdown import Markdown
from rich import box
from google.genai.types import Content, Part

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

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
        match_middle=False,
        ignore_case=True,
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

            elif hasattr(part, 'function_response') and part.function_response:
                pass

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
    from cli.slash_commands import SlashCommandHandler  # Import here to avoid circular dependency
    
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
            result = await slash_handler.handle_command(user_input, session_id)
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
    