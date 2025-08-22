# Session API

API reference for Murlix's session management system.

## SessionManager Class

The main interface for session operations.

### Methods

#### `create_session()`
Create a new chat session.

#### `load_session(session_id)`
Load an existing session by ID.

#### `list_sessions()`
List all available sessions.

#### `continue_latest_session()`
Continue the most recent session.

## Session Data Model

### Session Object
- `id`: Unique session identifier
- `user_id`: User identifier
- `created_at`: Session creation timestamp
- `last_activity`: Last interaction timestamp
- `status`: Session status

### Message Object
- `id`: Message identifier
- `session_id`: Associated session
- `role`: Message role (user/assistant)
- `content`: Message content
- `timestamp`: Message timestamp

*Detailed API documentation coming soon...*