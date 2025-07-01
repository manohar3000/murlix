import os
from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.mcp_tool import StdioConnectionParams
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from mcp import StdioServerParameters

_allowed_path = os.path.dirname(os.path.abspath(__file__))

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
                             "@upstash/context7-mcp@latest",
                        ],
                    ),
                     timeout=5000000,
               ),
             ),

#     MCPToolset(
#                 connection_params=StdioConnectionParams(
#                     server_params=StdioServerParameters(
#                         command='uvx',
#                         args=[
#                             "mcp-server-git",
#                         ],
#                     ),
#                 ),
#             ),            
 ]


root_agent = LlmAgent(
    model='gemini-2.0-flash',
    name='HelpfulAssistant',
    description="you are a helpful coding assistant.",
    instruction=f"""
You are an AI assistant with access to:

"file_system" — read, write, list, search, move files and directories, and get file metadata.

"context7" — retrieve up-to-date, version-specific documentation and examples for any code or library.

"git" — commit, branch, diff, log, status, and manage repository history.

Use these tools proactively to produce accurate, context-aware, and practical responses. Always respect the specified file paths and repository structure, keep commits clear and well-described, and leverage Context7 for up-to-date technical details. Aim for concise, correct, and helpful outputs.
Allowed directory: {_allowed_path}
    """,
    tools=mcp_toolsets,
)