<div align="center">

# 🔮 Murlix

### *Your Terminal-Based AI Coding Companion*

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Google Gemini](https://img.shields.io/badge/powered%20by-Google%20Gemini%202.0%20Flash-green.svg)](https://ai.google.dev/)
[![MCP Protocol](https://img.shields.io/badge/supports-MCP%20Protocol-orange.svg)](https://modelcontextprotocol.io/)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

*Meet Murlix - a beautiful, powerful, and intelligent coding assistant that lives right in your terminal.*

</div>

---

## ✨ What is Murlix?

Murlix is more than just another AI assistant. It's a **terminal-native coding companion** that combines the power of Google's cutting-edge Gemini 2.0 Flash model with seamless integrations to your development workflow. Whether you're debugging complex code, exploring new frameworks, or managing git repositories, Murlix provides intelligent, context-aware assistance without ever leaving your terminal.

### 🎯 **Core Philosophy**
- **Terminal-First**: Beautiful CLI experience with rich formatting and intuitive interactions
- **Context-Aware**: Deep integration with your filesystem, git repositories, and documentation
- **Developer-Focused**: Built by developers, for developers, with real workflow needs in mind

---

## 🚀 **Key Features**

### 🧠 **Intelligent AI Assistant**
- Powered by **Google Gemini 2.0 Flash** - the latest and most capable model
- Context-aware responses based on your project structure
- Natural language interface for complex coding tasks

### 🔧 **Integrated Development Tools**
- **File System Operations**: Read, write, search, and manage files and directories
- **Git Integration**: Commit, branch, diff, log, and manage repository history  
- **Live Documentation**: Access up-to-date, version-specific documentation via Context7
- **Project Analysis**: Understand codebases instantly

### 🎨 **Beautiful Terminal Interface**
```
███╗   ███╗██╗   ██╗██████╗ ██╗     ██╗██╗  ██╗
████╗ ████║██║   ██║██╔══██╗██║     ██║╚██╗██╔╝
██╔████╔██║██║   ██║██████╔╝██║     ██║ ╚███╔╝ 
██║╚██╔╝██║██║   ██║██╔══██╗██║     ██║ ██╔██╗ 
██║ ╚═╝ ██║╚██████╔╝██║  ██║███████╗██║██╔╝ ██╗
╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═╝
```

- Rich text formatting with colors and styling
- Interactive command system with auto-completion
- Beautiful welcome screens and status indicators
- Responsive layout that adapts to your terminal

### ⚡ **Slash Commands**
Murlix includes powerful slash commands for enhanced productivity:

| Command | Description | Usage |
|---------|-------------|-------|
| `/help` | Show available commands and usage | `/help` |
| `/model` | View or switch AI models | `/model list \| set <model>` |
| `/clear` | Clear conversation history | `/clear` |

---

## 🛠 **Installation & Setup**

### **Prerequisites**
- Python 3.11 or higher
- Node.js (for MCP server tools)
- Git (for repository operations)

### **Quick Start**

1. **Clone the Repository**
   ```bash
   git clone https://github.com/manohar3000/murlix.git
   cd murlix
   ```

2. **Set Up Environment**
   ```bash
   # Install dependencies using uv (recommended)
   pip install uv
   uv sync
   
   # Or using pip
   pip install -e .
   ```

3. **Configure API Keys**
   ```bash
   # Copy environment template
   cp .env.example .env
   
   # Add your Google AI API key
   echo "GOOGLE_API_KEY=your_api_key_here" >> .env
   ```

4. **Launch Murlix**
   ```bash
   uv run main.py
   ```

---

## 🎮 **Usage Examples**

### **File Operations**
```
💬 You: "Can you read my main.py file and explain what it does?"
🤖 Murlix: *Reads and analyzes your file structure, providing detailed explanations*
```

### **Code Generation**
```
💬 You: "Create a FastAPI endpoint for user authentication with JWT tokens"
🤖 Murlix: *Generates production-ready code with proper error handling and security*
```

### **Git Operations**
```
💬 You: "Show me the recent commits and create a new feature branch"
🤖 Murlix: *Analyzes git history and creates branch with descriptive name*
```

### **Documentation Lookup**
```
💬 You: "How do I use the latest React Hooks API?"
🤖 Murlix: *Fetches current documentation and provides practical examples*
```

---

## 🏗 **Project Structure**

```
murlix/
├── 📁 core_agent/          # AI agent core logic
│   ├── agent.py           # Main agent implementation
│   └── models.py          # Model management
├── 📁 cli/                # Command-line interface
│   ├── chat_loop.py       # Interactive chat system
│   ├── session.py         # Session management
│   ├── slash_commands.py  # Command handlers
│   └── commands.py        # Command definitions
├── 📄 main.py             # Application entry point
├── 📄 pyproject.toml      # Project configuration
└── 📄 utils.py            # Utility functions
```

---

## 🔌 **Integrations**

### **Model Context Protocol (MCP)**
Murlix leverages the Model Context Protocol for seamless tool integration:

- **File System Server**: Complete file and directory operations
- **Context7**: Real-time documentation and examples
- **Git Server**: Full repository management capabilities

### **Supported Models**
- **Google Gemini 2.0 Flash** (Default) - Latest multimodal capabilities
- Extensible architecture for additional models

---

## 🤝 **Contributing**

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b amazing-feature`
3. **Make your changes** with proper tests
4. **Commit with clear messages**: `git commit -m "Add amazing feature"`
5. **Push to your branch**: `git push origin amazing-feature`
6. **Open a Pull Request**

### **Development Setup**
```bash
# Clone your fork
git clone https://github.com/yourusername/murlix.git
cd murlix

# Install in development mode
uv sync --dev

# Run tests
uv run pytest

# Format code
uv run black .
uv run isort .
```

---

## 📝 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 **Acknowledgments**

- **Google AI** for the powerful Gemini models
- **Model Context Protocol** for seamless tool integration
- **Rich** library for beautiful terminal interfaces
- **Questionary** for interactive prompts

---

<div align="center">

### 🌟 **Ready to Transform Your Coding Experience?**

**[Get Started Now](#installation--setup)** • **[View Examples](#usage-examples)** • **[Contribute](#contributing)**

*Built with ❤️ for developers who love their terminals*

</div>