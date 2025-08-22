# Troubleshooting

Common issues and solutions for Murlix installation, configuration, and usage.

## Installation Issues

### Python Version Errors
**Problem**: `python: command not found` or version < 3.13

**Solution**:
```bash
# Install Python 3.13+ using pyenv
curl https://pyenv.run | bash
pyenv install 3.13.0
pyenv global 3.13.0
```

### UV Installation Issues
**Problem**: `uv: command not found`

**Solution**:
```bash
# Install UV
curl -LsSf https://astral.sh/uv/install.sh | sh
source ~/.bashrc
```

## Configuration Issues

### API Authentication Errors
**Problem**: `Authentication failed` or `API key invalid`

**Solutions**:
1. Verify API key in `.env` file
2. Check API key format (should be ~40 characters)
3. Ensure API is enabled in Google Cloud Console

### Database Permission Errors
**Problem**: Cannot create or access database

**Solutions**:
```bash
# Check directory permissions
ls -la $(dirname my_agent_data.db)

# Fix permissions
chmod 755 $(dirname my_agent_data.db)
```

## Runtime Issues

### Display Problems
**Problem**: Formatting broken, boxes not displaying

**Solutions**:
- Use modern terminal with Unicode support
- Check terminal size (minimum 80x24)
- Update terminal software

### Performance Issues
**Problem**: Slow responses or high resource usage

**Solutions**:
- Check internet connection
- Verify API quotas
- Reduce conversation history length

## Getting Help

1. Check logs in `~/.murlix/logs/`
2. Search [GitHub Issues](https://github.com/manohar3000/murlix/issues)
3. Create new issue with error details
4. Join community discussions

*More troubleshooting guides coming soon...*