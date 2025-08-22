# Configuration

Murlix is designed to work great out of the box, but it's also highly customizable. This guide covers all the ways you can configure Murlix to match your workflow and preferences.

## Environment Configuration

### Basic Environment Setup

The primary way to configure Murlix is through environment variables. Create a `.env` file in your project root:

```bash
# Copy the example file
cp .env.example .env

# Edit with your preferred editor
vim .env  # or nano, code, etc.
```

### Core Settings

=== "User Configuration"
    ```bash
    # .env file
    
    # User identification (used for session management)
    USER_ID=your_username
    
    # Optional: Custom user display name
    USER_DISPLAY_NAME="Your Full Name"
    ```

=== "API Configuration"
    ```bash
    # Google AI API (recommended for personal use)
    GOOGLE_API_KEY=your_google_ai_api_key
    
    # OR Vertex AI (for enterprise use)
    VERTEX_AI_PROJECT=your_project_id
    VERTEX_AI_LOCATION=us-central1
    VERTEX_AI_CREDENTIALS_PATH=/path/to/credentials.json
    ```

=== "Advanced Settings"
    ```bash
    # Database location (optional)
    DATABASE_PATH=./custom_murlix_data.db
    
    # Logging level
    LOG_LEVEL=INFO  # DEBUG, INFO, WARNING, ERROR
    
    # Session timeout (in minutes)
    SESSION_TIMEOUT=1440  # 24 hours default
    
    # Maximum conversation history
    MAX_HISTORY_LENGTH=100
    ```

## API Configuration

### Google AI API Setup

The Google AI API is the recommended option for personal use:

1. **Get your API key**:
   - Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Sign in and create a new API key
   - Copy the key to your `.env` file

2. **Configure in `.env`**:
   ```bash
   GOOGLE_API_KEY=AIzaSyD...your_key_here
   ```

3. **Optional model selection**:
   ```bash
   # Override the default model
   GOOGLE_AI_MODEL=gemini-2.0-flash
   ```

### Vertex AI Setup

For enterprise users or advanced features:

1. **Set up Google Cloud Project**:
   ```bash
   # Create project
   gcloud projects create your-project-id
   gcloud config set project your-project-id
   
   # Enable Vertex AI API
   gcloud services enable aiplatform.googleapis.com
   ```

2. **Authentication options**:

   === "Application Default Credentials"
       ```bash
       # Authenticate with your user account
       gcloud auth application-default login
       ```
   
   === "Service Account"
       ```bash
       # Create service account
       gcloud iam service-accounts create murlix-service-account
       
       # Download credentials
       gcloud iam service-accounts keys create credentials.json \
         --iam-account=murlix-service-account@your-project-id.iam.gserviceaccount.com
       ```

3. **Configure in `.env`**:
   ```bash
   VERTEX_AI_PROJECT=your_project_id
   VERTEX_AI_LOCATION=us-central1
   VERTEX_AI_CREDENTIALS_PATH=./credentials.json  # if using service account
   ```

## Agent Customization

### Default Agent Configuration

Murlix's AI agent can be customized by modifying `src/murlix/core_agent/agent.py`:

```python
from google_adk import LlmAgent

# Custom agent configuration
root_agent = LlmAgent(
    model='gemini-2.0-flash',
    name='Murlix_Assistant',
    instruction="""
    You are Murlix, a helpful AI assistant focused on providing clear,
    accurate, and actionable responses. You excel at:
    
    - Programming and technical support
    - Problem-solving and analysis  
    - Educational explanations
    - Creative collaboration
    
    Always be concise but thorough, and ask clarifying questions when needed.
    """,
    tools=mcp_toolsets,  # Your custom tools here
)
```

### Custom Instructions

Tailor the agent's behavior for your specific use case:

=== "Development Focus"
    ```python
    instruction="""
    You are a senior software engineer and mentor. Focus on:
    - Code quality and best practices
    - Architecture and design patterns
    - Performance optimization
    - Security considerations
    - Testing strategies
    
    Always provide code examples and explain your reasoning.
    """
    ```

=== "Research Assistant"
    ```python
    instruction="""
    You are a research assistant specializing in:
    - Literature reviews and citations
    - Data analysis and interpretation
    - Methodology suggestions
    - Academic writing support
    
    Be thorough, cite sources when possible, and suggest follow-up research.
    """
    ```

=== "Creative Partner"
    ```python
    instruction="""
    You are a creative collaborator focused on:
    - Brainstorming and ideation
    - Writing and storytelling
    - Design thinking
    - Problem reframing
    
    Be imaginative, ask thought-provoking questions, and build on ideas.
    """
    ```

### Model Selection

Choose the best model for your needs:

```python
# Available models (check Google AI documentation for latest)
models = {
    'gemini-2.0-flash': 'Fast, efficient, good for most tasks',
    'gemini-1.5-pro': 'More capable, better for complex reasoning',
    'gemini-1.5-flash': 'Balanced performance and speed'
}

# Configure in agent.py
root_agent = LlmAgent(
    model='gemini-2.0-flash',  # Change this
    # ... other configuration
)
```

## UI Customization

### Terminal Appearance

While Murlix's UI is primarily controlled by the Rich library, you can customize some aspects:

#### Color Schemes

Create a custom color configuration in `src/murlix/ui.py`:

```python
# Custom color scheme
CUSTOM_COLORS = {
    'primary': '#667eea',
    'secondary': '#764ba2', 
    'accent': '#f093fb',
    'success': '#4facfe',
    'warning': '#feca57',
    'error': '#ff6b6b'
}
```

#### ASCII Art

Customize the welcome screen by modifying the ASCII art in `src/murlix/ui.py`:

```python
CUSTOM_ASCII_ART = """
╭─ Your Custom ASCII Art Here ─╮
│                               │
│  ████  ████  ████  ████       │
│  ████  ████  ████  ████       │
│                               │
╰───────────────────────────────╯
"""
```

### Response Formatting

Customize how AI responses are displayed:

```python
# In src/murlix/ui.py
def format_response(content: str, agent_name: str = "Murlix") -> Panel:
    return Panel(
        content,
        title=f"─ {agent_name} ─",
        title_align="left",
        border_style="blue",
        padding=(1, 2),
        # Add your custom styling here
    )
```

## Database Configuration

### Custom Database Location

By default, Murlix stores data in `my_agent_data.db`. You can customize this:

```bash
# In .env file
DATABASE_PATH=/path/to/your/custom/database.db

# Or use environment variable
export MURLIX_DATABASE_PATH=/path/to/database.db
```

### Database Schema Customization

For advanced users, you can extend the database schema by modifying the session management code:

```python
# In src/murlix/session.py
# Add custom fields to session metadata
async def create_session_with_metadata(self, metadata: dict):
    # Your custom session creation logic
    pass
```

## Logging Configuration

### Log Levels

Control the verbosity of Murlix's logging:

```bash
# In .env file
LOG_LEVEL=DEBUG    # Most verbose
LOG_LEVEL=INFO     # Default
LOG_LEVEL=WARNING  # Warnings and errors only
LOG_LEVEL=ERROR    # Errors only
```

### Custom Log Location

```bash
# In .env file
LOG_FILE_PATH=/path/to/murlix.log

# Or disable file logging
LOG_TO_FILE=false
```

### Log Format

Customize log formatting in your configuration:

```python
# Custom logging configuration
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('murlix.log'),
        logging.StreamHandler()
    ]
)
```

## Performance Tuning

### Response Optimization

```bash
# In .env file

# Adjust response timeout (seconds)
RESPONSE_TIMEOUT=30

# Enable response streaming for faster perceived performance
ENABLE_STREAMING=true

# Limit conversation context for faster responses
MAX_CONTEXT_MESSAGES=20
```

### Memory Management

```bash
# Control memory usage
MAX_SESSION_CACHE=10      # Number of sessions to keep in memory
CLEANUP_INTERVAL=3600     # Cleanup interval in seconds
AUTO_CLEANUP_ENABLED=true # Enable automatic cleanup
```

## Security Configuration

### API Key Security

!!! warning "Security Best Practices"
    - Never commit API keys to version control
    - Use environment variables or secure key management
    - Regularly rotate your API keys
    - Use least-privilege access for service accounts

### Local Data Security

```bash
# In .env file

# Encrypt local database (requires additional setup)
ENCRYPT_DATABASE=true
DATABASE_ENCRYPTION_KEY=your_encryption_key

# Limit session data retention
MAX_SESSION_AGE_DAYS=30
AUTO_DELETE_OLD_SESSIONS=true
```

## Configuration Validation

### Verify Your Setup

Murlix includes a configuration validation command:

```bash
# Check your configuration
uv run murlix config check

# Output example:
✓ Environment file found
✓ API credentials configured
✓ Database accessible
✓ Agent configuration valid
⚠ Log directory not writable (using default)
```

### Common Configuration Issues

!!! failure "API Key Not Working"
    **Symptoms**: Authentication errors, API failures
    
    **Solutions**:
    ```bash
    # Check API key format
    echo $GOOGLE_API_KEY | wc -c  # Should be ~40 characters
    
    # Test API access
    curl -H "Authorization: Bearer $GOOGLE_API_KEY" \
         "https://generativelanguage.googleapis.com/v1beta/models"
    ```

!!! failure "Database Permission Errors"
    **Symptoms**: Cannot create or access database
    
    **Solutions**:
    ```bash
    # Check directory permissions
    ls -la $(dirname $DATABASE_PATH)
    
    # Fix permissions
    chmod 755 $(dirname $DATABASE_PATH)
    ```

!!! failure "Import Errors"
    **Symptoms**: Module not found errors
    
    **Solutions**:
    ```bash
    # Reinstall dependencies
    uv sync --reinstall
    
    # Check Python path
    uv run python -c "import sys; print(sys.path)"
    ```

## Configuration Templates

### Development Template

```bash
# .env for development
USER_ID=dev_user
GOOGLE_API_KEY=your_api_key
LOG_LEVEL=DEBUG
MAX_HISTORY_LENGTH=50
ENABLE_STREAMING=true
DATABASE_PATH=./dev_murlix.db
```

### Production Template

```bash
# .env for production
USER_ID=prod_user
VERTEX_AI_PROJECT=your_production_project
VERTEX_AI_LOCATION=us-central1
LOG_LEVEL=INFO
MAX_HISTORY_LENGTH=100
SESSION_TIMEOUT=2880  # 48 hours
ENCRYPT_DATABASE=true
AUTO_CLEANUP_ENABLED=true
```

### Minimal Template

```bash
# .env minimal setup
USER_ID=your_username
GOOGLE_API_KEY=your_api_key
```

## Next Steps

With Murlix configured to your needs:

1. **[Interactive Mode](../user-guide/interactive-mode.md)** - Explore all the features
2. **[Extending Murlix](../developer-guide/extending.md)** - Add custom functionality
3. **[Custom Commands](../developer-guide/custom-commands.md)** - Create your own slash commands

!!! tip "Configuration Tips"
    - Start with minimal configuration and add settings as needed
    - Keep sensitive credentials in environment variables
    - Document your custom configurations for team members
    - Test configuration changes in a development environment first