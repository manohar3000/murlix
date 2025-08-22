# Custom Commands

Create your own slash commands to extend Murlix's interactive functionality with custom features tailored to your workflow.

## Command Structure

Every slash command in Murlix follows a consistent pattern:

```python
from dataclasses import dataclass
from typing import Callable

@dataclass
class SlashCommand:
    name: str
    description: str
    handler: Callable
    usage: str
```

## Creating Your First Command

### 1. Define the Handler

```python
# In src/murlix/slash_commands.py

def handle_time() -> None:
    """Display current time and date."""
    from datetime import datetime
    from rich.panel import Panel
    
    now = datetime.now()
    time_str = now.strftime("%Y-%m-%d %H:%M:%S")
    
    panel = Panel(
        f"🕐 Current time: {time_str}",
        title="Time",
        border_style="cyan"
    )
    console.print(panel)
```

### 2. Register the Command

```python
# Add to slash_commands dictionary
slash_commands["/time"] = SlashCommand(
    name="time",
    description="Show current date and time",
    handler=handle_time,
    usage="/time"
)
```

### 3. Test Your Command

```bash
uv run murlix
You: /time
```

## Advanced Command Examples

### File Operations Command

```python
def handle_pwd() -> None:
    """Show current working directory."""
    import os
    from rich.panel import Panel
    
    cwd = os.getcwd()
    panel = Panel(
        f"📁 {cwd}",
        title="Current Directory",
        border_style="green"
    )
    console.print(panel)

slash_commands["/pwd"] = SlashCommand(
    name="pwd",
    description="Show current working directory",
    handler=handle_pwd,
    usage="/pwd"
)
```

### Git Status Command

```python
def handle_git() -> None:
    """Show git repository status."""
    import subprocess
    from rich.table import Table
    
    try:
        # Get git status
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            capture_output=True,
            text=True,
            check=True
        )
        
        if not result.stdout:
            console.print("✅ Working directory clean")
            return
        
        # Parse and display status
        table = Table(title="Git Status")
        table.add_column("Status")
        table.add_column("File")
        
        for line in result.stdout.strip().split('\n'):
            status = line[:2]
            filename = line[3:]
            table.add_row(status, filename)
        
        console.print(table)
        
    except subprocess.CalledProcessError:
        console.print("❌ Not a git repository")
    except FileNotFoundError:
        console.print("❌ Git not found")

slash_commands["/git"] = SlashCommand(
    name="git",
    description="Show git repository status",
    handler=handle_git,
    usage="/git"
)
```

## Commands with Parameters

### Environment Variable Command

```python
def handle_env() -> None:
    """Show environment variables (filtered for safety)."""
    import os
    from rich.table import Table
    
    # Safe environment variables to display
    safe_vars = [
        'PATH', 'HOME', 'USER', 'SHELL', 'PWD',
        'TERM', 'LANG', 'EDITOR', 'PAGER'
    ]
    
    table = Table(title="Environment Variables")
    table.add_column("Variable")
    table.add_column("Value")
    
    for var in safe_vars:
        value = os.getenv(var, "Not set")
        # Truncate long values
        if len(value) > 50:
            value = value[:47] + "..."
        table.add_row(var, value)
    
    console.print(table)

slash_commands["/env"] = SlashCommand(
    name="env",
    description="Show safe environment variables",
    handler=handle_env,
    usage="/env"
)
```

## Interactive Commands

### Session Export Command

```python
def handle_export() -> None:
    """Export current session with format selection."""
    from rich.prompt import Prompt
    
    # Get format choice
    format_choice = Prompt.ask(
        "Export format",
        choices=["json", "txt", "md"],
        default="json"
    )
    
    # Get filename
    filename = Prompt.ask(
        "Filename",
        default=f"session.{format_choice}"
    )
    
    try:
        # Implement export logic here
        console.print(f"✅ Session exported to {filename}")
    except Exception as e:
        console.print(f"❌ Export failed: {e}")

slash_commands["/export"] = SlashCommand(
    name="export",
    description="Export current session",
    handler=handle_export,
    usage="/export"
)
```

## Utility Commands

### System Information Command

```python
def handle_sysinfo() -> None:
    """Display system information."""
    import platform
    import psutil
    from rich.table import Table
    
    table = Table(title="System Information")
    table.add_column("Property")
    table.add_column("Value")
    
    # System info
    table.add_row("OS", platform.system())
    table.add_row("OS Version", platform.release())
    table.add_row("Architecture", platform.machine())
    table.add_row("Python Version", platform.python_version())
    
    # Memory info
    memory = psutil.virtual_memory()
    table.add_row("Total Memory", f"{memory.total // (1024**3)} GB")
    table.add_row("Available Memory", f"{memory.available // (1024**3)} GB")
    table.add_row("Memory Usage", f"{memory.percent}%")
    
    console.print(table)

slash_commands["/sysinfo"] = SlashCommand(
    name="sysinfo",
    description="Show system information",
    handler=handle_sysinfo,
    usage="/sysinfo"
)
```

## Best Practices

### Error Handling

```python
def handle_safe_command() -> None:
    """Example of proper error handling."""
    try:
        # Your command logic here
        result = some_operation()
        console.print(f"✅ Success: {result}")
        
    except FileNotFoundError as e:
        console.print(f"❌ File not found: {e}")
    except PermissionError:
        console.print("❌ Permission denied")
    except Exception as e:
        console.print(f"❌ Unexpected error: {e}")
        # Log the error for debugging
        import logging
        logging.error(f"Command failed: {e}", exc_info=True)
```

### Input Validation

```python
def handle_validated_command() -> None:
    """Example with input validation."""
    from rich.prompt import Prompt, IntPrompt
    
    # Validate string input
    name = Prompt.ask("Enter name", default="user")
    if not name.isalpha():
        console.print("❌ Name must contain only letters")
        return
    
    # Validate numeric input
    try:
        count = IntPrompt.ask("Enter count", default=1)
        if count < 1:
            console.print("❌ Count must be positive")
            return
    except ValueError:
        console.print("❌ Invalid number")
        return
    
    console.print(f"✅ Processing {count} items for {name}")
```

### Performance Considerations

```python
def handle_async_command() -> None:
    """Example of handling long-running operations."""
    import time
    from rich.progress import track
    
    # Show progress for long operations
    items = range(100)
    
    for item in track(items, description="Processing..."):
        time.sleep(0.01)  # Simulate work
    
    console.print("✅ Processing complete")
```

## Testing Custom Commands

### Unit Tests

```python
# tests/test_custom_commands.py
import pytest
from unittest.mock import patch
from murlix.slash_commands import handle_time

def test_time_command():
    """Test time command execution."""
    with patch('murlix.slash_commands.console') as mock_console:
        handle_time()
        mock_console.print.assert_called_once()

def test_git_command_no_repo():
    """Test git command in non-git directory."""
    with patch('subprocess.run') as mock_run:
        mock_run.side_effect = subprocess.CalledProcessError(1, 'git')
        
        with patch('murlix.slash_commands.console') as mock_console:
            handle_git()
            mock_console.print.assert_called_with("❌ Not a git repository")
```

## Command Organization

### Grouping Related Commands

```python
# Group related commands with prefixes
slash_commands.update({
    "/git": git_status_command,
    "/git-log": git_log_command,
    "/git-diff": git_diff_command,
    
    "/sys-info": system_info_command,
    "/sys-proc": process_list_command,
    "/sys-disk": disk_usage_command,
})
```

### Conditional Command Loading

```python
def load_optional_commands():
    """Load commands based on available dependencies."""
    
    # Git commands (if git is available)
    if shutil.which('git'):
        slash_commands["/git"] = git_status_command
    
    # Docker commands (if docker is available)
    if shutil.which('docker'):
        slash_commands["/docker"] = docker_status_command
    
    # System commands (if psutil is available)
    try:
        import psutil
        slash_commands["/sysinfo"] = system_info_command
    except ImportError:
        pass
```

## Distribution

### Plugin Architecture

```python
# For distributable command packages
class CustomCommandPlugin:
    def get_commands(self) -> dict:
        """Return dictionary of commands to register."""
        return {
            "/mycmd": SlashCommand(
                name="mycmd",
                description="My custom command",
                handler=self.handle_mycmd,
                usage="/mycmd"
            )
        }
    
    def handle_mycmd(self):
        console.print("My custom command executed!")

# Register plugin commands
plugin = CustomCommandPlugin()
slash_commands.update(plugin.get_commands())
```

## Next Steps

- **[Extending Murlix](extending.md)**: Learn about other extension points
- **[Agent Configuration](agent-configuration.md)**: Customize the AI agent
- **[Architecture](architecture.md)**: Understand the system design

!!! success "Command Creation Success"
    With these patterns, you can create powerful custom commands that integrate seamlessly with Murlix's interactive interface.