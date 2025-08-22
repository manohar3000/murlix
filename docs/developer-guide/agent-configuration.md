# Agent Configuration

Learn how to customize and configure the AI agent in Murlix to suit your specific needs and use cases.

## Overview

The Murlix agent is configured in `src/murlix/core_agent/agent.py` using Google's Agent Development Kit (ADK).

## Basic Configuration

```python
from google_adk import LlmAgent

root_agent = LlmAgent(
    model='gemini-2.0-flash',
    name='Murlix_Assistant',
    instruction="Your custom instructions here...",
    tools=mcp_toolsets
)
```

## Model Selection

Choose from available models:
- `gemini-2.0-flash` - Fast and efficient
- `gemini-1.5-pro` - More capable reasoning
- `gemini-1.5-flash` - Balanced performance

## Custom Instructions

Tailor the agent's behavior with specific instructions for your use case.

## Tool Integration

Add custom tools to extend the agent's capabilities.

*More detailed documentation coming soon...*