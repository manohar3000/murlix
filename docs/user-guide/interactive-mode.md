# Interactive Mode

Interactive mode is the heart of Murlix – a beautiful, real-time chat interface that transforms your terminal into an AI conversation space. This guide covers everything you need to know to master interactive mode.

## Starting Interactive Mode

Launch Murlix in interactive mode with:

```bash
uv run murlix
```

You'll be greeted with the stunning welcome screen and automatically enter a new chat session.

## The Interface

### Welcome Screen

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
```

### Chat Interface Components

#### 1. Session Information
```
Starting new session...
Session ID: abc123def456...
```

#### 2. User Input Prompt
```
You: 
```

#### 3. AI Response Display
```
╭─ Murlix ─────────────────────────────────────────────────────────────────────╮
│ Your AI assistant's response appears here in a beautifully formatted box     │
│ with proper text wrapping and visual hierarchy.                              │
╰──────────────────────────────────────────────────────────────────────────────╯
```

## Navigation & Controls

### Keyboard Shortcuts

| Shortcut | Action | Description |
|----------|--------|-------------|
| `Enter` | Send message | Send your typed message to the AI |
| `Ctrl+C` | Exit | Gracefully exit Murlix |
| `Ctrl+L` | Clear screen | Clear the terminal display |
| `↑` / `↓` | History navigation | Browse through previous messages |
| `Tab` | Command completion | Auto-complete slash commands |
| `Ctrl+A` | Beginning of line | Move cursor to start of input |
| `Ctrl+E` | End of line | Move cursor to end of input |

### Input Features

#### Multi-line Input
For longer messages, you can continue typing across multiple lines:

```
You: This is a long message that spans
multiple lines. Just keep typing and
press Enter when you're done.
```

#### Paste Support
Murlix handles pasted content intelligently:

```
You: Here's my code:

def example_function():
    # Pasted code maintains formatting
    return "Hello, World!"

What do you think of this approach?
```

## Conversation Flow

### Starting Conversations

Begin with context-rich opening messages:

!!! tip "Good Opening Messages"
    ```
    ✓ "I'm building a REST API in Python and need help with authentication"
    ✓ "Can you explain the difference between async and sync programming?"
    ✓ "I'm getting this error: [paste error]. What might be causing it?"
    ```

!!! warning "Less Effective Openings"
    ```
    ✗ "Hi"
    ✗ "Help me"
    ✗ "What can you do?"
    ```

### Building Context

Murlix maintains conversation context throughout your session:

```
You: I'm working on a web scraper in Python.

╭─ Murlix ─────────────────────────────────────────────────────────────────────╮
│ Great! I can help you with web scraping in Python. What specific aspect     │
│ would you like to work on? Are you using libraries like requests and        │
│ BeautifulSoup, or perhaps Scrapy?                                           │
╰──────────────────────────────────────────────────────────────────────────────╯

You: I'm using requests and BeautifulSoup, but I'm having trouble with JavaScript-rendered content.

╭─ Murlix ─────────────────────────────────────────────────────────────────────╮
│ Ah, that's a common challenge! JavaScript-rendered content won't be         │
│ available in the initial HTML that requests fetches. Here are some          │
│ solutions...                                                                 │
╰──────────────────────────────────────────────────────────────────────────────╯
```

## Advanced Features

### Code Formatting

Murlix automatically formats code blocks in responses:

```python
def example_function(param1, param2):
    """
    This is how Murlix displays code - with syntax highlighting
    and proper formatting.
    """
    result = param1 + param2
    return result
```

### Lists and Structure

Responses are formatted with clear structure:

```
╭─ Murlix ─────────────────────────────────────────────────────────────────────╮
│ Here are the key points:                                                     │
│                                                                               │
│ 1. **First Point**: Detailed explanation with examples                       │
│ 2. **Second Point**: Additional context and reasoning                        │
│ 3. **Third Point**: Practical implementation advice                          │
│                                                                               │
│ Would you like me to elaborate on any of these points?                       │
╰──────────────────────────────────────────────────────────────────────────────╯
```

### Error Handling

When things go wrong, Murlix provides helpful feedback:

```
╭─ System ─────────────────────────────────────────────────────────────────────╮
│ ⚠️  Connection error occurred. Retrying...                                   │
╰──────────────────────────────────────────────────────────────────────────────╯

╭─ System ─────────────────────────────────────────────────────────────────────╮
│ ✓ Connection restored. Your message has been sent.                           │
╰──────────────────────────────────────────────────────────────────────────────╯
```

## Conversation Patterns

### Effective Interaction Patterns

#### 1. Iterative Development
```
You: I need to create a login system for my web app.

# Murlix provides overview

You: Let's focus on password hashing first. Show me secure implementation.

# Murlix provides specific code

You: Good! Now how do I integrate this with session management?

# Continue building on previous responses
```

#### 2. Problem-Solution Flow
```
You: I'm getting a "KeyError" when processing JSON data. Here's my code: [paste code]

# Murlix analyzes the problem

You: That makes sense. Can you show me a more robust way to handle missing keys?

# Murlix provides improved solution

You: Perfect! How would this handle nested JSON structures?

# Dive deeper into the solution
```

#### 3. Learning Sessions
```
You: I want to understand machine learning fundamentals.

# Murlix provides structured overview

You: Explain supervised learning with a practical example.

# Focus on specific concepts

You: Now show me how to implement a simple classifier in Python.

# Move from theory to practice
```

### Conversation Best Practices

!!! tip "Maximize Effectiveness"
    - **Be specific**: Include relevant details, error messages, and code snippets
    - **Build incrementally**: Use previous responses as foundation for follow-ups
    - **Ask for clarification**: Don't hesitate to ask for more explanation
    - **Provide context**: Mention your skill level, goals, and constraints

!!! tip "Code Discussions"
    - **Share relevant code**: Paste the specific code you're working with
    - **Explain the goal**: Describe what you're trying to achieve
    - **Include error messages**: Copy the exact error text if applicable
    - **Mention your environment**: Specify language versions, frameworks, etc.

## Session Continuity

### Within a Session

Your conversation context is maintained throughout the session:

- Previous messages are remembered
- Code examples can be referenced later
- Complex topics can be explored progressively
- Solutions can be refined iteratively

### Across Sessions

While each session is separate, you can:

- Reference previous sessions when starting new ones
- Continue similar topics in new sessions
- Build on knowledge from earlier conversations

## Customizing Interactive Mode

### Environment Variables

Control interactive mode behavior:

```bash
# In your .env file
INTERACTIVE_TIMEOUT=1800  # 30 minutes of inactivity before timeout
RESPONSE_STREAMING=true   # Enable streaming responses
MAX_INPUT_LENGTH=10000    # Maximum characters per message
HISTORY_SIZE=50          # Number of messages to remember
```

### Visual Customization

While limited, you can modify some visual aspects by editing the source:

```python
# In src/murlix/ui.py
RESPONSE_BORDER_STYLE = "blue"      # Change border color
RESPONSE_TITLE_ALIGN = "left"       # Title alignment
USER_INPUT_STYLE = "bold cyan"      # User input styling
```

## Troubleshooting Interactive Mode

### Common Issues

!!! failure "Input Not Working"
    **Symptoms**: Typing doesn't appear or commands aren't recognized
    
    **Solutions**:
    - Check terminal compatibility (use modern terminal emulator)
    - Verify Python version (3.13+ required)
    - Try resizing terminal window
    - Restart Murlix

!!! failure "Display Issues"
    **Symptoms**: Formatting broken, boxes not displaying correctly
    
    **Solutions**:
    - Ensure terminal supports Unicode
    - Check terminal size (minimum 80x24 recommended)
    - Update terminal software
    - Try different terminal emulator

!!! failure "Performance Issues"
    **Symptoms**: Slow responses, lag in typing
    
    **Solutions**:
    - Check internet connection
    - Verify API key and quotas
    - Reduce conversation history length
    - Close other resource-intensive applications

### Debug Mode

Enable debug mode for troubleshooting:

```bash
# Start with debug logging
LOG_LEVEL=DEBUG uv run murlix

# Or set in .env file
LOG_LEVEL=DEBUG
```

## Tips for Power Users

### Efficient Workflows

1. **Prepare context**: Have code, error messages, and documentation ready
2. **Use specific terminology**: Technical terms help get precise responses
3. **Break down complex problems**: Tackle one aspect at a time
4. **Save important responses**: Copy useful code snippets and explanations
5. **Experiment iteratively**: Test suggestions and report back results

### Advanced Techniques

#### Context Injection
Start sessions with rich context:

```
You: I'm working on a Django REST API for an e-commerce platform. 
Current models: User, Product, Order, OrderItem. 
Using PostgreSQL, Redis for caching, Celery for tasks.
Need help optimizing the product search endpoint that's currently slow.
```

#### Progressive Refinement
Build solutions incrementally:

```
You: Show me basic product search implementation.
# Get basic version

You: Now add filtering by category and price range.
# Add features

You: How can we optimize this for large datasets?
# Improve performance

You: Add caching layer to this solution.
# Final optimization
```

## Next Steps

Master these related features:

1. **[Session Management](session-management.md)** - Learn to manage multiple conversations
2. **[Slash Commands](slash-commands.md)** - Discover powerful built-in commands  
3. **[Advanced Usage](advanced-usage.md)** - Explore advanced features and integrations

!!! success "Interactive Mode Mastery"
    With these techniques, you'll be able to have highly productive AI conversations that feel natural and help you solve complex problems efficiently.