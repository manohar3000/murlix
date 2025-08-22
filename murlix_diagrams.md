# Murlix Tool - Architecture and Flow Diagrams

This document contains various Mermaid diagrams explaining the working of the Murlix CLI chat interface tool.

## 1. High-Level Architecture Overview

```mermaid
graph TB
    subgraph "User Interface Layer"
        CLI[CLI Commands]
        UI[Rich UI Components]
        ASCII[ASCII Art & Welcome]
    end
    
    subgraph "Core Application"
        MAIN[Main Entry Point]
        CHAT[Chat Loop]
        SESSION[Session Manager]
        SLASH[Slash Commands]
    end
    
    subgraph "AI Agent Layer"
        AGENT[LLM Agent<br/>Gemini 2.0 Flash]
        TOOLS[MCP Toolsets]
        FS[Filesystem Tools]
        CTX[Context7 Tools]
        CMD[Command Runner]
    end
    
    subgraph "Persistence Layer"
        DB[(SQLite Database<br/>my_agent_data.db)]
        SESSIONS[Session Service]
    end
    
    subgraph "External Dependencies"
        GOOGLE[Google ADK]
        RICH[Rich Terminal]
        CLICK[Click CLI]
    end
    
    CLI --> MAIN
    UI --> CHAT
    ASCII --> UI
    
    MAIN --> CHAT
    MAIN --> SESSION
    CHAT --> SLASH
    CHAT --> AGENT
    
    SESSION --> SESSIONS
    SESSIONS --> DB
    
    AGENT --> TOOLS
    TOOLS --> FS
    TOOLS --> CTX
    TOOLS --> CMD
    
    MAIN -.-> GOOGLE
    UI -.-> RICH
    CLI -.-> CLICK
    
    style AGENT fill:#e1f5fe
    style DB fill:#f3e5f5
    style CLI fill:#e8f5e8
```

## 2. User Interaction Flow

```mermaid
flowchart TD
    START([User starts Murlix]) --> MODE{Choose Mode}
    
    MODE -->|Default| INTERACTIVE[Interactive Mode]
    MODE -->|--query| SINGLE[Single Query Mode]
    MODE -->|continue-chat| CONTINUE[Continue Last Session]
    MODE -->|load-chat| PICKER[Session Picker]
    
    INTERACTIVE --> WELCOME[Display Welcome Screen]
    WELCOME --> WAIT[Wait for Enter]
    WAIT --> NEW_SESSION[Create New Session]
    
    CONTINUE --> LAST{Last Session Exists?}
    LAST -->|Yes| LOAD_LAST[Load Last Session]
    LAST -->|No| NEW_SESSION
    
    PICKER --> LIST[List All Sessions]
    LIST --> SELECT[User Selects Session]
    SELECT --> LOAD_SELECTED[Load Selected Session]
    
    NEW_SESSION --> CHAT_LOOP[Enter Chat Loop]
    LOAD_LAST --> CHAT_LOOP
    LOAD_SELECTED --> CHAT_LOOP
    
    CHAT_LOOP --> INPUT[Wait for User Input]
    INPUT --> SLASH_CHECK{Starts with '/'?}
    
    SLASH_CHECK -->|Yes| SLASH_CMD[Process Slash Command]
    SLASH_CHECK -->|No| AI_PROCESS[Send to AI Agent]
    
    SLASH_CMD --> QUIT_CHECK{Is /quit?}
    QUIT_CHECK -->|Yes| END([Exit])
    QUIT_CHECK -->|No| INPUT
    
    AI_PROCESS --> RESPONSE[Display AI Response]
    RESPONSE --> INPUT
    
    SINGLE --> TODO[TODO: Implement Single Query]
    TODO --> END
    
    style START fill:#c8e6c9
    style END fill:#ffcdd2
    style CHAT_LOOP fill:#e1f5fe
```

## 3. Session Management Lifecycle

```mermaid
stateDiagram-v2
    [*] --> SessionManager: Initialize
    
    SessionManager --> CreateNew: create_session()
    SessionManager --> ListSessions: list_sessions()
    SessionManager --> LoadExisting: load_session(id)
    SessionManager --> ContinueLast: continue_latest_session()
    
    CreateNew --> DatabaseCreate: Create in DB
    DatabaseCreate --> RunnerInit: Initialize Runner
    RunnerInit --> Active: Session Active
    
    ListSessions --> DisplayTable: Show Session Table
    DisplayTable --> UserSelect: User Selection
    UserSelect --> LoadExisting: Load Selected
    UserSelect --> CreateNew: New Session
    
    LoadExisting --> DatabaseLoad: Load from DB
    DatabaseLoad --> RunnerRestore: Restore Runner
    RunnerRestore --> Active
    
    ContinueLast --> CheckExists: Check Last Session
    CheckExists --> LoadExisting: Found
    CheckExists --> CreateNew: Not Found
    
    Active --> ChatLoop: Enter Chat
    ChatLoop --> Persist: Auto-save Messages
    Persist --> ChatLoop
    
    ChatLoop --> Cleanup: /quit or Exit
    Cleanup --> [*]
    
    note right of Active
        Session contains:
        - Unique ID
        - User ID
        - App Name
        - Created/Updated timestamps
        - Conversation history
    end note
```

## 4. Chat Loop Detailed Flow

```mermaid
flowchart TD
    START_CHAT[Start Chat Loop] --> PROMPT[Display 'You: ' prompt]
    PROMPT --> INPUT[Wait for user input]
    
    INPUT --> SLASH_CHECK{Input starts with '/'?}
    
    SLASH_CHECK -->|Yes| PARSE_CMD[Parse slash command]
    PARSE_CMD --> CMD_EXISTS{Command exists?}
    
    CMD_EXISTS -->|Yes| EXECUTE_CMD[Execute command handler]
    CMD_EXISTS -->|No| UNKNOWN[Show unknown command]
    
    EXECUTE_CMD --> QUIT_CHECK{Command is /quit?}
    QUIT_CHECK -->|Yes| FAREWELL[Show farewell message]
    QUIT_CHECK -->|No| PROMPT
    
    UNKNOWN --> PROMPT
    FAREWELL --> EXIT[Exit chat loop]
    
    SLASH_CHECK -->|No| CREATE_MSG[Create Content message]
    CREATE_MSG --> SEND_AGENT[Send to AI agent via runner]
    
    SEND_AGENT --> STREAM[Stream response events]
    STREAM --> EVENT_TYPE{Event type?}
    
    EVENT_TYPE -->|Text| DISPLAY_TEXT[Display text response]
    EVENT_TYPE -->|Tool Call| DISPLAY_TOOL[Display tool execution]
    EVENT_TYPE -->|Error| DISPLAY_ERROR[Display error message]
    EVENT_TYPE -->|Other| DISPLAY_OTHER[Display other events]
    
    DISPLAY_TEXT --> MORE_EVENTS{More events?}
    DISPLAY_TOOL --> MORE_EVENTS
    DISPLAY_ERROR --> MORE_EVENTS
    DISPLAY_OTHER --> MORE_EVENTS
    
    MORE_EVENTS -->|Yes| STREAM
    MORE_EVENTS -->|No| SAVE_MSG[Auto-save to session]
    SAVE_MSG --> PROMPT
    
    INPUT -.-> KEYBOARD_INT[Keyboard Interrupt]
    KEYBOARD_INT --> GRACEFUL_EXIT[Graceful exit message]
    GRACEFUL_EXIT --> EXIT
    
    style START_CHAT fill:#e8f5e8
    style EXIT fill:#ffcdd2
    style STREAM fill:#e1f5fe
```

## 5. Slash Commands Processing

```mermaid
flowchart LR
    INPUT[User Input: /command] --> SPLIT[Split by whitespace]
    SPLIT --> EXTRACT[Extract command name]
    
    EXTRACT --> REGISTRY{Check command registry}
    
    REGISTRY -->|/help| HELP_HANDLER[Display help panel<br/>with all commands]
    REGISTRY -->|/quit| QUIT_HANDLER[Show farewell message<br/>Return quit signal]
    REGISTRY -->|/sessions| SESSION_HANDLER[List all sessions<br/>in table format]
    REGISTRY -->|/clear| CLEAR_HANDLER[Clear terminal screen]
    REGISTRY -->|/new| NEW_HANDLER[Show new session<br/>instructions]
    REGISTRY -->|Unknown| ERROR_HANDLER[Show unknown command<br/>error message]
    
    subgraph "Command Handlers"
        HELP_HANDLER
        QUIT_HANDLER
        SESSION_HANDLER
        CLEAR_HANDLER
        NEW_HANDLER
        ERROR_HANDLER
    end
    
    HELP_HANDLER --> RETURN[Return to chat loop]
    SESSION_HANDLER --> RETURN
    CLEAR_HANDLER --> RETURN
    NEW_HANDLER --> RETURN
    ERROR_HANDLER --> RETURN
    
    QUIT_HANDLER --> QUIT_SIGNAL[Signal to exit chat loop]
    
    style INPUT fill:#e8f5e8
    style QUIT_SIGNAL fill:#ffcdd2
    style REGISTRY fill:#fff3e0
```

## 6. AI Agent and Tools Integration

```mermaid
graph TB
    subgraph "User Message Flow"
        USER_MSG[User Message] --> CONTENT[Create Content Object]
        CONTENT --> RUNNER[ADK Runner]
    end
    
    subgraph "LLM Agent Configuration"
        AGENT[Gemini 2.0 Flash Agent]
        AGENT_CONFIG[Agent Configuration:<br/>- Name: HelpfulAssistant<br/>- Model: gemini-2.0-flash<br/>- Instructions & Guidelines]
        
        AGENT --> AGENT_CONFIG
    end
    
    subgraph "MCP Toolsets"
        FILESYSTEM[Filesystem MCP<br/>@modelcontextprotocol/<br/>server-filesystem]
        CONTEXT7[Context7 MCP<br/>@upstash/context7-mcp]
        COMMAND[Command Runner<br/>run_command function]
        
        FILESYSTEM --> FS_OPS[File Operations:<br/>- Read/Write files<br/>- List directories<br/>- Search files<br/>- File metadata]
        
        CONTEXT7 --> DOC_OPS[Documentation:<br/>- Package docs<br/>- Code examples<br/>- API references<br/>- Version info]
        
        COMMAND --> CMD_OPS[Command Execution:<br/>- Terminal commands<br/>- Capture output<br/>- Error handling<br/>- Process management]
    end
    
    RUNNER --> AGENT
    AGENT --> FILESYSTEM
    AGENT --> CONTEXT7
    AGENT --> COMMAND
    
    subgraph "Response Processing"
        EVENTS[Async Event Stream]
        TEXT_EVENT[Text Response Events]
        TOOL_EVENT[Tool Execution Events]
        ERROR_EVENT[Error Events]
        
        AGENT --> EVENTS
        EVENTS --> TEXT_EVENT
        EVENTS --> TOOL_EVENT
        EVENTS --> ERROR_EVENT
    end
    
    subgraph "UI Display"
        UI_HANDLER[show_agent_response]
        RICH_PANEL[Rich Panel Display]
        
        TEXT_EVENT --> UI_HANDLER
        TOOL_EVENT --> UI_HANDLER
        ERROR_EVENT --> UI_HANDLER
        UI_HANDLER --> RICH_PANEL
    end
    
    style AGENT fill:#e1f5fe
    style FILESYSTEM fill:#f3e5f5
    style CONTEXT7 fill:#f3e5f5
    style COMMAND fill:#f3e5f5
    style RICH_PANEL fill:#e8f5e8
```

## 7. Database Schema and Session Persistence

```mermaid
erDiagram
    SESSIONS {
        string session_id PK
        string app_name
        string user_id
        datetime created_at
        datetime updated_at
        string status
        json metadata
    }
    
    MESSAGES {
        string message_id PK
        string session_id FK
        string role
        text content
        datetime timestamp
        json parts
        string event_type
    }
    
    EVENTS {
        string event_id PK
        string session_id FK
        string event_type
        json event_data
        datetime timestamp
        string status
    }
    
    USERS {
        string user_id PK
        string app_name
        datetime first_seen
        datetime last_active
        json preferences
    }
    
    SESSIONS ||--o{ MESSAGES : contains
    SESSIONS ||--o{ EVENTS : generates
    USERS ||--o{ SESSIONS : owns
    
    SESSIONS {
        string "Unique identifier"
        string "Application name (cwd)"
        string "User identifier"
        datetime "Session creation time"
        datetime "Last activity time"
        string "Active/Inactive"
        json "Additional session data"
    }
    
    MESSAGES {
        string "Unique message ID"
        string "Parent session"
        string "user/assistant/system"
        text "Message content"
        datetime "When sent/received"
        json "Message parts/attachments"
        string "text/tool_call/error"
    }
```

## 8. Application Startup Sequence

```mermaid
sequenceDiagram
    participant User
    participant CLI as Click CLI
    participant Main as Main Entry
    participant Env as Environment
    participant UI as UI Components
    participant SM as Session Manager
    participant DB as SQLite Database
    participant Agent as LLM Agent
    participant Runner as ADK Runner
    
    User->>CLI: uv run murlix [command]
    CLI->>Main: Parse command & options
    Main->>Env: load_dotenv()
    Env-->>Main: Environment variables loaded
    
    alt Interactive Mode (default)
        Main->>UI: clear_screen()
        Main->>UI: display_welcome()
        UI->>User: Show ASCII art & welcome
        User->>Main: Press Enter
        Main->>UI: clear_screen()
        Main->>UI: show_ready_message()
        
        Main->>SM: SessionManager()
        SM->>DB: Initialize database connection
        DB-->>SM: Connection established
        
        Main->>SM: create_session()
        SM->>DB: INSERT new session
        DB-->>SM: Session ID returned
        SM->>Runner: Initialize with agent
        Runner->>Agent: Load LLM agent config
        Agent-->>Runner: Agent ready
        Runner-->>SM: Runner initialized
        SM-->>Main: (runner, session_id)
        
        Main->>Main: run_chat_loop(runner, sm, session_id)
        
    else Continue Chat
        Main->>SM: SessionManager()
        SM->>DB: Initialize database connection
        Main->>SM: continue_latest_session()
        SM->>DB: SELECT latest session
        alt Session exists
            DB-->>SM: Session data
            SM->>Runner: Restore runner with session
            Runner-->>SM: Runner restored
            SM-->>Main: Start chat with existing session
        else No session
            SM->>SM: create_session()
            Note over SM: Falls back to new session
        end
        
    else Load Chat
        Main->>SM: SessionManager()
        Main->>SM: list_sessions()
        SM->>DB: SELECT all user sessions
        DB-->>SM: Session list
        SM->>UI: Display session table
        UI->>User: Show session picker
        User->>SM: Select session index
        SM->>SM: load_session(selected_id)
        SM->>Runner: Restore with selected session
        Runner-->>SM: Runner restored
        SM-->>Main: Start chat with selected session
    end
    
    Note over User,Runner: Chat loop begins...
```

## 9. Component Interaction Network

```mermaid
graph LR
    subgraph "Entry Points"
        MAIN_CLI[murlix]
        CONTINUE_CLI[murlix continue-chat]
        LOAD_CLI[murlix load-chat]
        QUERY_CLI[murlix --query]
    end
    
    subgraph "Core Modules"
        INIT[__init__.py]
        CHAT[chat.py]
        SESSION[session.py]
        SLASH[slash_commands.py]
        UI[ui.py]
    end
    
    subgraph "Agent System"
        AGENT_MOD[core_agent/agent.py]
        RUNNER[ADK Runner]
        LLM[Gemini 2.0 Flash]
    end
    
    subgraph "Utilities"
        CONSOLE[utils/console.py]
        HELPER[utils/helper.py]
        SUPPRESS[utils/supress_warnings.py]
    end
    
    subgraph "External Systems"
        MCP_FS[MCP Filesystem]
        MCP_CTX[MCP Context7]
        SQLITE[SQLite DB]
        RICH_LIB[Rich Library]
        CLICK_LIB[Click Library]
    end
    
    MAIN_CLI --> INIT
    CONTINUE_CLI --> INIT
    LOAD_CLI --> INIT
    QUERY_CLI --> INIT
    
    INIT --> CHAT
    INIT --> SESSION
    INIT --> UI
    
    CHAT --> SLASH
    CHAT --> AGENT_MOD
    CHAT --> SESSION
    
    SESSION --> SQLITE
    SLASH --> UI
    UI --> CONSOLE
    
    AGENT_MOD --> RUNNER
    RUNNER --> LLM
    AGENT_MOD --> MCP_FS
    AGENT_MOD --> MCP_CTX
    
    CONSOLE --> RICH_LIB
    INIT --> CLICK_LIB
    HELPER --> CONSOLE
    
    style INIT fill:#e1f5fe
    style CHAT fill:#e8f5e8
    style SESSION fill:#f3e5f5
    style AGENT_MOD fill:#fff3e0
```

## 10. Error Handling and Recovery Flow

```mermaid
flowchart TD
    START[Application Start] --> TRY_INIT[Try Initialize]
    TRY_INIT --> INIT_ERROR{Initialization Error?}
    
    INIT_ERROR -->|No| NORMAL_FLOW[Normal Operation]
    INIT_ERROR -->|Yes| HANDLE_INIT[Handle Init Error]
    
    HANDLE_INIT --> LOG_ERROR[Log error message]
    LOG_ERROR --> GRACEFUL_EXIT[Graceful exit with error code]
    
    NORMAL_FLOW --> CHAT_LOOP[Chat Loop Running]
    CHAT_LOOP --> USER_INPUT[Wait for Input]
    
    USER_INPUT --> KEYBOARD_INT{Keyboard Interrupt?}
    KEYBOARD_INT -->|Yes| SAVE_SESSION[Save current session]
    SAVE_SESSION --> GOODBYE_MSG[Show goodbye message]
    GOODBYE_MSG --> CLEAN_EXIT[Clean exit]
    
    KEYBOARD_INT -->|No| PROCESS_INPUT[Process Input]
    PROCESS_INPUT --> INPUT_ERROR{Processing Error?}
    
    INPUT_ERROR -->|No| DISPLAY_RESPONSE[Display Response]
    INPUT_ERROR -->|Yes| HANDLE_INPUT_ERROR[Handle Input Error]
    
    HANDLE_INPUT_ERROR --> SHOW_ERROR[Show error to user]
    SHOW_ERROR --> CONTINUE_CHAT{Continue chat?}
    CONTINUE_CHAT -->|Yes| USER_INPUT
    CONTINUE_CHAT -->|No| SAVE_SESSION
    
    DISPLAY_RESPONSE --> RESPONSE_ERROR{Response Error?}
    RESPONSE_ERROR -->|No| USER_INPUT
    RESPONSE_ERROR -->|Yes| HANDLE_RESPONSE_ERROR[Handle Response Error]
    
    HANDLE_RESPONSE_ERROR --> SHOW_RESPONSE_ERROR[Show response error]
    SHOW_RESPONSE_ERROR --> USER_INPUT
    
    subgraph "Error Types"
        DB_ERROR[Database Connection Error]
        AGENT_ERROR[AI Agent Error]
        NETWORK_ERROR[Network/API Error]
        FILE_ERROR[File System Error]
        TOOL_ERROR[MCP Tool Error]
    end
    
    HANDLE_INIT -.-> DB_ERROR
    HANDLE_INPUT_ERROR -.-> AGENT_ERROR
    HANDLE_INPUT_ERROR -.-> NETWORK_ERROR
    HANDLE_RESPONSE_ERROR -.-> FILE_ERROR
    HANDLE_RESPONSE_ERROR -.-> TOOL_ERROR
    
    style START fill:#c8e6c9
    style CLEAN_EXIT fill:#c8e6c9
    style GRACEFUL_EXIT fill:#ffcdd2
    style HANDLE_INIT fill:#ffecb3
    style HANDLE_INPUT_ERROR fill:#ffecb3
    style HANDLE_RESPONSE_ERROR fill:#ffecb3
```

## 11. Configuration and Environment Setup

```mermaid
graph TB
    subgraph "Environment Configuration"
        ENV_FILE[.env file]
        ENV_VARS[Environment Variables]
        DEFAULTS[Default Values]
    end
    
    subgraph "Configuration Options"
        USER_ID[USER_ID<br/>default: "default_user"]
        GOOGLE_API[GOOGLE_API_KEY<br/>for Google AI API]
        VERTEX_PROJECT[VERTEX_AI_PROJECT<br/>for Vertex AI]
        VERTEX_LOCATION[VERTEX_AI_LOCATION<br/>for Vertex AI]
    end
    
    subgraph "Agent Configuration"
        MODEL[Model: gemini-2.0-flash]
        NAME[Name: HelpfulAssistant]
        INSTRUCTIONS[System Instructions]
        TOOLS_CONFIG[MCP Tools Configuration]
    end
    
    subgraph "Database Configuration"
        DB_URL[Database URL<br/>sqlite:///./my_agent_data.db]
        APP_NAME[App Name<br/>from current directory]
        SCHEMA[Auto-created schema]
    end
    
    subgraph "MCP Tools Setup"
        FS_TOOL[Filesystem Tool<br/>@modelcontextprotocol/server-filesystem]
        CTX_TOOL[Context7 Tool<br/>@upstash/context7-mcp]
        CMD_TOOL[Command Runner<br/>Custom function]
        
        ALLOWED_PATH[Allowed Path<br/>Current working directory]
    end
    
    ENV_FILE --> ENV_VARS
    ENV_VARS --> USER_ID
    ENV_VARS --> GOOGLE_API
    ENV_VARS --> VERTEX_PROJECT
    ENV_VARS --> VERTEX_LOCATION
    
    DEFAULTS --> USER_ID
    
    USER_ID --> DB_URL
    APP_NAME --> DB_URL
    DB_URL --> SCHEMA
    
    MODEL --> AGENT_CONFIG[Agent Instance]
    NAME --> AGENT_CONFIG
    INSTRUCTIONS --> AGENT_CONFIG
    TOOLS_CONFIG --> AGENT_CONFIG
    
    FS_TOOL --> TOOLS_CONFIG
    CTX_TOOL --> TOOLS_CONFIG
    CMD_TOOL --> TOOLS_CONFIG
    
    ALLOWED_PATH --> FS_TOOL
    ALLOWED_PATH --> CMD_TOOL
    
    style ENV_FILE fill:#e8f5e8
    style AGENT_CONFIG fill:#e1f5fe
    style SCHEMA fill:#f3e5f5
    style ALLOWED_PATH fill:#ffecb3
```

## Summary

These diagrams provide a comprehensive overview of the Murlix tool's architecture and operation:

1. **Architecture Overview** - Shows the layered structure and component relationships
2. **User Interaction Flow** - Illustrates different ways users can interact with the tool
3. **Session Management** - Details the lifecycle of chat sessions and persistence
4. **Chat Loop Flow** - Explains the core conversation handling logic
5. **Slash Commands** - Shows how built-in commands are processed
6. **AI Agent Integration** - Demonstrates the integration with Google ADK and MCP tools
7. **Database Schema** - Details the data model for session persistence
8. **Startup Sequence** - Shows the initialization process for different modes
9. **Component Network** - Illustrates module dependencies and interactions
10. **Error Handling** - Shows error recovery and graceful degradation
11. **Configuration** - Details environment setup and configuration options

Murlix is a well-architected CLI tool that provides a beautiful interface for AI chat interactions with robust session management, extensible command system, and powerful tool integration through the Model Context Protocol (MCP).