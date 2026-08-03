# Module 4 – Azure AI Services

## 📖 Overview

Azure AI Services is Microsoft's comprehensive suite of cloud-based AI capabilities that enables developers to build intelligent applications without requiring deep expertise in machine learning.

In this module, you'll learn how to work with **Azure AI Foundry**, deploy Large Language Models (LLMs), build AI Agents, integrate them with custom Python applications, and explore Azure's pre-built AI services such as Vision, OCR, Language, Speech, Face API, and AI Search with Retrieval-Augmented Generation (RAG).

By the end of this module, you'll be able to build production-ready AI applications using Azure AI Services.

---

# 📚 Course Agenda

1. Azure AI Ecosystem Overview
2. Azure AI Foundry – Introduction
3. Azure OpenAI Service (Deployment)
4. Azure AI Vision & OCR
5. Azure Face API
6. Azure AI Language (Text Analytics & Classification)
7. Azure AI Search + RAG
8. Demo

---

# 1. Azure AI Ecosystem Overview

Microsoft Azure provides a rich ecosystem of AI services that allow developers to add intelligence into applications with minimal machine learning expertise.

## Azure AI Ecosystem

- Azure AI Foundry
- Azure OpenAI Service
- Azure AI Vision
- Azure AI Speech
- Azure AI Translator
- Azure AI Language
- Azure AI Search
- Azure AI Document Intelligence
- Azure AI Content Safety
- Azure AI Agent Service

These services can be combined to build enterprise-grade AI applications.

---

# 2. Prerequisites

Before starting the hands-on labs, ensure the following tools are installed.

## Python

Install **Python 3.10 or later**.

Verify installation:

```bash
python3 --version
```

---

## Install UV (Fast Python Package Manager)

### macOS / Linux

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Windows

Download and install from:

https://docs.astral.sh/uv/

After installation, restart your terminal.

Verify:

```bash
uv --version
```

---

## Create a Virtual Environment

```bash
uv venv
```

### Activate on macOS/Linux

```bash
source .venv/bin/activate
```

### Activate on Windows

```powershell
.venv\Scripts\activate
```

---

## Install Azure CLI

Verify:

```bash
az version
```

Login:

```bash
az login
```

Select the correct Azure subscription before continuing.

---

# 3. Azure AI Foundry – Introduction

Azure AI Foundry is Microsoft's unified platform for building, deploying, evaluating, and managing AI applications and AI Agents.

It provides:

- AI Playground
- Model Catalog
- Agent Service
- Prompt Flow
- Monitoring
- Evaluation
- Deployments
- SDK Integration

---

# Hands-on Lab – Building an AI Agent

---

## Step 1 – Create an Azure AI Foundry Project

Create:

**Resource**

```
devopsmela-openai
```

**Project**

```
devopsmela-openai-proj
```

---

## Step 2 – Create an AI Agent

Create a new Agent.

Example name:

```
devopsmela-openai-agent
```

Choose model:

```
gpt-nano
```

> **Tip:** GPT-Nano is one of the most cost-effective models for demonstrations and learning.

---

## Step 3 – Configure Monitoring

Create a separate **Application Insights** resource.

Connect it:

```
Agent
    → Monitor
        → Connect Application Insights
```

This enables telemetry, diagnostics, and monitoring.

---

## Step 4 – Configure Agent Instructions

Upload the HR policy documents provided with the course.

Example documents:

- Global Time Off and Holidays
- Leave Types and Procedures
- Travel and Expense Policy
- Remote Work Policy
- HR FAQs

---

### Agent Instructions

```text
You are a helpful, policy-accurate HR assistant for Globomantics employees.

You answer questions using the provided HR documents:

- Global Time Off and Holidays
- Travel and Expense Policy
- Remote Work and Mobility
- Leave Types and Procedures
- HR FAQ

Quote or summarize these policies in plain language and tell the employee which document you used.

If a question is not covered by the documents, clearly say you don't know and suggest contacting HR rather than guessing.
```

---

## Step 5 – Test the Agent

Example Prompt

```
What public holidays does a German citizen get?
```

Test using:

- Playground
- Preview Application

Verify that the responses come from uploaded HR documents.

---

## Step 6 – Configure Authentication

Create:

```
User Managed Identity
```

Assign RBAC role:

```
Azure AI User
```

Scope:

```
Azure AI Foundry Resource
```

---

## Step 7 – Generate Python SDK Code

Navigate to:

```
Playground

↓

Call Agent

↓

Python
```

Copy the generated Python code.

---

## Step 8 – Publish the Agent

Click:

```
Publish Agent
```

Publishing creates production endpoints that can be consumed from external applications.

> **Note:** Published endpoints are intended for custom applications and APIs, not browser-based Playground testing.

---

# 4. Build a Python Client

Create the following structure.

```
OpenAI/

│── run_agent.py
│── .venv/
│── requirements.txt
```

---

## Install Required Packages

```bash
uv pip install openai
```

```bash
uv pip install azure.identity
```

```bash
uv pip install azure-ai-projects
```

---

## Configure VS Code Interpreter

Open Command Palette

```
Cmd + Shift + P
```

Choose

```
Python: Select Interpreter
```

Select

```
.venv
```

---

## Login

```bash
az login
```

Choose the correct Azure subscription.

---

## Sample Code

```python
from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient

endpoint = "https://YOUR_PROJECT.services.ai.azure.com/api/projects/YOUR_PROJECT"

project_client = AIProjectClient(
    endpoint=endpoint,
    credential=DefaultAzureCredential(),
)

my_agent = "devopsmela-openai-agent"
my_version = "3"

openai_client = project_client.get_openai_client()

response = openai_client.responses.create(
    input=[
        {
            "role": "user",
            "content": "What public holidays does a German citizen get?"
        }
    ],
    extra_body={
        "agent_reference": {
            "name": my_agent,
            "version": my_version,
            "type": "agent_reference"
        }
    },
)

print(response.output_text)
```

Run:

```bash
python3 run_agent.py
```

---

# Understanding the Code

## Authentication

```python
DefaultAzureCredential()
```

Automatically authenticates using:

- Azure CLI
- VS Code
- Managed Identity
- Environment Variables

---

## AIProjectClient

```python
AIProjectClient()
```

Connects your Python application to the Azure AI Foundry project.

---

## OpenAI Client

```python
project_client.get_openai_client()
```

Returns an OpenAI-compatible client for interacting with deployed Azure AI models and Agents.

---

## Agent Reference

Instead of calling a model directly, the request references your published Agent.

```python
extra_body={
    "agent_reference": {
        "name": "...",
        "version": "...",
        "type": "agent_reference"
    }
}
```

This routes the request through your configured Agent, allowing it to use uploaded documents and custom instructions.

---

# 5. Azure Speech Service (Text-to-Speech)

Azure Speech converts text into natural-sounding speech using neural voices.

Typical use cases:

- Voice Assistants
- Chatbots
- IVR Systems
- Accessibility
- E-learning

---

## Install SDK

```bash
uv pip install azure-cognitiveservices-speech
```

---

## Sample Code

```python
import azure.cognitiveservices.speech as speechsdk

speech_config = speechsdk.SpeechConfig(
    subscription="YOUR_KEY",
    endpoint="YOUR_ENDPOINT"
)

speech_config.speech_synthesis_voice_name = "en-US-Ava:DragonHDLatestNeural"

speech_synthesizer = speechsdk.SpeechSynthesizer(
    speech_config=speech_config
)

result = speech_synthesizer.speak_text_async(
    "Hello! Welcome to Azure AI."
).get()
```

---

# 6. Azure Translator Service

Azure Translator provides real-time translation across hundreds of languages.

Typical scenarios:

- Chatbots
- Customer Support
- Global Applications
- Multilingual Websites

---

## Install

```bash
uv pip install requests
```

---

## Example

Translate:

```
Doctor is available next Monday.
```

Target languages:

- Spanish
- Hindi

The Translator API returns translated text for each requested language.

---

# 7. Azure OpenAI Service

Azure OpenAI allows organizations to deploy OpenAI models securely within Azure.

Supported capabilities include:

- GPT Models
- Embeddings
- Chat Applications
- Function Calling
- Structured Outputs
- Image Generation
- Audio Models

Typical workflow:

```
Deploy Model

↓

Create Deployment

↓

Call via SDK

↓

Integrate into Application
```

---

# 8. Azure AI Vision & OCR

Azure AI Vision analyzes images and extracts useful information.

Capabilities include:

- Image Captioning
- OCR
- Object Detection
- Dense Captions
- Smart Cropping
- Background Removal

OCR extracts printed and handwritten text from images and documents.

---

# 9. Azure Face API

Azure Face API provides facial analysis capabilities.

Features include:

- Face Detection
- Face Verification
- Face Identification
- Face Attributes
- Face Grouping

Typical use cases:

- Attendance Systems
- Identity Verification
- Access Control
- Photo Management

---

# 10. Azure AI Language

Azure AI Language provides natural language processing services.

Capabilities include:

- Sentiment Analysis
- Key Phrase Extraction
- Entity Recognition
- Language Detection
- Text Classification
- Question Answering
- Conversational Language Understanding

---

# 11. Azure AI Search + RAG

Azure AI Search enables enterprise search and Retrieval-Augmented Generation (RAG).

Typical architecture:

```
Documents

↓

Chunking

↓

Embeddings

↓

Azure AI Search

↓

Vector Search

↓

Retrieved Context

↓

Azure OpenAI

↓

Grounded Response
```

Benefits:

- Reduces hallucinations
- Uses enterprise knowledge
- Improves response accuracy
- Enables document-based chatbots

---

# Demo

During the live demonstration, we will:

- Create an Azure AI Foundry project
- Deploy GPT-Nano
- Create an AI Agent
- Upload HR documents
- Configure Application Insights
- Publish the Agent
- Connect using Python SDK
- Authenticate using Azure CLI
- Build a custom Python application
- Generate speech using Azure Speech
- Translate text using Azure Translator
- Explore Azure AI Search with RAG

---

# Key Takeaways

- Azure AI Foundry is Microsoft's unified platform for building AI applications.
- Azure AI Agents can be configured with custom instructions and enterprise documents.
- Application Insights enables monitoring and diagnostics.
- Azure AI Projects SDK allows seamless integration with Python applications.
- DefaultAzureCredential simplifies secure authentication.
- Azure Speech converts text into natural speech.
- Azure Translator supports multilingual applications.
- Azure AI Vision extracts insights from images and documents.
- Azure AI Language enables advanced NLP capabilities.
- Azure AI Search with RAG provides grounded, enterprise-ready AI responses.

---

# Module Summary

In this module, you learned:

- Azure AI ecosystem overview
- Azure AI Foundry fundamentals
- Deploying Azure OpenAI models
- Creating and publishing AI Agents
- Monitoring with Application Insights
- Authentication using Azure CLI and Managed Identity
- Integrating AI Agents with Python
- Azure Speech (Text-to-Speech)
- Azure Translator
- Azure Vision & OCR
- Azure Face API
- Azure AI Language
- Azure AI Search with Retrieval-Augmented Generation (RAG)

You are now ready to build secure, scalable, and enterprise-grade AI applications using Azure AI Services.