"""
Session management for Murlix CLI.
"""
import os
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional, Tuple

from google.adk.sessions import DatabaseSessionService
from google.adk.runners import Runner
import questionary
from rich.console import Console
from rich.panel import Panel

from core_agent.agent import root_agent, mcp_toolsets

@dataclass
class SessionInfo:
    """Information about a chat session."""
    id: str
    last_update_time: datetime
    session_summary: Optional[str] = None

class SessionManager:
    """Manages chat sessions for Murlix."""
    
    def __init__(self, console: Console):
        self.console = console
        self.db_url = "sqlite:///./my_agent_data.db"
        self.app_name = str(os.getcwd()).split("\\")[-1]
        self.user_id = os.environ.get("USER_ID", "default_user")
        self.session_service = DatabaseSessionService(db_url=self.db_url)
    
    async def list_sessions(self) -> List[SessionInfo]:
        """Get list of available sessions."""
        sessions = await self.session_service.list_sessions(
            app_name=self.app_name,
            user_id=self.user_id
        )
        return [
            SessionInfo(
                id=s.id,
                last_update_time=datetime.fromtimestamp(s.last_update_time),
                session_summary=s.state.get("session_summary", "")
            )
            for s in sessions.sessions
        ] if sessions else []
    
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
        
        self.console.print(Panel(
            f"✨ [cyan]New session started:[/cyan] [dim]{session.id}[/dim]",
            border_style="cyan",
            padding=(0, 2)
        ))
        
        return runner, session.id
    
    async def resume_session(self, session_id: str) -> Tuple[Runner, str]:
        """Resume an existing session."""
        runner = Runner(
            agent=root_agent,
            app_name=self.app_name,
            session_service=self.session_service
        )
        
        self.console.print(Panel(
            f"🔄 [green]Resumed session:[/green] [dim]{session_id}[/dim]",
            border_style="green",
            padding=(0, 2)
        ))
        
        return runner, session_id
    
    async def pick_session(self) -> Optional[Tuple[Runner, str]]:
        """Show interactive session picker."""
        sessions = await self.list_sessions()
        
        if not sessions:
            self.console.print(Panel(
                "✨ [yellow]No existing sessions found.[/yellow]",
                border_style="yellow",
                padding=(0, 2)
            ))
            return await self.create_session()
        
        # Format session choices for questionary select
        choices = []
        for i, s in enumerate(sessions):
            # Format timestamp nicely
            timestamp = s.last_update_time.strftime('%d-%m-%Y %H:%M:%S')
            
            # Create summary text
            summary = f"💬 {s.session_summary[:50]}..." if s.session_summary else ""
            
            title = f"Session ID: {s.id[:7]} • Last Updated: {timestamp}  {summary}"
            choices.append(questionary.Choice(title=title, value=s.id))
            
        # Add option for new session with special styling
        choices.append(questionary.Choice(
            title="✨ Start new session",
            value="new"
        ))
        
        # Show picker with custom styling
        result = await questionary.select(
            message="Select a session to resume",
            choices=choices,
            qmark="🔍",
            instruction="(Use ↑↓ arrows and press Enter)",
            use_indicator=True,
            style=questionary.Style([
                ('qmark', 'fg:cyan bold'),
                ('question', 'fg:cyan bold'),
                ('pointer', 'fg:cyan bold'),
                ('highlighted', 'fg:cyan bold'),
                ('answer', 'fg:#ffffff'),         
            ])
        ).ask_async()
        
        if result == "new":
            return await self.create_session()
        elif result:
            return await self.resume_session(result)
            
        return None
        
    async def cleanup(self):
        """Clean up resources."""
        for toolset in mcp_toolsets:
            await toolset.close() 

    async def clear_session(self, session_id: str) -> Tuple[Runner, str]:
        """Clear a session and return a new Runner instance."""
        # Delete the old session
        await self.session_service.delete_session(
            app_name=self.app_name,
            user_id=self.user_id,
            session_id=session_id
        )
        
        # Create a new session with the same ID
        new_session = await self.session_service.create_session(
            app_name=self.app_name,
            user_id=self.user_id,
            session_id=session_id
        )
        
        # Create a new Runner instance for the cleared session
        new_runner = Runner(
            agent=root_agent,
            app_name=self.app_name,
            session_service=self.session_service
        )
        
        return new_runner, session_id