# Custom Agents

Examples of customizing the Murlix AI agent for specific use cases and workflows.

## Agent Customization

### Development-Focused Agent

```python
root_agent = LlmAgent(
    model='gemini-2.0-flash',
    name='DevAssistant',
    instruction="""
    You are a senior software engineer and mentor. Focus on:
    - Code quality and best practices
    - Architecture and design patterns  
    - Performance optimization
    - Security considerations
    
    Always provide code examples and explain your reasoning.
    """
)
```

### Research Assistant Agent

```python
root_agent = LlmAgent(
    model='gemini-1.5-pro',
    name='ResearchBot',
    instruction="""
    You are a research assistant specializing in:
    - Literature reviews and citations
    - Data analysis and interpretation
    - Methodology suggestions
    - Academic writing support
    
    Be thorough and suggest follow-up research.
    """
)
```

## Agent Tools

### Adding Custom Tools

```python
def get_weather(location: str) -> str:
    """Get weather information for a location."""
    # Implementation here
    return f"Weather in {location}: Sunny, 72°F"

custom_tools = [
    Tool(
        name="get_weather",
        description="Get current weather",
        handler=get_weather
    )
]

root_agent = LlmAgent(
    model='gemini-2.0-flash',
    tools=mcp_toolsets + custom_tools
)
```

*More examples coming soon...*