# Murlix

A beautiful CLI chat interface powered by Google's Agent Development Kit (ADK). Murlix provides an intuitive and feature-rich command-line experience for interacting with AI agents.

## Features

- 🎨 **Beautiful CLI Interface** - Rich terminal UI with ASCII art and elegant formatting
- 💬 **Interactive Chat** - Seamless conversation experience with the AI agent
- 📚 **Session Management** - Persistent sessions that survive application restarts
- 🔄 **Session Continuation** - Resume your last conversation or pick from any previous session
- 🛠️ **Slash Commands** - Built-in commands for enhanced functionality
- 📱 **Modern UX** - Responsive design with loading indicators and status panels

## Installation

### Prerequisites

- Python 3.13+
- [uv](https://github.com/astral-sh/uv) package manager

### Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd murlix
   ```

2. Install dependencies:
   ```bash
   uv sync
   ```

3. Set up environment variables (optional):
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

## Usage

### Basic Commands

```bash
# Start an interactive chat session
uv run murlix

# Continue your most recent session
uv run murlix continue-chat

# Pick from any previous session
uv run murlix load-chat

# Process a single query
uv run murlix --query "Your question here"

# Show help
uv run murlix --help
```

### Interactive Mode

When you start Murlix in interactive mode, you'll see a beautiful welcome screen followed by a chat interface:

```
You: Hello, how are you?
╭─ Murlix ─────────────────────────────────────────────────────────────────────╮
│ Hello! I'm doing well, thank you for asking. How can I help you today?       │
╰──────────────────────────────────────────────────────────────────────────────╯
```

### Slash Commands

Murlix supports several built-in slash commands:

- `/help` - Show all available commands
- `/quit` - Exit the chat session
- `/sessions` - List all your chat sessions
- `/clear` - Clear the terminal screen
- `/new` - Instructions for starting a new session

Example:
```
You: /help
╭─ Help ───────────────────────────────────────────────────────────────────────╮
│ Available Commands:                                                           │
│                                                                               │
│ /help                                                                         │
│   Show list of available commands                                            │
│                                                                               │
│ /quit                                                                         │
│   Exit the interactive mode                                                   │
│                                                                               │
│ /sessions                                                                     │
│   List all available chat sessions                                           │
│                                                                               │
│ Tip: Use Ctrl+C to exit at any time                                          │
╰──────────────────────────────────────────────────────────────────────────────╯
```

### Session Management

#### Continue Last Session
```bash
uv run murlix continue-chat
```
Automatically resumes your most recent conversation. If no previous sessions exist, it starts a new one.

#### Load Specific Session
```bash
uv run murlix load-chat
```
Shows a table of all your sessions and lets you pick which one to continue:

```
                           Available Sessions                            
┏━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┓
┃ Index    ┃ Session ID           ┃ Created At           ┃ Status       ┃
┡━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━┩
│ 1        │ abc123...            │ 2024-01-15 14:30:25  │ Active       │
│ 2        │ def456...            │ 2024-01-14 09:15:42  │ Active       │
└──────────┴──────────────────────┴──────────────────────┴──────────────┘

Select a session by index (or 'n' for new session) (1):
```

## Project Structure

The codebase has been refactored for clarity and maintainability:

```
src/murlix/
├── __init__.py          # Main CLI entry point and command definitions
├── chat.py              # Chat loop and interaction logic
├── session.py           # Session management and persistence
├── slash_commands.py    # Slash command handlers
├── ui.py                # User interface components and formatting
├── core_agent/
│   └── agent.py         # AI agent configuration
└── utils/
    ├── __init__.py      # Utils package initialization
    ├── console.py       # Rich console instance
    ├── helper.py        # Utility functions
    └── supress_warnings.py  # Warning suppression
```

### Module Responsibilities

- **`__init__.py`** - CLI commands, main entry point, and application orchestration
- **`chat.py`** - Core chat loop functionality and message handling
- **`session.py`** - Session creation, loading, listing, and persistence management
- **`slash_commands.py`** - Command registry and handlers for slash commands
- **`ui.py`** - Rich terminal UI components, ASCII art, and response formatting
- **`core_agent/agent.py`** - AI agent configuration and toolset setup
- **`utils/`** - Shared utilities for console, helpers, and warning management

## Configuration

### Environment Variables

Create a `.env` file with the following optional configurations:

```bash
# User identification (defaults to "default_user")
USER_ID=your_user_id

# Google AI API Key (for Google AI API)
GOOGLE_API_KEY=your_api_key

# Vertex AI Configuration (for Vertex AI API)
VERTEX_AI_PROJECT=your_project_id
VERTEX_AI_LOCATION=your_location
```

### Agent Configuration

The AI agent can be customized in `src/murlix/core_agent/agent.py`:

```python
root_agent = LlmAgent(
    model='gemini-2.0-flash',
    name='Murlix_Assistant',
    instruction="Your custom instructions here...",
    tools=mcp_toolsets,  # Add your custom tools
)
```

## Development

### Code Style

The project follows Python best practices:

- Type hints for better code clarity
- Docstrings for all public functions
- Modular design with clear separation of concerns
- Rich terminal formatting for beautiful output

### Adding New Commands

To add a new slash command:

1. Create a handler function in `slash_commands.py`:
   ```python
   def handle_my_command() -> None:
       """Handle the /my-command command."""
       console.print("My command executed!")
   ```

2. Register it in the `slash_commands` dictionary:
   ```python
   "/my-command": SlashCommand(
       name="my-command",
       description="Description of what it does",
       handler=handle_my_command,
       usage="/my-command"
   ),
   ```

### Extending Session Management

The `SessionManager` class provides a clean interface for session operations:

```python
# Create a new session
runner, session_id = await session_manager.create_session()

# List all sessions
sessions = await session_manager.list_sessions()

# Load a specific session
runner = await session_manager.load_session(session_id)

# Continue the latest session
result = await session_manager.continue_latest_session()
```

## Database

Murlix uses SQLite for session persistence. The database file (`my_agent_data.db`) is automatically created and contains:

- Session metadata
- Conversation history
- User state and preferences
- Event logs

## Troubleshooting

### Common Issues

1. **Import Errors**: Make sure all dependencies are installed with `uv sync`
2. **API Errors**: Configure your Google AI or Vertex AI credentials
3. **Session Errors**: Delete `my_agent_data.db` to reset all sessions
4. **Tool Errors**: Check your MCP toolset configuration in `agent.py`

### Debug Mode

For detailed logging, you can modify the console output in `utils/console.py` or add debugging statements.

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes with proper documentation
4. Test your changes thoroughly
5. Submit a pull request

## License

[Add your license information here]

## Acknowledgments

- Built with [Google Agent Development Kit (ADK)](https://github.com/google/adk-python)
- Terminal UI powered by [Rich](https://github.com/Textualize/rich)
- CLI framework using [Click](https://click.palletsprojects.com/)