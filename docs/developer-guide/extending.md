# Extending Murlix

Learn how to extend Murlix with custom functionality, integrate with external tools, and create powerful AI-assisted workflows.

## Extension Overview

Murlix is designed to be highly extensible through several extension points:

- **Custom Slash Commands**: Add new interactive commands
- **Agent Tools**: Integrate external APIs and services  
- **UI Components**: Create custom display elements
- **Database Extensions**: Add custom data storage
- **Workflow Integration**: Connect with development tools

## Getting Started

### Development Setup

1. **Fork and clone the repository**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/murlix.git
   cd murlix
   ```

2. **Install in development mode**:
   ```bash
   uv sync --dev
   ```

3. **Verify setup**:
   ```bash
   uv run murlix --help
   ```

## Extension Types

### 1. Custom Slash Commands

Add new commands to the interactive interface:

```python
# In src/murlix/slash_commands.py

def handle_export() -> None:
    """Export current session to file."""
    console.print("Exporting session...")
    # Implementation here

# Register the command
slash_commands["/export"] = SlashCommand(
    name="export",
    description="Export current session",
    handler=handle_export,
    usage="/export [format]"
)
```

### 2. Agent Tool Integration

Add external tools to the AI agent:

```python
# In src/murlix/core_agent/agent.py

from google_adk import Tool

def weather_tool(location: str) -> str:
    """Get weather information for a location."""
    # Implementation here
    return f"Weather in {location}: Sunny, 72°F"

# Add to toolset
custom_tools = [
    Tool(
        name="get_weather",
        description="Get current weather for a location",
        handler=weather_tool
    )
]

mcp_toolsets.extend(custom_tools)
```

### 3. Custom UI Components

Create new display components:

```python
# In src/murlix/ui.py

def display_weather_panel(weather_data: dict) -> None:
    """Display weather information in a custom panel."""
    panel = Panel(
        f"🌤️ {weather_data['condition']}\n"
        f"🌡️ {weather_data['temperature']}°F\n"
        f"💨 {weather_data['wind']} mph",
        title=f"Weather in {weather_data['location']}",
        border_style="blue"
    )
    console.print(panel)
```

## Advanced Extensions

### Database Schema Extensions

Add custom tables and data:

```python
# Custom database extension
class ExtendedSessionManager(SessionManager):
    async def create_custom_table(self):
        """Create custom data table."""
        await self.db.execute("""
            CREATE TABLE IF NOT EXISTS custom_data (
                id TEXT PRIMARY KEY,
                session_id TEXT REFERENCES sessions(id),
                data_type TEXT,
                content JSON,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)
```

### Plugin System

Create a basic plugin architecture:

```python
# Plugin base class
class MurlixPlugin:
    def __init__(self, name: str):
        self.name = name
    
    def initialize(self):
        """Initialize plugin."""
        pass
    
    def register_commands(self) -> dict:
        """Return dict of commands to register."""
        return {}
    
    def register_tools(self) -> list:
        """Return list of tools to register."""
        return []

# Example plugin
class WeatherPlugin(MurlixPlugin):
    def __init__(self):
        super().__init__("weather")
    
    def register_commands(self):
        return {
            "/weather": SlashCommand(
                name="weather",
                description="Get weather information",
                handler=self.handle_weather,
                usage="/weather <location>"
            )
        }
    
    def handle_weather(self):
        # Implementation
        pass
```

## Integration Examples

### Git Integration

```python
def handle_git_status() -> None:
    """Show git status in formatted panel."""
    import subprocess
    
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"],
            capture_output=True,
            text=True,
            check=True
        )
        
        if result.stdout:
            panel = Panel(
                result.stdout,
                title="Git Status",
                border_style="green"
            )
            console.print(panel)
        else:
            console.print("✅ Working directory clean")
    except subprocess.CalledProcessError:
        console.print("❌ Not a git repository")
```

### File System Operations

```python
def handle_ls() -> None:
    """List directory contents."""
    import os
    from rich.table import Table
    
    table = Table(title="Directory Contents")
    table.add_column("Name")
    table.add_column("Type")
    table.add_column("Size")
    
    for item in os.listdir("."):
        item_type = "📁 Dir" if os.path.isdir(item) else "📄 File"
        size = "—" if os.path.isdir(item) else f"{os.path.getsize(item)} bytes"
        table.add_row(item, item_type, size)
    
    console.print(table)
```

## Testing Extensions

### Unit Testing

```python
# tests/test_extensions.py
import pytest
from murlix.slash_commands import handle_export

def test_export_command():
    """Test custom export command."""
    # Test implementation
    result = handle_export()
    assert result is not None
```

### Integration Testing

```python
def test_plugin_integration():
    """Test plugin integration."""
    plugin = WeatherPlugin()
    commands = plugin.register_commands()
    assert "/weather" in commands
```

## Best Practices

### Code Organization

- Keep extensions in separate modules
- Use clear naming conventions
- Document all public interfaces
- Follow existing code style

### Error Handling

```python
def safe_command_handler():
    """Example of proper error handling."""
    try:
        # Command implementation
        result = perform_operation()
        console.print(f"✅ Success: {result}")
    except Exception as e:
        console.print(f"❌ Error: {str(e)}")
        logger.error(f"Command failed: {e}")
```

### Performance Considerations

- Cache expensive operations
- Use async/await for I/O operations
- Implement proper resource cleanup
- Consider memory usage for large data

## Distribution

### Creating Plugins

Package extensions as separate Python packages:

```python
# setup.py for plugin
from setuptools import setup

setup(
    name="murlix-weather-plugin",
    version="1.0.0",
    packages=["murlix_weather"],
    install_requires=["murlix>=0.1.0"],
    entry_points={
        "murlix.plugins": [
            "weather = murlix_weather:WeatherPlugin"
        ]
    }
)
```

### Plugin Discovery

Implement automatic plugin discovery:

```python
def load_plugins():
    """Load all installed plugins."""
    import pkg_resources
    
    plugins = []
    for entry_point in pkg_resources.iter_entry_points("murlix.plugins"):
        plugin_class = entry_point.load()
        plugin = plugin_class()
        plugins.append(plugin)
    
    return plugins
```

## Contributing Extensions

### Contribution Guidelines

1. **Fork the repository**
2. **Create feature branch**: `git checkout -b feature/my-extension`
3. **Implement extension** with tests and documentation
4. **Submit pull request** with clear description

### Review Process

Extensions are reviewed for:
- Code quality and style
- Test coverage
- Documentation completeness
- Security considerations
- Performance impact

## Next Steps

- **[Custom Commands](custom-commands.md)**: Detailed slash command creation
- **[Agent Configuration](agent-configuration.md)**: AI agent customization
- **[Architecture](architecture.md)**: Understanding Murlix internals

!!! success "Extension Success"
    With these extension patterns, you can create powerful customizations that integrate seamlessly with Murlix's architecture.