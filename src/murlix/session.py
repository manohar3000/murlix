import os
from typing import List, Optional, Tuple
from datetime import datetime

from .utils.console import console

from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt

from google.adk.sessions import DatabaseSessionService, Session
from google.adk.runners import Runner
from google.genai.types import Content, Part

from .core_agent.agent import root_agent, mcp_toolsets

class SessionManager:
    def __init__(self):
        self.db_url = "sqlite:///./my_agent_data.db"
        self.app_name = str(os.getcwd()).split(os.sep)[-1]  # Use os.sep for cross-platform compatibility
        self.user_id = os.environ.get("USER_ID", "default_user")
        self.session_service = DatabaseSessionService(db_url=self.db_url)

    async def create_session(self) -> Tuple[Runner, str]:
        """Create a new session."""
        session = await self.session_service.create_session(
            app_name=self.app_name,
            user_id=self.user_id
        )
        
        runner = Runner(
            agent=root_agent,
            app_name=self.app_name,
            session_service=self.session_service
        )
        
        console.print(Panel(
            f"✨ [cyan]New session started:[/cyan] [dim]{session.id}[/dim]",
            border_style="cyan",
            padding=(0, 2)
        ))
        
        return runner, session.id
    
    async def list_sessions(self) -> List[Session]:
        """List all sessions for the current user."""
        try:
            sessions_response = await self.session_service.list_sessions(
                app_name=self.app_name,
                user_id=self.user_id
            )
            # Extract sessions from the response object
            if hasattr(sessions_response, 'sessions'):
                return sessions_response.sessions
            elif hasattr(sessions_response, 'session_ids'):
                # If only session IDs are returned, we need to fetch each session
                sessions = []
                for session_id in sessions_response.session_ids:
                    try:
                        session = await self.session_service.get_session(
                            app_name=self.app_name,
                            user_id=self.user_id,
                            session_id=session_id
                        )
                        if session:
                            sessions.append(session)
                    except Exception as inner_e:
                        console.print(f"[yellow]Warning: Could not fetch session {session_id}: {str(inner_e)}[/yellow]")
                return sessions
            else:
                # Fallback: try to treat it as an iterable
                return list(sessions_response) if sessions_response else []
        except Exception as e:
            console.print(f"[red]Error listing sessions:[/red] {str(e)}")
            return []
    
    async def get_latest_session(self) -> Optional[Session]:
        """Get the most recent session."""
        sessions = await self.list_sessions()
        if not sessions:
            return None
        
        # Sort by created_at timestamp (most recent first)
        # Handle cases where created_at might be None
        sessions.sort(key=lambda s: getattr(s, 'created_at', 0) or 0, reverse=True)
        return sessions[0]
    
    async def load_session(self, session_id: str) -> Optional[Runner]:
        """Load a specific session by ID."""
        try:
            session = await self.session_service.get_session(
                app_name=self.app_name,
                user_id=self.user_id,
                session_id=session_id
            )
            if not session:
                console.print(f"[red]Session not found:[/red] {session_id}")
                return None
            
            runner = Runner(
                agent=root_agent,
                app_name=self.app_name,
                session_service=self.session_service
            )
            
            console.print(Panel(
                f"📂 [green]Session loaded:[/green] [dim]{session_id}[/dim]",
                border_style="green",
                padding=(0, 2)
            ))
            
            return runner
        except Exception as e:
            console.print(f"[red]Error loading session:[/red] {str(e)}")
            return None
    
    async def continue_latest_session(self) -> Optional[Tuple[Runner, str]]:
        """Continue the most recent session."""
        latest_session = await self.get_latest_session()
        if not latest_session:
            console.print("[yellow]No previous sessions found. Starting a new session...[/yellow]")
            return await self.create_session()
        
        runner = await self.load_session(latest_session.id)
        if runner:
            return runner, latest_session.id
        return None
    
    def display_sessions_table(self, sessions: List[Session]) -> None:
        """Display sessions in a formatted table."""
        if not sessions:
            console.print("[yellow]No sessions found.[/yellow]")
            return
        
        table = Table(title="Available Sessions")
        table.add_column("Index", style="cyan", width=8)
        table.add_column("Session ID", style="green", width=20)
        table.add_column("Created At", style="yellow", width=20)
        table.add_column("Status", style="blue", width=12)
        
        for i, session in enumerate(sessions):
            # Format the created_at timestamp safely
            created_at = getattr(session, 'created_at', None)
            if created_at:
                try:
                    if hasattr(created_at, 'strftime'):
                        created_str = created_at.strftime("%Y-%m-%d %H:%M:%S")
                    else:
                        created_str = str(created_at)
                except:
                    created_str = "Unknown"
            else:
                created_str = "Unknown"
            
            # Get session status or ID as fallback info
            session_id = getattr(session, 'id', f'Session {i+1}')
            
            table.add_row(
                str(i + 1),
                session_id[:18] + "..." if len(session_id) > 20 else session_id,
                created_str,
                "Active"
            )
        
        console.print(table)

    async def reset_session(self):
        """Reset/clear session data (placeholder for future implementation)."""
        pass


async def resume_last_session():
    """Resume the most recent session."""
    from .chat import run_chat_loop  # Import here to avoid circular imports
    
    session_manager = SessionManager()
    result = await session_manager.continue_latest_session()
    
    if result:
        runner, session_id = result
        try:
            await run_chat_loop(runner, session_manager, session_id)
        finally:
            if runner:
                await runner.close()
    else:
        console.print("[red]Failed to resume session.[/red]")


async def show_session_picker():
    """Show session picker and resume selected session."""
    from .chat import run_chat_loop  # Import here to avoid circular imports
    
    session_manager = SessionManager()
    sessions = await session_manager.list_sessions()
    
    if not sessions:
        console.print("[yellow]No sessions found. Starting a new session...[/yellow]")
        runner, session_id = await session_manager.create_session()
        try:
            await run_chat_loop(runner, session_manager, session_id)
        finally:
            if runner:
                await runner.close()
        return
    
    # Sort sessions by created_at (most recent first)
    sessions.sort(key=lambda s: getattr(s, 'created_at', 0) or 0, reverse=True)
    
    session_manager.display_sessions_table(sessions)
    
    try:
        choice = Prompt.ask(
            "\n[cyan]Select a session by index (or 'n' for new session)[/cyan]",
            default="1"
        )
        
        if choice.lower() == 'n':
            runner, session_id = await session_manager.create_session()
        else:
            try:
                index = int(choice) - 1
                if 0 <= index < len(sessions):
                    selected_session = sessions[index]
                    runner = await session_manager.load_session(selected_session.id)
                    if not runner:
                        return
                    session_id = selected_session.id
                else:
                    console.print("[red]Invalid selection.[/red]")
                    return
            except ValueError:
                console.print("[red]Invalid input.[/red]")
                return
        
        try:
            await run_chat_loop(runner, session_manager, session_id)
        finally:
            if runner:
                await runner.close()
                
    except KeyboardInterrupt:
        console.print("\n[yellow]Selection cancelled.[/yellow]")
    
    