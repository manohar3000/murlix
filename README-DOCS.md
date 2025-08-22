# 📚 Murlix Documentation

This repository includes a beautiful, modern documentation website built with MkDocs Material theme, inspired by Anthropic's documentation design.

## 🚀 Quick Start

### View Documentation Locally

**Easy Setup (Recommended):**
```bash
python setup-docs.py
```

**Manual Setup:**
```bash
# Create virtual environment
python -m venv docs-env

# Activate it
# Windows: docs-env\Scripts\activate
# macOS/Linux: source docs-env/bin/activate

# Install requirements
pip install -r requirements-docs.txt

# Serve documentation
mkdocs serve
```

Then visit: http://127.0.0.1:8000

### Build Documentation

```bash
# Using the setup script
python setup-docs.py
# Choose option 2 (Build documentation only)

# Or manually after activating virtual environment
mkdocs build
```

## 🎨 Features

- **Beautiful Design**: Inspired by Anthropic's documentation with modern gradients and styling
- **Responsive**: Works perfectly on desktop, tablet, and mobile
- **Dark/Light Mode**: Automatic theme switching
- **Interactive Elements**: Tabbed content, code highlighting, search functionality
- **GitHub Pages Ready**: Automatic deployment via GitHub Actions

## 📁 Documentation Structure

```
docs/
├── index.md              # Homepage with hero section
├── getting-started/      # Installation & quick start
├── user-guide/          # User documentation  
├── developer-guide/     # Developer documentation
├── api-reference/       # CLI & API reference
├── examples/            # Usage examples
├── support/             # FAQ & troubleshooting
└── stylesheets/         # Custom CSS styling
```

## 🔧 Troubleshooting

**Error: `custom_dir does not exist`**
- The `docs/overrides` directory should be created automatically
- If not, run: `mkdir -p docs/overrides`

**Error: `mkdocs command not found`**
- Make sure you've activated the virtual environment
- Or use the setup script which handles everything automatically

**Styling Issues**
- Clear your browser cache
- Try incognito/private browsing mode

## 🌐 GitHub Pages Deployment

The documentation automatically deploys to GitHub Pages when you push to the `main` branch.

### ⚠️ Important: First-Time Setup Required

**Before the workflow can run successfully, you need to enable GitHub Pages:**

1. **Go to your repository Settings**
2. **Click "Pages" in the left sidebar**
3. **Set Source to "GitHub Actions"** (not "Deploy from a branch")
4. **Save the configuration**

See `GITHUB-PAGES-SETUP.md` for detailed instructions.

### Workflow Options

- **Primary**: `.github/workflows/docs.yml` - Full-featured with Pages API
- **Fallback**: `.github/workflows/docs-simple.yml` - Works without pre-configuration

If you get "Pages not enabled" errors, try renaming `docs-simple.yml` to `docs.yml`.

## 📖 More Information

See `docs/README.md` for detailed documentation about the documentation system itself, including customization options and advanced features.

---

**Built with ❤️ using MkDocs Material**