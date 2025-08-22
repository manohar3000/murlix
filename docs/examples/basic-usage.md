# Basic Usage Examples

Practical examples of using Murlix for common tasks and workflows.

## Getting Started

### Your First Chat Session

```bash
# Start Murlix
uv run murlix

# Interactive conversation
You: Hello, how are you?
Murlix: Hello! I'm doing well, thank you for asking. How can I help you today?
```

### Quick Queries

```bash
# One-off questions
uv run murlix -q "What is Python?"
uv run murlix -q "Explain REST APIs"
uv run murlix -q "Show me a Python decorator example"
```

## Common Use Cases

### Code Help

```bash
You: I need help with Python error handling. Can you show me best practices?
```

### Learning New Technologies

```bash
You: I'm learning Docker. Can you explain containers and images?
```

### Debugging Assistance

```bash
You: I'm getting this error: [paste error message]. What might be causing it?
```

## Session Management

### Continuing Conversations

```bash
# Continue your last session
uv run murlix continue-chat

# Pick from previous sessions
uv run murlix load-chat
```

### Using Slash Commands

```bash
You: /help          # Show available commands
You: /sessions      # List all sessions
You: /clear         # Clear screen
You: /quit          # Exit Murlix
```

*More examples coming soon...*