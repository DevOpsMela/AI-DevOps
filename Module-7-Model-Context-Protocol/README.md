````markdown
# Module 7 - MCP Server for Executing Terminal Commands

## Agenda

- Model Context Protocol – Introduction ​
- MCP Workflow – Explained​
- DEMO – Setting UP 1st MCP Server Locally

## What is MCP?

**MCP (Model Context Protocol)** is a protocol that enables AI models to interact with external tools and retrieve information. MCP servers can:

- ✅ Store data (files, API responses, databases, etc.)
- ✅ Execute tools (functions the AI can call)
- ✅ Use prompts (predefined templates for specific tasks)

In this tutorial, we'll build an MCP server that executes terminal commands and returns the output.

---

# Installing Claude Desktop

**Claude Desktop** is a desktop application (macOS/Windows) developed by Anthropic that allows Claude to interact with local tools using MCP.

> **Claude Desktop = ChatGPT-like application + Local Tool Execution (via MCP)**

### Installation

Download and install Claude Desktop from Anthropic's website.

### macOS

- Drag the application into the **Applications** folder.

### Windows

- Run the installer and follow the installation wizard.

After installation:

1. Launch Claude Desktop.
2. Sign in with your account.

---

# Setting Up Python and Required Tools

## Prerequisites

- Python **3.10 or later**
- **uv** (Fast Python package manager)

---

## Step 1: Install uv

### macOS / Linux

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Windows

Follow the installation instructions from the official **uv** documentation.

> **Note:** Restart your terminal after installation so the `uv` command is available.

---

## Step 2: Create the MCP Directory Structure

Create a dedicated workspace for your MCP servers.

```bash
mkdir -p ~/AI/mcp/servers/terminal_server
mkdir -p ~/AI/mcp/workspace
cd ~/AI/mcp/servers/
```

### Directory Structure

```
AI/
└── mcp/
    ├── servers/
    │   └── terminal_server/
    └── workspace/
```

| Directory | Purpose |
|-----------|---------|
| `servers/` | Stores all MCP servers |
| `workspace/` | Workspace where terminal commands will execute |

---

## Step 3: Initialize a Python Project

```bash
uv init
```

---

## Step 4: Create a Virtual Environment

```bash
uv venv
```

### Activate the Environment

#### macOS / Linux

```bash
source .venv/bin/activate
```

#### Windows

```powershell
.venv\Scripts\activate
```

---

## Step 5: Install Required Packages

Install the MCP SDK:

```bash
uv pip install "mcp[cli]"
```

Install Flask (optional for future enhancements):

```bash
uv pip install flask
```

These packages allow the MCP server to communicate with Claude Desktop.

---

# Building the MCP Server

We'll use the following Python modules:

| Module | Purpose |
|---------|---------|
| `os` | Handle file paths |
| `subprocess` | Execute shell commands |
| `FastMCP` | Build MCP servers easily |

---

## Step 1: Create the Server File

Create a new file:

```bash
touch terminal_server.py
```

---

## Step 2: Add the Server Code

```python
import os
import subprocess
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("terminal")

DEFAULT_WORKSPACE = os.path.expanduser(
    "/Users/devopsmela/Desktop/AI/mcp/workspace/"
)

@mcp.tool()
async def run_command(command: str) -> str:
    """
    Run a terminal command inside the workspace directory.

    If a terminal command can accomplish a task,
    tell the user you'll use this tool to accomplish it,
    even though you cannot directly do it.

    Args:
        command: Shell command to execute.

    Returns:
        Command output or an error message.
    """

    try:
        result = subprocess.run(
            command,
            shell=True,
            cwd=DEFAULT_WORKSPACE,
            capture_output=True,
            text=True,
        )

        return result.stdout or result.stderr

    except Exception as e:
        return str(e)


if __name__ == "__main__":
    mcp.run(transport="stdio")
```

---

## Step 3: Run the MCP Server

```bash
uv run terminal_server.py
```

If everything is configured correctly, the server will start and wait for requests from Claude.

---

# Connecting the MCP Server to Claude Desktop

Open the Claude Desktop configuration file.

### macOS

```bash
code ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

Add the following configuration:

```json
{
  "mcpServers": {
    "terminal": {
      "command": "/opt/homebrew/bin/uv",
      "args": [
        "--directory",
        "/Users/devopsmela/Desktop/AI/mcp/servers/",
        "run",
        "terminal_server.py"
      ]
    }
  }
}
```

> Update the directory path if your project is located elsewhere.

Save the file and restart **Claude Desktop**.

If configured correctly, a **🔨 Hammer** icon will appear, indicating the MCP server is available.

---

# Verifying the MCP Server with MCP Inspector

Use the MCP Inspector to verify your server.

```bash
npx @modelcontextprotocol/inspector python3 terminal_server.py
```

The inspector allows you to:

- View available tools
- Execute tool functions
- Inspect request/response payloads
- Debug MCP communication

---

# Testing the MCP Server

Once Claude Desktop is running, try the following prompts.

## Example 1

> Run the command `ls` in my workspace using the terminal MCP workspace.

---

## Example 2

> Create a file named `terminal-test.txt` and write:

```text
Welcome to my first MCP Server...
```

using the terminal MCP workspace.

---

# Checking MCP Logs

If the MCP server is not responding, inspect the logs.

```bash
tail -50 ~/Library/Logs/Claude/mcp-server-terminal.log
```

These logs can help identify:

- Startup failures
- Python exceptions
- Invalid configuration
- Communication issues with Claude Desktop

---

# Project Workflow

```text
User Prompt
      │
      ▼
Claude Desktop
      │
      ▼
MCP Server (terminal_server.py)
      │
      ▼
subprocess.run()
      │
      ▼
Terminal Command
      │
      ▼
Command Output
      │
      ▼
Claude Desktop
      │
      ▼
User
```

---

# Summary

1. Install Claude Desktop.
2. Install Python and `uv`.
3. Create the MCP project structure.
4. Initialize a Python project.
5. Create a virtual environment.
6. Install the MCP SDK.
7. Build the `terminal_server.py` MCP server.
8. Configure Claude Desktop.
9. Verify using MCP Inspector.
10. Test terminal commands through Claude.
11. Check logs if troubleshooting is required.
````
