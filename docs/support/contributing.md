# Contributing

We welcome contributions to Murlix! This guide explains how to contribute to the project.

## Getting Started

### Development Setup

1. **Fork the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/murlix.git
   cd murlix
   ```

2. **Install in development mode**
   ```bash
   uv sync --dev
   ```

3. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Types of Contributions

### Code Contributions
- Bug fixes
- New features
- Performance improvements
- Code refactoring

### Documentation
- Improve existing documentation
- Add new guides and examples
- Fix typos and errors

### Testing
- Add unit tests
- Improve test coverage
- Integration tests

## Contribution Process

1. **Create an issue** (for major changes)
2. **Fork and clone** the repository
3. **Create a feature branch**
4. **Make your changes** with tests and documentation
5. **Run tests** and ensure they pass
6. **Submit a pull request**

## Code Style

- Follow Python PEP 8 style guidelines
- Use type hints for function signatures
- Add docstrings for all public functions
- Write clear commit messages

## Testing

```bash
# Run tests
uv run pytest

# Run with coverage
uv run pytest --cov=murlix
```

## Documentation

```bash
# Build documentation locally
python setup-docs.py
```

## Pull Request Guidelines

- Clear description of changes
- Reference related issues
- Include tests for new features
- Update documentation as needed

## Community Guidelines

- Be respectful and inclusive
- Help others learn and contribute
- Follow the code of conduct
- Ask questions in discussions

*More detailed contributing guidelines coming soon...*