````markdown
# CrewAI Setup Guide

## Prerequisites

Before getting started, ensure you have:

- Python **3.10 or higher**
- **uv** (a fast Python package manager)

---

# Setting Up Python and uv

## Step 1: Install uv

### macOS / Linux

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Windows

Follow the installation instructions from the official **uv** documentation.

> **Note:** Restart your terminal after installation so that `uv` is recognized.

---

## Step 2: Create a Virtual Environment

```bash
uv venv
```

### Activate the Virtual Environment

#### macOS / Linux

```bash
source .venv/bin/activate
```

#### Windows

```powershell
.venv\Scripts\activate
```

---

## Step 3: Install CrewAI

```bash
uv tool install crewai
```

---

## Step 4: Verify Installation

```bash
uv tool list
```

---

## Step 5: Update Your Shell (Optional)

If CrewAI was installed using **uv**, update your shell configuration:

```bash
uv tool update-shell
```

---

# Create Your First Crew

## Step 1: Create a New Crew

```bash
crewai create crew my-first-crew
```

---

## Step 2: Configure the LLM

### Option 1: Azure AI Foundry (Recommended & Tested)

Create a `.env` file and add:

```env
MODEL=gpt-4.1-mini
OPENAI_API_KEY=<YOUR_API_KEY>
OPENAI_API_BASE=https://devopsmela-ai-fdry.services.ai.azure.com/openai/v1
OPENAI_API_VERSION=2025-04-14
```

---

## Step 3: Project Structure

After creating the project, you'll see the following files:

| File | Purpose |
|------|---------|
| `agents.yaml` | Define AI agents and their roles |
| `tasks.yaml` | Define tasks and workflows |
| `.env` | Store API keys and environment variables |
| `main.py` | Project entry point |
| `crew.py` | Crew orchestration logic |
| `tools/` | Custom agent tools |
| `knowledge/` | Knowledge base files |

### Next Steps

- Edit **`agents.yaml`** to define your agents.
- Edit **`tasks.yaml`** to define workflows.
- Store secrets (API keys, endpoints) inside the **`.env`** file.

---

## Step 4: Install Project Dependencies

Navigate to the project directory:

```bash
cd my-first-crew
```

Install CrewAI project dependencies:

```bash
crewai install
```

---

## Step 5: Install Required Python Packages

### FastAPI

```bash
uv pip install fastapi
uv add fastapi
```

### APScheduler

```bash
uv pip install apscheduler
uv add apscheduler
```

---

## Step 6: Run Your Crew

From the project root:

```bash
crewai run
```

---

# Troubleshooting & Debugging

## Error 1

### Error Message

```text
An error occurred while running the crew:
Fallback to LiteLLM is not available
```

### Solution

```bash
uv pip install litellm
uv add litellm
```

### VS Code Interpreter

If the error persists, ensure VS Code is using the project's virtual environment.

1. Press **Command + Shift + P** (macOS) or **Ctrl + Shift + P** (Windows/Linux).
2. Select **Python: Select Interpreter**.
3. Choose your project's `.venv`.

Example:

```text
/Users/devopsmela/Desktop/CrewAI/kube-manifest-crew/kube_manifest_crew/.venv
```

---

## Error 2

### Error Message

```text
ImportError: Missing dependency
No module named 'fastapi'
```

### Solution

```bash
uv pip install fastapi
uv add fastapi
```

---

## Error 3

### Error Message

```text
ImportError: Missing dependency
No module named 'apscheduler'
```

### Solution

```bash
uv pip install apscheduler
uv add apscheduler
```

---

## Error 4

### Error Message

```text
Cache_breakpoint is unsupported
"type":"invalid_request_error"
```

### Solution

Use **Azure AI Foundry** instead of **Groq** as the LLM provider.

---

# Summary

1. Install **uv**
2. Create and activate a virtual environment
3. Install **CrewAI**
4. Create a new crew
5. Configure Azure AI Foundry
6. Install dependencies
7. Run the crew
8. Refer to the troubleshooting section if any issues occur
````
