import os

from .utils.console import console

from rich.panel import Panel

from google.adk.sessions import DatabaseSessionService
from google.adk.runners import Runner
from google.genai.types import Content, Part

from .core_agent.agent import root_agent, mcp_toolsets

class SessionManager:
    def __init__(self):
        self.db_url = "sqlite:///./my_agent_data.db"
        self.app_name = str(os.getcwd()).split("\\")[-1]
        self.user_id = os.environ.get("USER_ID", "default_user")
        self.session_service = DatabaseSessionService(db_url=self.db_url)

    async def create_session(self):
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
    
    async def reset_session():
        pass
    
    