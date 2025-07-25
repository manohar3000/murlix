import os

from google.adk.agents.llm_agent import LlmAgent

_allowed_path = os.path.dirname(os.path.abspath(__file__))

# Simple agent without MCP tools for now
# You can add working MCP toolsets here later
mcp_toolsets = []

root_agent = LlmAgent(
    model='gemini-2.0-flash',
    name='Murlix_Assistant',
    instruction=f"""\
You are Murlix, a helpful AI assistant. You can help users with:

- General questions and information
- Writing and editing text
- Problem solving and analysis
- Code explanation and debugging
- Creative tasks and brainstorming

Be friendly, helpful, and conversational in your responses.
""",
    tools=mcp_toolsets,
)