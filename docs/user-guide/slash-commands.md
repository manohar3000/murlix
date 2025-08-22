# Slash Commands

Slash commands are powerful built-in commands that enhance your Murlix experience. They provide quick access to functionality without leaving the interactive chat interface.

## Available Commands

### `/help`
**Usage**: `/help`  
**Description**: Display all available slash commands with descriptions

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
│ /clear                                                                        │
│   Clear the terminal screen                                                   │
│                                                                               │
│ /new                                                                          │
│   Instructions for starting a new session                                    │
╰──────────────────────────────────────────────────────────────────────────────╯
```

### `/quit`
**Usage**: `/quit`  
**Description**: Gracefully exit Murlix and save the current session

- Saves all conversation data
- Closes database connections cleanly
- Returns to terminal prompt

### `/sessions`
**Usage**: `/sessions`  
**Description**: Display a table of all your chat sessions

Shows detailed information including:
- Session index for easy reference
- Partial session ID
- Creation timestamp
- Current status

### `/clear`
**Usage**: `/clear`  
**Description**: Clear the terminal screen while preserving session context

- Clears visual display only
- Conversation history remains intact
- Useful for reducing clutter during long sessions

### `/new`
**Usage**: `/new`  
**Description**: Display instructions for starting a new session

Provides guidance on:
- How to exit current session
- Commands to start fresh sessions
- Best practices for session organization

## Command Features

### Auto-completion
Slash commands support tab completion:

```bash
You: /he<TAB>
# Completes to: /help

You: /se<TAB>  
# Completes to: /sessions
```

### Case Sensitivity
Commands are case-insensitive:

```bash
/HELP    # Works
/Help    # Works  
/help    # Works
/hElP    # Works
```

### Error Handling
Invalid commands show helpful suggestions:

```bash
You: /halp
Unknown command '/halp'. Did you mean '/help'?
Type /help to see all available commands.
```

## Advanced Usage

### Command Chaining
While not directly supported, you can use commands in sequence:

```bash
You: /clear
You: /sessions
You: /help
```

### Integration with Chat
Commands can be used naturally within conversations:

```bash
You: Let me check my previous sessions first.
You: /sessions
You: Now I'll continue with my Python question...
```

## Custom Commands

Murlix supports adding custom slash commands. See the [Custom Commands](../developer-guide/custom-commands.md) guide for details on:

- Creating new commands
- Registering command handlers
- Adding command descriptions
- Implementing command logic

## Best Practices

### When to Use Slash Commands

!!! tip "Effective Command Usage"
    - **Quick actions**: Use commands for immediate actions like clearing screen
    - **Navigation**: Use `/sessions` to switch between conversations
    - **Help**: Use `/help` when you forget available commands
    - **Clean exits**: Always use `/quit` instead of Ctrl+C when possible

### Command Workflow Tips

**Start of Session**:
```bash
You: /clear        # Clean slate
You: /sessions     # Review available sessions if needed
```

**During Long Conversations**:
```bash
You: /clear        # Reduce visual clutter
# Continue conversation...
```

**End of Session**:
```bash
You: /quit         # Clean exit
```

## Troubleshooting Commands

### Command Not Working

!!! failure "Command Not Recognized"
    **Problem**: Command doesn't execute or shows as regular message
    
    **Solutions**:
    - Ensure command starts with `/` character
    - Check spelling (use tab completion)
    - Verify you're in interactive mode
    - Try `/help` to see available commands

### Tab Completion Issues

!!! failure "Tab Completion Not Working"  
    **Problem**: Tab key doesn't complete commands
    
    **Solutions**:
    - Ensure your terminal supports tab completion
    - Try typing more letters before pressing tab
    - Update your terminal software
    - Check if other applications are intercepting tab key

### Display Issues

!!! failure "Command Output Malformed"
    **Problem**: Command output doesn't display correctly
    
    **Solutions**:
    - Try `/clear` to refresh display
    - Ensure terminal supports Unicode characters
    - Resize terminal window
    - Update terminal software

## Future Commands

Planned slash commands for future releases:

- `/export` - Export current session
- `/search` - Search conversation history  
- `/theme` - Change display theme
- `/config` - View/modify configuration
- `/debug` - Toggle debug mode
- `/stats` - Show session statistics

## Next Steps

- **[Advanced Usage](advanced-usage.md)**: Explore power-user features
- **[Custom Commands](../developer-guide/custom-commands.md)**: Create your own commands
- **[Interactive Mode](interactive-mode.md)**: Master the chat interface

!!! success "Command Mastery"
    Slash commands make Murlix more efficient and enjoyable to use. Master these built-in commands and consider creating custom ones for your specific workflow needs.