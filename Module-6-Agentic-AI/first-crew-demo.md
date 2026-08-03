#### CREWAI SETUP \####\
\
�� Setting Up Python and the Right Tools\
\
We need Python 3.10 or higher and a tool called uv, which is a fast
package manager for Python.\
\
Step 1: Install uv\
�� Mac/Linux:\
\
curl -LsSf https://astral.sh/uv/install.sh \| sh\
�� Windows: Follow the instructions at uv's installation page.\
\
After installation, restart your terminal so uv is recognized.\
\
Step 2: Set Up a Virtual Environment\
uv venv\
source .venv/bin/activate \# Mac/Linux\
or\
.venv\\Scripts\\activate \# Windows\
\
Step 3: Install CREWAI\
uv tool install crewai\
\
Step 4: Verify Installation\
uv tool list\
\
Step 5: Update shell (if CREWAI install using UV)\
uv tool update-shell\
\
\#### Create 1st CREW \####\
\
Step 1: crewai create crew my-first-crew\
\
Step1.2: Alternatively try Azure Foundry (Tested - Working)\
\
MODEL=gpt-4.1-mini\
OPENAI_API_KEY=\
OPENAI_API_BASE=https://devopsmela-ai-fdry.services.ai.azure.com/openai/v1\
OPENAI_API_VERSION=2025-04-14\
\
Step 2: Project contains esstential files\

  ------------- ------------------------------------------
  File          Purpose
  agents.yaml   Define your AI agents and their roles
  tasks.yaml    Set up agent tasks and workflows
  .env          Store API keys and environment variables
  main.py       Project entry point and execution flow
  crew.py       Crew orchestration and coordination
  tools/        Directory for custom agent tools
  knowledge/    Directory for knowledge base
  ------------- ------------------------------------------

-   Start by editing agents.yaml and tasks.yaml to define your crew's
    behavior.

-   Keep sensitive information like API keys in .env.\
    \
    Step 3: Before you run your crew, make sure to run\
    \
    - cd my-first-crew\
    - crewai install\
    \
    Step 4: Install below packages before run\
    \
    - uv pip install fastapi; uv add fastapi\
    - uv pip install apscheduler; uv add apscheduler\
    \
    Step 5: To run your crew, execute the following command in the root
    of your project\
    \
    - crewai run\
    \
    \##### Troubleshooting && Debugging \#####\
    \
    Error 1:\
    \
    - An error occurred while running the crew: Fallback to LiteLLM is
    not available\
    \
    Solution:\
    \
    - uv pip install LiteLLM\
    \
    - uv add litellm\
    \
    Addtional:\
    \
    Select the .venv path for interpreter\
    \
    - command + shift + p ---\> Select Python Interpreter ---\> Paste
    the .venv path\
    \
    - Ex:
    /Users/devopsmela/Desktop/CrewAI/kube-manifest-crew/kube_manifest_crew/.venv\
    \
    Error 2:\
    \
    - ImportError: Missing dependency No module named \'fastapi\'\
    \
    Solution:\
    \
    - uv pip install fastapi\
    \
    - uv add fastapi\
    \
    Error 3:\
    \
    - ImportError: Missing dependency No module named \'apscheduler\'\
    \
    Solution:\
    \
    - uv pip install apscheduler\
    \
    - uv add apscheduler\
    \
    Error 4:\
    \
    - Cache_breakpoint: is
    unsupported,\"type\":\"invalid_request_error\"\
    \
    Solution:\
    \
    - Used Azure Foundry in-place of Groq\
    \
    \
    \
    \
    \
    \
