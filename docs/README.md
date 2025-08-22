# Murlix Documentation

This directory contains the complete documentation for Murlix, built with MkDocs Material theme and inspired by Anthropic's documentation design.

## 🚀 Quick Start

### Prerequisites

- Python 3.11+ (for documentation building)
- MkDocs Material and dependencies

### Local Development

**Option 1: Automated Setup (Recommended)**
```bash
# Run the setup script - it handles everything automatically
python setup-docs.py
```

**Option 2: Manual Setup**
```bash
# Create virtual environment
python -m venv docs-env

# Activate virtual environment
# On Windows:
docs-env\Scripts\activate
# On macOS/Linux:
source docs-env/bin/activate

# Install dependencies
pip install -r requirements-docs.txt

# Serve documentation
mkdocs serve
```

Visit `http://127.0.0.1:8000` to view the documentation.

3. **Build for production**:
   ```bash
   mkdocs build
   ```

### GitHub Pages Deployment

The documentation is automatically deployed to GitHub Pages via GitHub Actions when changes are pushed to the `main` branch. The workflow is defined in `.github/workflows/docs.yml`.

## 📁 Structure

```
docs/
├── index.md                    # Homepage with hero section
├── getting-started/           # Installation and setup guides
│   ├── overview.md
│   ├── installation.md
│   ├── quick-start.md
│   └── configuration.md
├── user-guide/               # User documentation
│   ├── interactive-mode.md
│   ├── session-management.md
│   ├── slash-commands.md
│   └── advanced-usage.md
├── developer-guide/          # Developer documentation
│   ├── architecture.md
│   ├── extending.md
│   ├── custom-commands.md
│   └── agent-configuration.md
├── api-reference/           # API and CLI reference
│   ├── cli-commands.md
│   ├── core-modules.md
│   └── session-api.md
├── examples/                # Usage examples
│   ├── basic-usage.md
│   ├── custom-agents.md
│   └── integration.md
├── support/                 # Help and support
│   ├── faq.md
│   ├── troubleshooting.md
│   └── contributing.md
├── stylesheets/            # Custom CSS
│   ├── extra.css
│   └── anthropic-style.css
├── javascripts/           # Custom JavaScript
│   └── mathjax.js
├── overrides/            # Template overrides
├── includes/             # Shared content
│   └── mkdocs.md
└── README.md            # This file
```

## 🎨 Design Features

### Anthropic-Inspired Styling

The documentation features a modern design inspired by Anthropic's Claude documentation:

- **Hero Section**: Gradient background with call-to-action buttons
- **Feature Cards**: Interactive cards with hover effects
- **Modern Typography**: Clean, readable fonts (Inter + JetBrains Mono)
- **Color Scheme**: Professional blue-grey palette with orange accents
- **Responsive Design**: Optimized for all screen sizes
- **Dark/Light Mode**: Automatic theme switching

### Advanced Features

- **Tabbed Content**: Organized information in clean tabs
- **Code Highlighting**: Syntax highlighting for multiple languages
- **Mermaid Diagrams**: Interactive flowcharts and diagrams
- **Search**: Fast, client-side search functionality
- **Navigation**: Intuitive navigation with breadcrumbs
- **Git Integration**: Automatic last-modified dates
- **Performance**: Minified output for fast loading

## 🛠️ Customization

### Styling

Custom styles are located in:
- `stylesheets/anthropic-style.css` - Main custom styling
- `stylesheets/extra.css` - Additional utilities

### Configuration

The main configuration is in `mkdocs.yml` at the project root. Key features:

- Material theme with custom palette
- Advanced markdown extensions
- Plugin configuration
- Navigation structure
- SEO optimization

### Content

All content is written in Markdown with enhanced features:

- **Admonitions**: Info, warning, tip, and error callouts
- **Code Blocks**: Syntax highlighting and copy buttons
- **Tables**: Responsive tables with hover effects
- **Links**: Automatic link generation and validation
- **Images**: Optimized image handling

## 📝 Writing Guidelines

### Style Guide

- Use clear, concise language
- Include practical examples
- Add code snippets for technical content
- Use admonitions for important information
- Structure content with proper headings

### Markdown Extensions

Available extensions include:

- `pymdownx.superfences` - Advanced code blocks
- `pymdownx.tabbed` - Tabbed content
- `pymdownx.details` - Collapsible sections
- `admonition` - Callout boxes
- `toc` - Table of contents
- `attr_list` - HTML attributes in Markdown

### Example Usage

```markdown
!!! tip "Pro Tip"
    Use specific examples to illustrate concepts.

=== "Tab 1"
    Content for first tab.

=== "Tab 2" 
    Content for second tab.

```python title="example.py"
def hello_world():
    print("Hello, World!")
```
```

## 🚀 Deployment

### Automatic Deployment

Documentation is automatically built and deployed via GitHub Actions:

1. Push changes to `main` branch
2. GitHub Actions builds the documentation
3. Built site is deployed to GitHub Pages
4. Available at `https://manohar3000.github.io/murlix`

### Manual Deployment

To deploy manually:

```bash
# Build and deploy to gh-pages branch
mkdocs gh-deploy

# Or build locally and push to gh-pages
mkdocs build
# ... manually copy site/ contents to gh-pages branch
```

## 🔧 Troubleshooting

### Common Issues

**Build Errors**:
- Ensure all dependencies are installed
- Check for broken links in markdown files
- Verify image paths are correct

**Styling Issues**:
- Clear browser cache
- Check CSS syntax in custom stylesheets
- Verify theme configuration in mkdocs.yml

**Deployment Issues**:
- Check GitHub Actions logs
- Verify repository settings for GitHub Pages
- Ensure gh-pages branch exists and is set as source

### Debug Mode

Enable verbose output for debugging:

```bash
mkdocs serve --verbose
mkdocs build --verbose
```

## 📚 Resources

- [MkDocs Documentation](https://www.mkdocs.org/)
- [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/)
- [PyMdown Extensions](https://facelessuser.github.io/pymdown-extensions/)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)

## 🤝 Contributing

To contribute to the documentation:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test locally with `mkdocs serve`
5. Submit a pull request

For major changes, please open an issue first to discuss the proposed changes.

---

Built with ❤️ using MkDocs Material, inspired by Anthropic's beautiful documentation design.