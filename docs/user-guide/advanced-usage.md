# Advanced Usage

Unlock the full potential of Murlix with advanced features, power-user techniques, and expert workflows that go beyond basic chat interactions.

## Power User Features

### Environment Variable Overrides

Customize Murlix behavior on-the-fly:

```bash
# Temporary API key override
GOOGLE_API_KEY=temp_key uv run murlix

# Debug mode for troubleshooting
LOG_LEVEL=DEBUG uv run murlix

# Custom database location
DATABASE_PATH=/tmp/test_murlix.db uv run murlix

# Multiple overrides
USER_ID=test LOG_LEVEL=DEBUG uv run murlix -q "Test query"
```

### Command Line Scripting

Automate Murlix interactions:

```bash
#!/bin/bash
# batch-queries.sh - Process multiple queries

queries=(
    "Explain Python decorators"
    "Show me async/await examples"
    "What are Python context managers?"
)

for query in "${queries[@]}"; do
    echo "Processing: $query"
    uv run murlix -q "$query" > "output_$(date +%s).txt"
    sleep 1  # Rate limiting
done
```

### Advanced Session Workflows

#### Project-Based Session Management

```bash
# Create project-specific session naming
start_project_session() {
    local project_name=$1
    uv run murlix -q "Starting work on project: $project_name. This session will focus on development tasks related to this project."
}

# Usage
start_project_session "e-commerce-api"
```

#### Session Templates

```bash
# Create session templates for different use cases
create_learning_session() {
    local topic=$1
    uv run murlix -q "I want to learn about $topic. Please provide a structured learning path with examples and practical exercises."
}

create_debugging_session() {
    local issue=$1
    uv run murlix -q "I'm debugging an issue: $issue. Please help me systematically troubleshoot this problem."
}
```

## Integration Patterns

### IDE Integration

#### VS Code Integration

Create custom VS Code tasks:

```json
// .vscode/tasks.json
{
    "version": "2.0.0",
    "tasks": [
        {
            "label": "Ask Murlix",
            "type": "shell",
            "command": "uv run murlix -q '${input:query}'",
            "group": "build",
            "presentation": {
                "echo": true,
                "reveal": "always",
                "focus": false,
                "panel": "new"
            }
        }
    ],
    "inputs": [
        {
            "id": "query",
            "description": "What do you want to ask Murlix?",
            "type": "promptString"
        }
    ]
}
```

#### Vim Integration

Add Vim commands:

```vim
" ~/.vimrc
" Send selected text to Murlix
function! AskMurlix()
    let query = input('Ask Murlix: ')
    if !empty(query)
        execute '!uv run murlix -q "' . query . '"'
    endif
endfunction

command! Murlix call AskMurlix()
nnoremap <leader>m :Murlix<CR>
```

### Git Hooks Integration

#### Pre-commit Analysis

```bash
#!/bin/bash
# .git/hooks/pre-commit
# Analyze commit with Murlix

changed_files=$(git diff --cached --name-only --diff-filter=ACM)

if [[ $changed_files == *.py ]]; then
    echo "Analyzing Python changes with Murlix..."
    git diff --cached | uv run murlix -q "Review this code diff for potential issues, improvements, and best practices:"
fi
```

### CI/CD Integration

#### GitHub Actions Integration

```yaml
name: Code Review with Murlix
on:
  pull_request:
    types: [opened, synchronize]

jobs:
  murlix-review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.13'
      
      - name: Install Murlix
        run: |
          pip install uv
          # Install your Murlix setup here
      
      - name: Analyze Changes
        run: |
          git diff origin/main...HEAD > changes.diff
          uv run murlix -q "Review this code diff: $(cat changes.diff)"
        env:
          GOOGLE_API_KEY: ${{ secrets.GOOGLE_API_KEY }}
```

## Performance Optimization

### Response Caching

Implement response caching for repeated queries:

```bash
#!/bin/bash
# cached-murlix.sh - Cache responses for common queries

cache_dir="$HOME/.murlix_cache"
mkdir -p "$cache_dir"

query="$1"
cache_key=$(echo "$query" | md5sum | cut -d' ' -f1)
cache_file="$cache_dir/$cache_key"

if [[ -f "$cache_file" && $(find "$cache_file" -mtime -1) ]]; then
    echo "Cached response:"
    cat "$cache_file"
else
    echo "Fetching new response..."
    uv run murlix -q "$query" | tee "$cache_file"
fi
```

### Parallel Processing

Process multiple queries in parallel:

```bash
#!/bin/bash
# parallel-queries.sh

queries=(
    "Explain REST API design principles"
    "Show me Python testing best practices"  
    "What are microservices patterns?"
)

# Process queries in parallel
for query in "${queries[@]}"; do
    (
        echo "Processing: $query"
        uv run murlix -q "$query" > "result_$(echo "$query" | tr ' ' '_').txt"
    ) &
done

# Wait for all background jobs
wait
echo "All queries completed!"
```

### Resource Management

Monitor and limit resource usage:

```bash
#!/bin/bash
# resource-limited-murlix.sh

# Limit memory usage
ulimit -m 512000  # 512MB

# Limit execution time  
timeout 30s uv run murlix -q "$1"

# Check exit status
if [ $? -eq 124 ]; then
    echo "Query timed out after 30 seconds"
fi
```

## Advanced Configuration

### Dynamic Configuration

Load configuration from multiple sources:

```python
# config_loader.py
import os
import json
from pathlib import Path

def load_dynamic_config():
    """Load configuration from multiple sources in priority order."""
    config = {}
    
    # 1. Default configuration
    config.update({
        'model': 'gemini-2.0-flash',
        'timeout': 30,
        'max_history': 100
    })
    
    # 2. Global config file
    global_config = Path.home() / '.murlix' / 'config.json'
    if global_config.exists():
        with open(global_config) as f:
            config.update(json.load(f))
    
    # 3. Project-specific config
    project_config = Path.cwd() / '.murlix.json'
    if project_config.exists():
        with open(project_config) as f:
            config.update(json.load(f))
    
    # 4. Environment variables (highest priority)
    if os.getenv('MURLIX_MODEL'):
        config['model'] = os.getenv('MURLIX_MODEL')
    if os.getenv('MURLIX_TIMEOUT'):
        config['timeout'] = int(os.getenv('MURLIX_TIMEOUT'))
    
    return config
```

### Custom Logging

Implement advanced logging:

```python
# custom_logger.py
import logging
import json
from datetime import datetime

class MurlixJSONFormatter(logging.Formatter):
    def format(self, record):
        log_entry = {
            'timestamp': datetime.utcnow().isoformat(),
            'level': record.levelname,
            'message': record.getMessage(),
            'module': record.module,
            'function': record.funcName,
            'line': record.lineno
        }
        return json.dumps(log_entry)

# Setup structured logging
def setup_advanced_logging():
    logger = logging.getLogger('murlix')
    handler = logging.FileHandler('murlix_structured.log')
    handler.setFormatter(MurlixJSONFormatter())
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger
```

## Workflow Automation

### Daily Standup Automation

```bash
#!/bin/bash
# daily-standup.sh - Generate daily standup using Murlix

echo "Generating daily standup report..."

# Get git activity
git_activity=$(git log --since="yesterday" --oneline --author="$(git config user.name)")

# Get calendar for today
today_tasks="Review code, Team meeting at 2 PM, Deploy feature X"

# Generate standup with Murlix
uv run murlix -q "Based on this git activity: '$git_activity' and today's tasks: '$today_tasks', generate a professional daily standup report covering what I did yesterday, what I'm doing today, and any blockers."
```

### Code Review Automation

```bash
#!/bin/bash
# automated-review.sh

# Get the diff for current branch
diff_content=$(git diff main...HEAD)

# Analyze with Murlix
uv run murlix -q "Please review this code diff and provide feedback on:
1. Code quality and best practices
2. Potential bugs or issues
3. Performance considerations
4. Security concerns
5. Suggestions for improvement

Diff:
$diff_content"
```

### Documentation Generation

```bash
#!/bin/bash
# doc-generator.sh - Generate documentation for code

file_path="$1"
if [[ ! -f "$file_path" ]]; then
    echo "Usage: $0 <file_path>"
    exit 1
fi

file_content=$(cat "$file_path")

uv run murlix -q "Generate comprehensive documentation for this code including:
- Overview and purpose
- Function/class descriptions
- Parameter documentation
- Usage examples
- Return value descriptions

Code:
$file_content" > "${file_path%.py}_docs.md"

echo "Documentation generated: ${file_path%.py}_docs.md"
```

## Monitoring and Analytics

### Usage Analytics

Track your Murlix usage patterns:

```bash
#!/bin/bash
# murlix-analytics.sh

log_file="$HOME/.murlix/usage.log"
mkdir -p "$(dirname "$log_file")"

# Log query
echo "$(date -u +%Y-%m-%dT%H:%M:%SZ),query,\"$1\"" >> "$log_file"

# Run Murlix
uv run murlix -q "$1"

# Generate weekly report
if [[ "$2" == "--report" ]]; then
    echo "Weekly Murlix Usage Report:"
    echo "=========================="
    
    # Count queries this week
    week_start=$(date -d "last monday" +%Y-%m-%d)
    query_count=$(grep "^$week_start" "$log_file" | wc -l)
    echo "Queries this week: $query_count"
    
    # Most common query patterns
    echo "Top query topics:"
    grep "query" "$log_file" | cut -d'"' -f2 | head -20 | \
    uv run murlix -q "Analyze these queries and identify the top 5 topics I ask about most: $(cat)"
fi
```

### Performance Monitoring

```bash
#!/bin/bash
# performance-monitor.sh

start_time=$(date +%s.%N)

# Run Murlix with monitoring
uv run murlix -q "$1"

end_time=$(date +%s.%N)
duration=$(echo "$end_time - $start_time" | bc)

echo "Query completed in ${duration}s"

# Log performance data
echo "$(date -u +%Y-%m-%dT%H:%M:%SZ),$duration,\"$1\"" >> ~/.murlix/performance.log

# Alert on slow queries
if (( $(echo "$duration > 10.0" | bc -l) )); then
    echo "⚠️  Slow query detected (${duration}s)"
fi
```

## Security Considerations

### Secure API Key Management

```bash
#!/bin/bash
# secure-key-manager.sh

# Use system keyring for API key storage
store_api_key() {
    echo "Storing API key securely..."
    echo "$1" | secret-tool store --label="Murlix API Key" service murlix username api
}

get_api_key() {
    secret-tool lookup service murlix username api
}

# Use in Murlix
export GOOGLE_API_KEY=$(get_api_key)
uv run murlix -q "$1"
```

### Query Sanitization

```bash
#!/bin/bash
# sanitized-murlix.sh

sanitize_query() {
    local query="$1"
    
    # Remove potential sensitive patterns
    query=$(echo "$query" | sed 's/password[[:space:]]*=[[:space:]]*[^[:space:]]*/password=****/gi')
    query=$(echo "$query" | sed 's/token[[:space:]]*=[[:space:]]*[^[:space:]]*/token=****/gi')
    query=$(echo "$query" | sed 's/key[[:space:]]*=[[:space:]]*[^[:space:]]*/key=****/gi')
    
    echo "$query"
}

# Sanitize and run
sanitized_query=$(sanitize_query "$1")
uv run murlix -q "$sanitized_query"
```

## Troubleshooting Advanced Usage

### Debug Mode

Enable comprehensive debugging:

```bash
#!/bin/bash
# debug-murlix.sh

export LOG_LEVEL=DEBUG
export PYTHONPATH="$PWD/src:$PYTHONPATH"

# Run with detailed tracing
python -m trace --trace -m murlix -q "$1" 2>&1 | tee debug.log

# Analyze debug output
echo "Debug analysis:"
grep -E "(ERROR|WARNING|Exception)" debug.log
```

### Performance Profiling

```bash
#!/bin/bash
# profile-murlix.sh

# Profile memory usage
/usr/bin/time -v uv run murlix -q "$1" 2>&1 | grep -E "(Maximum resident|User time|System time)"

# Profile with Python profiler
python -m cProfile -o murlix_profile.stats -m murlix -q "$1"

# Analyze profile
python -c "
import pstats
p = pstats.Stats('murlix_profile.stats')
p.sort_stats('cumulative').print_stats(10)
"
```

## Next Steps

- **[Custom Commands](../developer-guide/custom-commands.md)**: Create your own slash commands
- **[Architecture](../developer-guide/architecture.md)**: Understand Murlix internals
- **[Extending Murlix](../developer-guide/extending.md)**: Add new functionality

!!! success "Advanced Mastery"
    With these advanced techniques, you can integrate Murlix deeply into your development workflow, automate repetitive tasks, and create powerful AI-assisted development environments.