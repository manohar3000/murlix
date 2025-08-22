# Frequently Asked Questions

Find answers to common questions about Murlix, from installation to advanced usage.

## General Questions

### What is Murlix?

Murlix is a beautiful CLI chat interface powered by Google's Agent Development Kit (ADK). It transforms your terminal into an elegant AI conversation space with persistent sessions, rich formatting, and intuitive commands.

### How is Murlix different from other AI chat tools?

Murlix is specifically designed for terminal users and developers who want to:

- **Stay in their workflow**: No need to switch to web browsers or separate apps
- **Maintain context**: Persistent sessions that survive restarts
- **Beautiful interface**: Rich terminal UI with ASCII art and elegant formatting
- **Local control**: Your conversations are stored locally in SQLite
- **Extensible**: Easy to customize and extend with your own commands

### Is Murlix free to use?

Murlix itself is open source and free. However, you'll need access to Google's AI services:

- **Google AI API**: Has a free tier with generous limits
- **Vertex AI**: Paid service with enterprise features

## Installation & Setup

### What are the system requirements?

- **Python**: 3.13 or higher
- **Package Manager**: UV (recommended) or pip
- **Operating System**: Linux, macOS, or Windows
- **Terminal**: Modern terminal with Unicode support
- **Internet**: Connection required for AI API calls

### Why do I need Python 3.13+?

Murlix uses modern Python features and the latest versions of dependencies that require Python 3.13+. This ensures optimal performance and access to the newest language features.

### Can I use Murlix without UV?

While UV is recommended for its speed and reliability, you can use pip:

```bash
# Install with pip (not recommended)
pip install -r requirements.txt
python -m murlix
```

However, UV provides better dependency management and faster installations.

### How do I get a Google AI API key?

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Click "Create API Key"
4. Copy the key to your `.env` file as `GOOGLE_API_KEY=your_key_here`

## Usage Questions

### How do I start a conversation?

Simply run:
```bash
uv run murlix
```

This launches the interactive mode with a beautiful welcome screen and starts a new session.

### Can I continue previous conversations?

Yes! Murlix has excellent session management:

- **Continue latest**: `uv run murlix continue-chat`
- **Pick any session**: `uv run murlix load-chat`
- **View all sessions**: Use `/sessions` command in interactive mode

### How do I ask quick questions without starting a session?

Use the query option:
```bash
uv run murlix --query "Your question here"
```

This gives you a quick response without creating a persistent session.

### What slash commands are available?

The main slash commands are:

- `/help` - Show all available commands
- `/quit` - Exit Murlix
- `/sessions` - List all your sessions
- `/clear` - Clear the terminal screen
- `/new` - Instructions for starting a new session

Type `/help` in interactive mode for the complete list.

### How do I exit Murlix?

You can exit in several ways:

- Type `/quit` in interactive mode
- Press `Ctrl+C` at any time
- Close the terminal window

Your session is automatically saved when you exit.

## Technical Questions

### Where are my conversations stored?

Conversations are stored locally in a SQLite database file called `my_agent_data.db` in your project directory. This gives you complete control over your data.

### Can I change the database location?

Yes, set the `DATABASE_PATH` environment variable:
```bash
# In your .env file
DATABASE_PATH=/path/to/your/database.db
```

### How much data does Murlix store?

Murlix stores:
- Conversation history (messages and responses)
- Session metadata (creation time, status)
- User preferences and settings
- Event logs (for debugging)

The database typically grows slowly unless you have very long conversations.

### Can I export my conversations?

Yes, you can export sessions:
```bash
# Export all sessions to JSON
uv run murlix sessions export --output sessions.json

# Export specific session
uv run murlix sessions export abc123def456 --format txt
```

### How do I back up my data?

Simply copy the database file:
```bash
cp my_agent_data.db backup_$(date +%Y%m%d).db
```

Or use the built-in export feature for human-readable backups.

## Performance & Troubleshooting

### Murlix is slow to respond. What can I do?

Check these common causes:

1. **Internet connection**: Ensure stable connection to Google's APIs
2. **API quotas**: Verify you haven't exceeded your API limits
3. **Long conversations**: Very long sessions can slow responses
4. **System resources**: Close other resource-intensive applications

### I'm getting API authentication errors

1. **Check your API key**: Ensure it's correctly set in your `.env` file
2. **Verify the key format**: Google AI API keys are about 40 characters long
3. **Test API access**: Try a simple query to verify the key works
4. **Check quotas**: Ensure you haven't exceeded your API limits

### The terminal display looks broken

This usually indicates terminal compatibility issues:

1. **Use a modern terminal**: iTerm2, Windows Terminal, or recent GNOME Terminal
2. **Enable Unicode support**: Ensure your terminal supports UTF-8
3. **Check terminal size**: Minimum 80x24 characters recommended
4. **Update terminal software**: Use the latest version of your terminal

### Murlix won't start

Common solutions:

1. **Check Python version**: `python --version` should show 3.13+
2. **Verify installation**: `uv sync` to reinstall dependencies
3. **Check permissions**: Ensure you can write to the directory
4. **Review logs**: Check error messages for specific issues

## Customization Questions

### Can I customize the appearance?

Yes, you can customize several aspects:

- **Colors**: Modify the color scheme in the source code
- **ASCII art**: Change the welcome screen design
- **Response formatting**: Adjust how AI responses are displayed

See the [Configuration](../getting-started/configuration.md) guide for details.

### How do I add custom commands?

You can add custom slash commands by:

1. Creating handler functions in `slash_commands.py`
2. Registering them in the command dictionary
3. Following the existing command patterns

See [Custom Commands](../developer-guide/custom-commands.md) for a detailed guide.

### Can I change the AI model?

Yes, you can configure the model in `src/murlix/core_agent/agent.py`:

```python
root_agent = LlmAgent(
    model='gemini-1.5-pro',  # Change this
    # ... other settings
)
```

### How do I customize the AI's behavior?

Modify the `instruction` parameter in the agent configuration:

```python
root_agent = LlmAgent(
    model='gemini-2.0-flash',
    instruction="Your custom instructions here...",
    # ... other settings
)
```

## Data & Privacy

### Is my data sent to Google?

Yes, your messages are sent to Google's AI services for processing. However:

- Conversations are stored locally on your machine
- You control what data is sent
- You can delete local data anytime
- Google's privacy policies apply to API usage

### Can I use Murlix offline?

No, Murlix requires an internet connection to communicate with Google's AI APIs. However, your session data is stored locally and available offline for viewing.

### How do I delete my conversation history?

You can delete sessions in several ways:

```bash
# Delete specific session
uv run murlix sessions delete abc123def456

# Delete all sessions
uv run murlix sessions delete --all

# Delete old sessions
uv run murlix sessions delete --older-than 30
```

Or simply delete the database file to remove all data.

## Development Questions

### Can I contribute to Murlix?

Yes! Murlix is open source. You can:

1. Report bugs and request features on GitHub
2. Submit pull requests with improvements
3. Add documentation and examples
4. Share your custom extensions

See [Contributing](contributing.md) for guidelines.

### How is Murlix built?

Murlix is built with:

- **Python 3.13+**: Modern Python features
- **Google ADK**: AI agent framework
- **Rich**: Beautiful terminal UI
- **Click**: CLI framework
- **SQLite**: Local data storage

### Can I build extensions for Murlix?

Absolutely! The modular architecture makes it easy to:

- Add new slash commands
- Create custom UI components
- Integrate external tools and APIs
- Modify agent behavior

### How do I set up a development environment?

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/murlix.git`
3. Install in development mode: `uv sync --dev`
4. Make your changes and test
5. Submit a pull request

## Getting Help

### Where can I get help?

1. **Documentation**: This comprehensive guide covers most topics
2. **GitHub Issues**: Report bugs and ask questions
3. **GitHub Discussions**: Community support and ideas
4. **Source Code**: Well-documented code for reference

### How do I report a bug?

1. Check if the issue already exists on GitHub
2. Create a new issue with:
   - Clear description of the problem
   - Steps to reproduce
   - Error messages (if any)
   - System information (OS, Python version, etc.)

### How do I request a feature?

1. Check existing feature requests on GitHub
2. Create a new issue with:
   - Clear description of the desired feature
   - Use case and motivation
   - Possible implementation ideas (optional)

### The documentation doesn't answer my question

If you can't find an answer:

1. Search through GitHub issues and discussions
2. Create a new discussion or issue
3. Be specific about what you're trying to achieve
4. Include relevant details about your setup

---

Still have questions? Check our [GitHub repository](https://github.com/manohar3000/murlix) or create an issue for support!