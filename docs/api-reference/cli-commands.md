# CLI Commands Reference

Murlix provides a comprehensive command-line interface with multiple commands and options. This reference covers all available CLI commands, their options, and usage examples.

## Main Command

### `murlix`

The primary command to interact with Murlix.

```bash
uv run murlix [OPTIONS] [COMMAND] [ARGS]...
```

**Description**: A beautiful CLI chat interface powered by Google's Agent Development Kit (ADK).

## Interactive Commands

### Default (Interactive Mode)

Start an interactive chat session:

```bash
uv run murlix
```

**Behavior**:
- Launches the beautiful welcome screen
- Creates a new chat session
- Enters interactive mode for real-time conversation
- Session persists until manually exited

**Example**:
```bash
$ uv run murlix
╭─ Welcome to Murlix ───────────────────────────────────────────────────────────╮
│  A beautiful CLI chat interface powered by Google's ADK                       │
╰───────────────────────────────────────────────────────────────────────────────╯

Starting new session...
Session ID: abc123def456...

You: Hello! How can you help me today?
```

### `continue-chat`

Resume your most recent chat session:

```bash
uv run murlix continue-chat
```

**Behavior**:
- Automatically loads the latest session
- Continues conversation with full context
- Creates new session if no previous sessions exist

**Example**:
```bash
$ uv run murlix continue-chat
Continuing session: abc123def456...
Last message: "Thanks for the help with Python!"

You: Can you help me with the next part of that project?
```

### `load-chat`

Select from available chat sessions:

```bash
uv run murlix load-chat
```

**Behavior**:
- Displays a table of all available sessions
- Prompts for session selection
- Loads selected session with full context

**Example**:
```bash
$ uv run murlix load-chat

                           Available Sessions                            
┏━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┓
┃ Index    ┃ Session ID           ┃ Created At           ┃ Status       ┃
┡━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━┩
│ 1        │ abc123...            │ 2024-01-15 14:30:25  │ Active       │
│ 2        │ def456...            │ 2024-01-14 09:15:42  │ Active       │
└──────────┴──────────────────────┴──────────────────────┴──────────────┘

Select a session by index (or 'n' for new session) (1): 2
```

## Query Commands

### `--query` / `-q`

Execute a single query without entering interactive mode:

```bash
uv run murlix --query "Your question here"
uv run murlix -q "Your question here"
```

**Parameters**:
- `QUERY` (string): The question or prompt to send to the AI

**Behavior**:
- Sends query to AI agent
- Displays formatted response
- Exits immediately after response
- Does not create persistent session

**Examples**:

=== "Simple Query"
    ```bash
    $ uv run murlix -q "What is Python?"
    
    ╭─ Murlix ─────────────────────────────────────────────────────────────────────╮
    │ Python is a high-level, interpreted programming language known for its      │
    │ simple syntax and readability. It was created by Guido van Rossum and      │
    │ first released in 1991...                                                   │
    ╰──────────────────────────────────────────────────────────────────────────────╯
    ```

=== "Code Query"
    ```bash
    $ uv run murlix -q "Show me a Python function to calculate factorial"
    
    ╭─ Murlix ─────────────────────────────────────────────────────────────────────╮
    │ Here's a Python function to calculate factorial:                            │
    │                                                                              │
    │ ```python                                                                    │
    │ def factorial(n):                                                            │
    │     if n < 0:                                                                │
    │         raise ValueError("Factorial is not defined for negative numbers")   │
    │     elif n == 0 or n == 1:                                                  │
    │         return 1                                                             │
    │     else:                                                                    │
    │         return n * factorial(n - 1)                                          │
    │ ```                                                                          │
    ╰──────────────────────────────────────────────────────────────────────────────╯
    ```

=== "Long Query"
    ```bash
    $ uv run murlix -q "Explain the differences between synchronous and asynchronous programming in Python, with examples"
    
    # Detailed response with examples...
    ```

## Utility Commands

### `--help` / `-h`

Display help information:

```bash
uv run murlix --help
uv run murlix -h
```

**Output**:
```
Usage: murlix [OPTIONS] COMMAND [ARGS]...

  A beautiful CLI chat interface powered by Google's Agent Development Kit
  (ADK). Murlix provides an intuitive and feature-rich command-line experience
  for interacting with AI agents.

Options:
  -q, --query TEXT  Execute a single query without interactive mode
  -h, --help        Show this message and exit.

Commands:
  continue-chat  Continue your most recent chat session
  load-chat      Select and load a previous chat session
```

### `--version` / `-v`

Display version information:

```bash
uv run murlix --version
uv run murlix -v
```

**Output**:
```
Murlix version 0.1.0
Powered by Google Agent Development Kit (ADK)
```

## Configuration Commands

### `config`

Configuration management commands:

#### `config check`

Validate current configuration:

```bash
uv run murlix config check
```

**Output**:
```
✓ Environment file found
✓ API credentials configured  
✓ Database accessible
✓ Agent configuration valid
⚠ Log directory not writable (using default)
```

#### `config show`

Display current configuration:

```bash
uv run murlix config show
```

**Output**:
```
Configuration Summary:
├── User ID: your_username
├── API Provider: Google AI
├── Model: gemini-2.0-flash
├── Database: ./my_agent_data.db
├── Log Level: INFO
└── Session Timeout: 1440 minutes
```

#### `config reset`

Reset configuration to defaults:

```bash
uv run murlix config reset
```

**Behavior**:
- Prompts for confirmation
- Resets all settings to defaults
- Preserves session data unless specified

## Session Management Commands

### `sessions`

Session management commands:

#### `sessions list`

List all available sessions:

```bash
uv run murlix sessions list
```

**Output**:
```
Available Sessions (3 total):

┏━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┓
┃ Index    ┃ Session ID           ┃ Created At           ┃ Status       ┃
┡━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━┩
│ 1        │ abc123def456...      │ 2024-01-15 14:30:25  │ Active       │
│ 2        │ def456ghi789...      │ 2024-01-14 09:15:42  │ Active       │
│ 3        │ ghi789jkl012...      │ 2024-01-13 16:22:10  │ Active       │
└──────────┴──────────────────────┴──────────────────────┴──────────────┘
```

#### `sessions export`

Export session data:

```bash
uv run murlix sessions export [SESSION_ID] [--format FORMAT] [--output FILE]
```

**Parameters**:
- `SESSION_ID` (optional): Specific session to export (default: all)
- `--format` (optional): Export format (json, csv, txt) (default: json)
- `--output` (optional): Output file path (default: stdout)

**Examples**:
```bash
# Export all sessions to JSON
uv run murlix sessions export --output sessions.json

# Export specific session to text
uv run murlix sessions export abc123def456 --format txt --output session.txt

# Export to stdout
uv run murlix sessions export def456ghi789
```

#### `sessions delete`

Delete session(s):

```bash
uv run murlix sessions delete [SESSION_ID] [--all] [--older-than DAYS]
```

**Parameters**:
- `SESSION_ID` (optional): Specific session to delete
- `--all`: Delete all sessions
- `--older-than`: Delete sessions older than N days

**Examples**:
```bash
# Delete specific session
uv run murlix sessions delete abc123def456

# Delete all sessions (with confirmation)
uv run murlix sessions delete --all

# Delete sessions older than 30 days
uv run murlix sessions delete --older-than 30
```

## Advanced Options

### Global Options

These options can be used with any command:

#### `--verbose` / `-v`

Enable verbose output:

```bash
uv run murlix --verbose [COMMAND]
```

#### `--quiet` / `-q`

Suppress non-essential output:

```bash
uv run murlix --quiet [COMMAND]
```

#### `--config-file`

Specify custom configuration file:

```bash
uv run murlix --config-file /path/to/config.env [COMMAND]
```

#### `--database`

Specify custom database path:

```bash
uv run murlix --database /path/to/custom.db [COMMAND]
```

### Environment Variable Overrides

Override configuration via environment variables:

```bash
# Override API key
GOOGLE_API_KEY=your_key uv run murlix

# Override user ID
USER_ID=custom_user uv run murlix

# Override log level
LOG_LEVEL=DEBUG uv run murlix

# Multiple overrides
USER_ID=test LOG_LEVEL=DEBUG uv run murlix -q "Hello"
```

## Exit Codes

Murlix uses standard exit codes:

| Code | Meaning |
|------|---------|
| 0 | Success |
| 1 | General error |
| 2 | Misuse of shell command |
| 126 | Command invoked cannot execute |
| 127 | Command not found |
| 128+n | Fatal error signal "n" |

## Command Chaining

### Sequential Commands

Execute multiple commands in sequence:

```bash
# Check config, then start interactive session
uv run murlix config check && uv run murlix

# Export sessions, then start new session
uv run murlix sessions export --output backup.json && uv run murlix
```

### Conditional Execution

Execute commands based on success/failure:

```bash
# Start interactive mode only if config is valid
uv run murlix config check && uv run murlix || echo "Configuration invalid"

# Try to continue chat, fallback to new session
uv run murlix continue-chat || uv run murlix
```

## Scripting with Murlix

### Batch Queries

Process multiple queries from a file:

```bash
# queries.txt contains one query per line
while IFS= read -r query; do
    echo "Query: $query"
    uv run murlix -q "$query"
    echo "---"
done < queries.txt
```

### Automated Session Management

```bash
#!/bin/bash
# backup-and-clean.sh

# Export all sessions
uv run murlix sessions export --output "backup-$(date +%Y%m%d).json"

# Delete sessions older than 30 days
uv run murlix sessions delete --older-than 30

echo "Session maintenance completed"
```

## Error Handling

### Common Error Messages

!!! failure "API Authentication Failed"
    ```
    Error: Failed to authenticate with Google AI API
    Cause: Invalid or missing API key
    Solution: Check GOOGLE_API_KEY in your .env file
    ```

!!! failure "Database Connection Error"
    ```
    Error: Cannot connect to database
    Cause: Database file permissions or corruption
    Solution: Check file permissions or delete database to reset
    ```

!!! failure "Session Not Found"
    ```
    Error: Session 'abc123...' not found
    Cause: Session ID doesn't exist or was deleted
    Solution: Use 'sessions list' to see available sessions
    ```

### Debug Mode

Enable debug mode for troubleshooting:

```bash
# Enable debug logging
LOG_LEVEL=DEBUG uv run murlix [COMMAND]

# Or set environment variable
export LOG_LEVEL=DEBUG
uv run murlix [COMMAND]
```

## Best Practices

### Command Usage

!!! tip "Efficient Command Usage"
    - Use `--query` for one-off questions
    - Use `continue-chat` for ongoing work
    - Use `load-chat` to switch between different topics
    - Export sessions regularly for backup

### Performance Tips

!!! tip "Performance Optimization"
    - Use specific queries to get focused responses
    - Clean up old sessions periodically
    - Use environment variables for configuration
    - Enable quiet mode for scripted usage

### Security Considerations

!!! warning "Security Best Practices"
    - Never include API keys in command history
    - Use environment variables for sensitive data
    - Export sessions to secure locations only
    - Regularly rotate API keys

## Next Steps

Explore related documentation:

1. **[Interactive Mode](../user-guide/interactive-mode.md)** - Master the interactive interface
2. **[Session Management](../user-guide/session-management.md)** - Advanced session handling
3. **[Configuration](../getting-started/configuration.md)** - Detailed configuration options