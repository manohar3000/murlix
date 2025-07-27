import sys
from typing import Optional

from google.genai.types import Content, Part
from google.adk.runners import Runner

from .utils.console import console
from .session import SessionManager
from .slash_commands import handle_slash_command
from .ui import show_agent_response
from .input_handler import get_user_input, display_enhanced_welcome, display_command_help_hint


async def run_chat_loop(runner: Runner, session_manager: SessionManager, session_id: str) -> None:
    """Run the main chat interaction loop."""
    
    # Display enhanced welcome and help hint
    display_enhanced_welcome()
    display_command_help_hint()
    
    try:
        while True:
            user_input = get_user_input()

            if user_input.startswith('/'):
                # Handle slash commands
                command = user_input.split()[0]
                
                # Check if it's a quit command to break the loop
                if command == '/quit':
                    handle_slash_command(command)
                    break
                else:
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
        return
    except Exception as e:
        print(f"An error occurred: {e}")
        return