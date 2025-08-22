# Installation

Get Murlix up and running on your system in just a few minutes. This guide covers all the prerequisites and installation steps for different platforms.

## Prerequisites

Before installing Murlix, ensure you have the following requirements:

### System Requirements

=== "Python"
    ```bash
    # Python 3.13 or higher is required
    python --version
    # Should output: Python 3.13.x or higher
    ```

=== "UV Package Manager"
    ```bash
    # Install UV (recommended package manager)
    curl -LsSf https://astral.sh/uv/install.sh | sh
    
    # Or via pip
    pip install uv
    
    # Verify installation
    uv --version
    ```

=== "Git"
    ```bash
    # Git is required for cloning the repository
    git --version
    # Should output: git version 2.x.x or higher
    ```

### API Requirements

To use Murlix, you'll need access to Google's AI services. Choose one of the following options:

!!! info "API Options"
    === "Google AI API (Recommended)"
        - **Free tier available**
        - Easier setup for personal use
        - Get your API key from [Google AI Studio](https://makersuite.google.com/app/apikey)
    
    === "Vertex AI"
        - **Enterprise features**
        - Better for production use
        - Requires Google Cloud Project setup

## Installation Methods

### Method 1: Quick Install (Recommended)

The fastest way to get started with Murlix:

```bash
# 1. Clone the repository
git clone https://github.com/manohar3000/murlix.git
cd murlix

# 2. Install dependencies
uv sync

# 3. Verify installation
uv run murlix --help
```

### Method 2: Development Install

For contributors or those who want to modify Murlix:

```bash
# 1. Fork and clone your fork
git clone https://github.com/YOUR_USERNAME/murlix.git
cd murlix

# 2. Install in development mode
uv sync --dev

# 3. Install pre-commit hooks (optional)
uv run pre-commit install

# 4. Run tests to verify setup
uv run pytest
```

### Method 3: Docker Install

!!! warning "Coming Soon"
    Docker installation method is planned for a future release. For now, please use the direct installation methods above.

## Configuration

### Environment Setup

Create a `.env` file to configure your API credentials:

```bash
# Copy the example environment file
cp .env.example .env

# Edit the file with your preferred editor
nano .env  # or vim, code, etc.
```

Configure your environment variables:

=== "Google AI API"
    ```bash
    # .env file
    USER_ID=your_username
    GOOGLE_API_KEY=your_google_ai_api_key
    ```

=== "Vertex AI"
    ```bash
    # .env file
    USER_ID=your_username
    VERTEX_AI_PROJECT=your_project_id
    VERTEX_AI_LOCATION=us-central1
    
    # You'll also need to authenticate with gcloud
    gcloud auth application-default login
    ```

### Getting API Keys

#### Google AI API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the generated key to your `.env` file

#### Vertex AI Setup

1. Create a Google Cloud Project:
   ```bash
   gcloud projects create your-project-id
   gcloud config set project your-project-id
   ```

2. Enable the Vertex AI API:
   ```bash
   gcloud services enable aiplatform.googleapis.com
   ```

3. Authenticate:
   ```bash
   gcloud auth application-default login
   ```

## Verification

Test your installation with these verification steps:

### Basic Functionality

```bash
# Test basic CLI functionality
uv run murlix --help

# Expected output:
# Usage: murlix [OPTIONS] COMMAND [ARGS]...
# 
# A beautiful CLI chat interface powered by Google's ADK
# ...
```

### API Connection

```bash
# Test with a simple query
uv run murlix --query "Hello, can you hear me?"

# Expected output:
# ╭─ Murlix ─────────────────────────────────────────────╮
# │ Hello! Yes, I can hear you perfectly. How can I     │
# │ help you today?                                      │
# ╰──────────────────────────────────────────────────────╯
```

### Interactive Mode

```bash
# Start interactive session
uv run murlix

# You should see the Murlix welcome screen with ASCII art
```

## Troubleshooting

### Common Issues

!!! failure "Python Version Error"
    **Problem**: `python: command not found` or version < 3.13
    
    **Solution**: 
    ```bash
    # Install Python 3.13+ using pyenv (recommended)
    curl https://pyenv.run | bash
    pyenv install 3.13.0
    pyenv global 3.13.0
    ```

!!! failure "UV Installation Issues"
    **Problem**: `uv: command not found`
    
    **Solution**:
    ```bash
    # Try alternative installation method
    pip install uv
    
    # Or use curl method
    curl -LsSf https://astral.sh/uv/install.sh | sh
    source ~/.bashrc  # or restart terminal
    ```

!!! failure "API Authentication Errors"
    **Problem**: `Authentication failed` or `API key invalid`
    
    **Solution**:
    1. Verify your API key is correct in `.env`
    2. Check that the API is enabled in your Google Cloud Console
    3. For Vertex AI, ensure you've run `gcloud auth application-default login`

!!! failure "Permission Denied"
    **Problem**: Permission errors during installation
    
    **Solution**:
    ```bash
    # Don't use sudo with uv, instead fix permissions
    chown -R $USER:$USER ~/.local/share/uv
    
    # Or install in user directory
    uv sync --user
    ```

### Getting Help

If you encounter issues not covered here:

1. **Check the logs**: Murlix creates detailed logs in `~/.murlix/logs/`
2. **Search issues**: Look through [GitHub Issues](https://github.com/manohar3000/murlix/issues)
3. **Create an issue**: Report bugs or ask questions on GitHub
4. **Community support**: Join our discussions for community help

### Performance Optimization

For optimal performance:

```bash
# Enable UV's faster resolver
export UV_RESOLVER=uv

# Use faster HTTP client
export UV_HTTP_TIMEOUT=30

# Enable parallel downloads
export UV_CONCURRENT_DOWNLOADS=10
```

## Next Steps

Now that Murlix is installed:

1. **[Quick Start Guide](quick-start.md)** - Learn the basics with your first conversation
2. **[Configuration](configuration.md)** - Customize Murlix for your workflow  
3. **[Interactive Mode](../user-guide/interactive-mode.md)** - Master the chat interface

!!! success "Installation Complete!"
    Congratulations! Murlix is now installed and ready to use. Try running `uv run murlix` to start your first AI conversation in the terminal.