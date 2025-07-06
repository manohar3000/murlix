"""
CLI command handlers for Murlix.
"""
import asyncio
import click
from rich.console import Console
from google.genai.types import Content, Part

from .session import SessionManager
from .slash_commands import SlashCommandHandler

console = Console()

@click.group()
def cli():
    """Murlix - AI-powered coding assistant."""
    pass

@cli.command()
@click.argument('query', required=False)
def main(query: str = ""):
    """Start Murlix in interactive mode or run a single query."""
    try:
        if query:
            # Run single query mode
            asyncio.run(run_single_query(query))
        else:
            # Start interactive mode
            from main import main as interactive_main
            asyncio.run(interactive_main())
    except KeyboardInterrupt:
        console.print("\n👋 [yellow]Goodbye![/yellow]")
    except Exception as e:
        console.print(f"[red]Error:[/red] {str(e)}")

@cli.command()
def continue_chat():
    """Continue the last session."""
    try:
        asyncio.run(resume_last_session())
    except KeyboardInterrupt:
        console.print("\n👋 [yellow]Goodbye![/yellow]")
    except Exception as e:
        console.print(f"[red]Error:[/red] {str(e)}")

@cli.command()
def load_chat():
    """Show session picker and resume selected session."""
    try:
        asyncio.run(show_session_picker())
    except KeyboardInterrupt:
        console.print("\n👋 [yellow]Goodbye![/yellow]")
    except Exception as e:
        console.print(f"[red]Error:[/red] {str(e)}")

async def run_single_query(query: str):
    """Run a single query and exit."""
    session_manager = SessionManager(console)
    runner, session_id = await session_manager.create_session()
    
    try:
        # Create message
        message = Content(role='user', parts=[Part(text=query)])
        
        # Run query
        with console.status("[cyan]Thinking...[/cyan]"):
            async for event in runner.run_async(
                user_id=session_manager.user_id,
                session_id=session_id,
                new_message=message
            ):
                from cli.chat_loop import show_agent_response
                show_agent_response(console, event)
    finally:
        await session_manager.cleanup()

async def resume_last_session():
    """Resume the most recent session."""
    session_manager = SessionManager(console)
    sessions = await session_manager.list_sessions()
    
    if not sessions:
        console.print("[yellow]No existing sessions found. Starting new session...[/yellow]")
        runner, session_id = await session_manager.create_session()
    else:
        # Get most recent session
        runner, session_id = await session_manager.resume_session(sessions[0].id)
    
    if runner:
        from cli.chat_loop import run_chat_loop
        await run_chat_loop(console, runner, session_manager.user_id, session_id, None)
    else:
        console.print("[red]Failed to initialize session.[/red]")

async def show_session_picker():
    """Show interactive session picker."""
    session_manager = SessionManager(console)
    result = await session_manager.pick_session()
    
    if result:
        runner, session_id = result
        from cli.chat_loop import run_chat_loop
        await run_chat_loop(console, runner, session_manager.user_id, session_id, None)