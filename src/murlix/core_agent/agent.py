import os
from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.mcp_tool import StdioConnectionParams
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from mcp import StdioServerParameters
import subprocess
_allowed_path = os.getcwd()

def run_command(command: str):
    """
    Runs a terminal command and returns the output, error, and exit code.
    
    Args:
        command (str or list): The command to run. Example: "ls -l" or ["ls", "-l"]
    
    Returns:
        A tuple of (stdout, stderr, exit_code)
    """
    try:
        result = subprocess.run(
            command,
            shell=isinstance(command, str),  # shell=True only if command is a string
            text=True,
            capture_output=True
        )
        return {
            "stdout": result.stdout,
            "stderr": result.stderr,
            "exit_code": result.returncode
        }
    except Exception as e:
        return {
            "stdout": "",
            "stderr": str(e),
            "exit_code": -1
        }
 

mcp_toolsets = [
    MCPToolset(
        connection_params=StdioConnectionParams(
            server_params=StdioServerParameters(
                command="npx",
                args=["-y",
                     "@modelcontextprotocol/server-filesystem",
                     _allowed_path,
                ],
            ),
            timeout=5000000,
        ),
    ),

    MCPToolset(
                connection_params=StdioConnectionParams(
                    server_params=StdioServerParameters(
                        command='npx',
                        args=[
                            '-y',  # Arguments for the command
                             "@upstash/context7-mcp",
                        ],
                    ),
                     timeout=5000000,
               ),
             ),
 
    run_command     
 ]


root_agent = LlmAgent(
    model='gemini-2.0-flash',
    name='HelpfulAssistant',
    description="you are a helpful coding assistant.",
    instruction=f"""
You are an AI assistant specialized in software development with access to these tools:

"file_system":
- Read, write, list, and search files/directories
- Move and manage files
- Get file metadata and properties
- Only operate within: {_allowed_path}

"context7":
- Access current documentation for any package/library
- Retrieve code examples and best practices
- Get version-specific implementation details
- Verify API compatibility and usage

"run_command":
- Execute terminal commands safely
- Handle both string and list command formats
- Capture stdout and stderr output
- Return command execution status
- Provide error handling for failed commands
- Support command timeouts and process management

Guidelines:
1. Always verify file paths exist before operations
2. Create descriptive commit messages with prefix (feat:, fix:, docs:, etc.)
3. Use Context7 to ensure up-to-date and correct implementations
4. Provide explanations for significant code changes
5. Follow project's existing code style and patterns
6. Handle errors gracefully and provide meaningful feedback

Maintain clean, efficient, and well-documented code while operating strictly within {_allowed_path}.
    """,
    tools=mcp_toolsets,
)