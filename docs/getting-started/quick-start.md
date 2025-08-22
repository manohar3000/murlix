# Quick Start

Welcome to your first Murlix experience! This guide will walk you through starting your first AI conversation and exploring the key features that make Murlix special.

## Your First Conversation

Let's dive right in with a simple conversation:

### 1. Start Murlix

Open your terminal and run:

```bash
uv run murlix
```

You'll be greeted with Murlix's beautiful welcome screen:

```
╭─ Welcome to Murlix ───────────────────────────────────────────────────────────╮
│                                                                               │
│  ███╗   ███╗██╗   ██╗██████╗ ██╗     ██╗██╗  ██╗                             │
│  ████╗ ████║██║   ██║██╔══██╗██║     ██║╚██╗██╔╝                             │
│  ██╔████╔██║██║   ██║██████╔╝██║     ██║ ╚███╔╝                              │
│  ██║╚██╔╝██║██║   ██║██╔══██╗██║     ██║ ██╔██╗                              │
│  ██║ ╚═╝ ██║╚██████╔╝██║  ██║███████╗██║██╔╝ ██╗                             │
│  ╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═╝                             │
│                                                                               │
│  A beautiful CLI chat interface powered by Google's ADK                       │
│                                                                               │
╰───────────────────────────────────────────────────────────────────────────────╯

Starting new session...
Session ID: abc123def456...

You: 
```

### 2. Ask Your First Question

Try asking something simple:

```
You: Hello! What can you help me with?
```

Murlix will respond with a beautifully formatted message:

```
╭─ Murlix ─────────────────────────────────────────────────────────────────────╮
│ Hello! I'm Murlix, your AI assistant. I can help you with a wide variety of  │
│ tasks including:                                                              │
│                                                                               │
│ • Programming and code review                                                 │
│ • Writing and editing                                                         │
│ • Problem-solving and analysis                                                │
│ • Research and fact-checking                                                  │
│ • Creative projects and brainstorming                                         │
│ • Learning new concepts and skills                                            │
│                                                                               │
│ What would you like to work on today?                                         │
╰──────────────────────────────────────────────────────────────────────────────╯
```

### 3. Continue the Conversation

Keep chatting naturally. Try asking about something you're working on:

```
You: I'm working on a Python project and need help with error handling. Can you show me best practices?

╭─ Murlix ─────────────────────────────────────────────────────────────────────╮
│ I'd be happy to help with Python error handling! Here are the key best       │
│ practices:                                                                    │
│                                                                               │
│ 1. **Use Specific Exceptions**                                                │
│    ```python                                                                  │
│    try:                                                                       │
│        result = int(user_input)                                               │
│    except ValueError as e:                                                    │
│        print(f"Invalid input: {e}")                                           │
│    ```                                                                        │
│                                                                               │
│ 2. **Handle Multiple Exceptions**                                             │
│    ```python                                                                  │
│    try:                                                                       │
│        with open(filename, 'r') as file:                                      │
│            data = json.load(file)                                             │
│    except FileNotFoundError:                                                  │
│        print("File not found")                                                │
│    except json.JSONDecodeError:                                               │
│        print("Invalid JSON format")                                           │
│    ```                                                                        │
│                                                                               │
│ Would you like me to explain any specific error handling scenario?            │
╰──────────────────────────────────────────────────────────────────────────────╯
```

## Exploring Slash Commands

Murlix includes powerful slash commands for enhanced functionality. Try them out:

### Get Help

```
You: /help
```

This shows all available commands:

```
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
│ /clear                                                                        │
│   Clear the terminal screen                                                   │
│                                                                               │
│ /new                                                                          │
│   Instructions for starting a new session                                    │
│                                                                               │
│ Tip: Use Ctrl+C to exit at any time                                          │
╰──────────────────────────────────────────────────────────────────────────────╯
```

### View Your Sessions

```
You: /sessions
```

See all your conversation history:

```
╭─ Your Chat Sessions ─────────────────────────────────────────────────────────╮
│                                                                               │
│                           Available Sessions                                  │
│ ┏━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┓     │
│ ┃ Index    ┃ Session ID           ┃ Created At           ┃ Status       ┃     │
│ ┡━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━┩     │
│ │ 1        │ abc123def456...      │ 2024-01-15 14:30:25  │ Current      │     │
│ │ 2        │ def456ghi789...      │ 2024-01-14 09:15:42  │ Active       │     │
│ │ 3        │ ghi789jkl012...      │ 2024-01-13 16:22:10  │ Active       │     │
│ └──────────┴──────────────────────┴──────────────────────┴──────────────┘     │
│                                                                               │
╰───────────────────────────────────────────────────────────────────────────────╯
```

## Command-Line Options

Murlix offers several ways to interact with it beyond the interactive mode:

### One-Shot Queries

For quick questions without starting a session:

```bash
uv run murlix --query "What's the weather like today?"
```

### Continue Your Last Session

Resume your most recent conversation:

```bash
uv run murlix continue-chat
```

### Load a Specific Session

Pick from any of your previous sessions:

```bash
uv run murlix load-chat
```

This shows a menu to select from:

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

## Essential Tips

### Navigation

- **Exit**: Use `Ctrl+C` or type `/quit` to exit
- **Clear Screen**: Type `/clear` to clear the terminal
- **New Session**: Start fresh with `/new` for instructions

### Best Practices

!!! tip "Conversation Tips"
    - **Be specific**: The more context you provide, the better Murlix can help
    - **Ask follow-ups**: Build on previous responses for deeper insights
    - **Use examples**: Show code, data, or specific scenarios for better assistance

!!! tip "Session Management"
    - **Name your sessions**: Use descriptive first messages to identify sessions later
    - **Continue sessions**: Resume conversations to maintain context
    - **Regular cleanup**: Review old sessions periodically

### Keyboard Shortcuts

| Shortcut | Action |
|----------|---------|
| `Ctrl+C` | Exit Murlix |
| `Ctrl+L` | Clear screen (same as `/clear`) |
| `↑` / `↓` | Navigate command history |
| `Tab` | Auto-complete slash commands |

## Example Workflows

### Code Review Session

```bash
# Start a focused session for code review
uv run murlix

You: I need help reviewing this Python function for performance issues:

def process_data(items):
    result = []
    for item in items:
        if item.is_valid():
            result.append(transform_item(item))
    return result

# Murlix provides detailed feedback and suggestions
```

### Learning Session

```bash
# Continue learning about a topic across multiple sessions
uv run murlix continue-chat

You: Yesterday we were discussing machine learning algorithms. Can you explain decision trees in more detail?

# Murlix remembers the context and continues the educational conversation
```

### Problem-Solving Session

```bash
# Quick problem-solving without persistent session
uv run murlix --query "I'm getting a 'ModuleNotFoundError' in Python. What are the common causes and solutions?"
```

## What's Next?

Now that you've experienced Murlix basics, explore more advanced features:

1. **[Interactive Mode](../user-guide/interactive-mode.md)** - Master all the interactive features
2. **[Session Management](../user-guide/session-management.md)** - Advanced session handling
3. **[Configuration](configuration.md)** - Customize Murlix for your workflow
4. **[Slash Commands](../user-guide/slash-commands.md)** - Complete command reference

!!! success "You're Ready!"
    You now know the essentials of using Murlix! The key is to start conversations naturally and let Murlix's intelligence and session management enhance your workflow.

## Common First Questions

Here are some great questions to try in your first sessions:

=== "Development"
    ```
    • "Help me debug this error message: [paste your error]"
    • "What are best practices for [programming concept]?"
    • "Review this code for improvements: [paste code]"
    • "Explain how [technology/framework] works"
    ```

=== "Learning"
    ```
    • "I'm learning [topic]. Where should I start?"
    • "Explain [concept] with examples"
    • "What are the key differences between [A] and [B]?"
    • "Give me a step-by-step guide for [task]"
    ```

=== "Problem Solving"
    ```
    • "I'm trying to [goal] but [obstacle]. Any ideas?"
    • "What's the best approach to [challenge]?"
    • "Help me brainstorm solutions for [problem]"
    • "What should I consider when [decision]?"
    ```

Happy chatting with Murlix! 🚀