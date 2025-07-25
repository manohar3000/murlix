"""Murlix - A beautiful CLI chat interface."""

import click
import asyncio
import sys
from dotenv import load_dotenv

from .utils import supress_warnings
from .utils.helper import clear_screen
from .utils.console import console
from .ui import display_welcome, show_ready_message
from .session import SessionManager, resume_last_session, show_session_picker
from .chat import run_chat_loop

load_dotenv()


async def interactive_mode() -> None:
    """Interactive mode for Murlix CLI."""
    clear_screen()
    display_welcome()
    input()
    clear_screen()

    show_ready_message()
    
    session_manager = SessionManager()
    runner, session_id = await session_manager.create_session()

    try:
        await run_chat_loop(runner, session_manager, session_id)
    finally:
        if runner:
            await runner.close()


@click.group(invoke_without_command=True)
@click.option('--query', '-q', default=None, help='Query to process')
@click.pass_context
def main(ctx, query) -> None:
    """Murlix CLI tool - A beautiful AI chat interface."""
    if ctx.invoked_subcommand is None:
        if query:
            console.print(f"[cyan]Query:[/cyan] {query}")
            # TODO: Add single query processing functionality
        else:
            try:
                asyncio.run(interactive_mode())
            except KeyboardInterrupt:
                console.print("\n👋 [yellow]Goodbye![/yellow]")
            except Exception as e:
                console.print(f"[red]Error:[/red] {str(e)}")


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


if __name__ == "__main__":
    main()

