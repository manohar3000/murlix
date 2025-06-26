import os

from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.mcp_tool import StdioConnectionParams
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from mcp import StdioServerParameters

_allowed_path = os.path.dirname(os.path.abspath(__file__))

mcp_toolsets = [
    
]

root_agent = LlmAgent(
    model='gemini-2.0-flash',
    name='file_system_agent',
    instruction=f"""\
Help user accessing their file systems.

Allowed directory: {_allowed_path}
    """,
    tools=mcp_toolsets,
)