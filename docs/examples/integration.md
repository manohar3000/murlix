# Integration Examples

Examples of integrating Murlix with development tools, IDEs, and workflows.

## IDE Integration

### VS Code Integration

```json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Ask Murlix",
            "type": "shell",
            "command": "uv run murlix -q '${input:query}'",
            "group": "build"
        }
    ]
}
```

### Vim Integration

```vim
function! AskMurlix()
    let query = input('Ask Murlix: ')
    if !empty(query)
        execute '!uv run murlix -q "' . query . '"'
    endif
endfunction

command! Murlix call AskMurlix()
```

## Git Integration

### Pre-commit Hook

```bash
#!/bin/bash
# .git/hooks/pre-commit
changed_files=$(git diff --cached --name-only)
if [[ $changed_files == *.py ]]; then
    git diff --cached | uv run murlix -q "Review this code diff:"
fi
```

## Workflow Automation

### Daily Standup

```bash
#!/bin/bash
git_activity=$(git log --since="yesterday" --oneline)
uv run murlix -q "Generate a standup report from: $git_activity"
```

### Code Review

```bash
#!/bin/bash
diff_content=$(git diff main...HEAD)
uv run murlix -q "Review this code diff: $diff_content"
```

*More integration examples coming soon...*