# Module 5 – Hugging Face & Ollama

## 📖 Overview

In this module, you'll learn how to use **Hugging Face** to discover AI models, datasets, and interactive applications, and how to run **Large Language Models (LLMs) locally** using **Ollama**.

By the end of this module, you'll be able to:

- Explore thousands of open-source AI models.
- Download and experiment with datasets.
- Use Hugging Face Spaces to test AI applications.
- Install and configure Ollama locally.
- Run LLMs without cloud services.
- Integrate Ollama with Python applications using its REST API.

---

# 📚 Course Agenda

1. Hugging Face – Introduction
2. Understanding Hugging Face Concepts
   - Models
   - Datasets
   - Spaces
3. Demo
4. Ollama – Introduction
5. Setting Up Ollama Locally
6. Demo

---

# 1. Hugging Face – Introduction

## What is Hugging Face?

Hugging Face is one of the world's largest open-source AI platforms. It provides developers and researchers with access to thousands of pre-trained AI models, datasets, and tools for building AI applications.

Think of Hugging Face as **GitHub for AI and Machine Learning**.

Instead of writing AI models from scratch, developers can download and use existing models with just a few lines of code.

---

## Why Hugging Face?

Hugging Face makes AI development much easier by providing:

- Thousands of open-source models
- Public datasets
- AI application hosting (Spaces)
- APIs for inference
- Community contributions
- Model documentation

---

## Popular Use Cases

- Chatbots
- Language Translation
- Text Summarization
- Image Generation
- Speech Recognition
- Sentiment Analysis
- Code Generation
- Document Question Answering

---

# 2. Hugging Face Concepts

The three most important concepts in Hugging Face are:

- Models
- Datasets
- Spaces

---

# Models

A **Model** is a trained AI system capable of performing a specific task.

Examples include:

- Text Generation
- Image Classification
- Translation
- Question Answering
- Summarization
- Embeddings

---

## Popular Models

| Model | Purpose |
|--------|----------|
| Llama 3 | Chat & Text Generation |
| Mistral | General-purpose LLM |
| DeepSeek | Reasoning & Coding |
| Phi | Lightweight AI Assistant |
| Gemma | Google's Open Model |
| Qwen | Multilingual LLM |
| Stable Diffusion | Image Generation |
| Whisper | Speech Recognition |
| BERT | NLP Classification |

---

## Model Information

Each model page typically includes:

- Description
- Architecture
- License
- Usage Instructions
- Example Code
- Downloads
- Community Discussions

---

# Datasets

Datasets are collections of data used for training and evaluating AI models.

Examples include:

- Text documents
- Images
- Videos
- Audio
- Question-Answer pairs
- CSV files

---

## Examples

| Dataset | Purpose |
|----------|----------|
| SQuAD | Question Answering |
| IMDB Reviews | Sentiment Analysis |
| Common Voice | Speech Recognition |
| WikiText | Language Modeling |
| COCO | Object Detection |

---

## Why Datasets Matter

Datasets help you:

- Train models
- Fine-tune models
- Benchmark performance
- Evaluate AI systems

---

# Spaces

Spaces are hosted AI applications built using:

- Gradio
- Streamlit
- Docker

They allow developers to showcase and share AI demos directly in the browser.

---

## Examples

- Chatbots
- Image Generators
- OCR Applications
- Resume Analyzers
- AI Assistants
- Speech-to-Text Applications

No local installation is required to try a Space.

---

# Hugging Face Workflow

```text
Dataset

↓

Train / Fine-tune

↓

Model

↓

Deploy

↓

Application (Space)
```

---

# Demo

During the demonstration, we will:

- Explore Hugging Face Hub
- Search for LLMs
- Download a model
- Browse datasets
- Test AI applications using Spaces

---

# 3. Ollama – Introduction

## What is Ollama?

Ollama is an open-source tool that allows you to run Large Language Models (LLMs) directly on your computer.

Instead of sending your data to cloud providers, Ollama executes models locally.

---

## Why Use Ollama?

Benefits include:

- Runs completely offline
- No API costs
- Better privacy
- Faster local inference
- Easy installation
- Supports many open-source LLMs

---

## Popular Models Supported

- Llama 3
- Mistral
- Gemma
- Phi
- Qwen
- DeepSeek
- Code Llama
- TinyLlama
- SQLCoder

---

# 4. System Requirements

The hardware required depends on the size of the model.

| Model Size | Recommended RAM |
|-------------|-----------------|
| 1B – 3B | 8 GB |
| 7B | 8–16 GB |
| 13B | 16 GB |
| 30B | 32 GB+ |
| 70B | 64 GB+ (Recommended) |

---

## Storage

Models typically require:

- Small models: 2–4 GB
- Medium models: 8–15 GB
- Large models: 30–40 GB+

---

## GPU

A GPU is optional but highly recommended for faster inference.

Supported GPUs include:

- NVIDIA CUDA
- Apple Silicon (Metal)
- AMD (limited support)

---

# 5. Installing Ollama

Visit:

https://ollama.com/download

---

## Supported Platforms

- Windows
- macOS
- Linux

---

## Linux Installation

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

---

## Verify Installation

```bash
ollama --version
```

---

# 6. Basic CLI Commands

## Run a Model

```bash
ollama run llama3.2
```

If the model is not available locally, Ollama automatically downloads it.

---

## Download a Model

```bash
ollama pull llama3.2
```

---

## List Installed Models

```bash
ollama list
```

---

## Delete a Model

```bash
ollama rm llama3.2
```

---

## Help

```bash
ollama help
```

---

# Ollama Workflow

```text
Pull Model

↓

Run Model

↓

Local REST API

↓

Python Application
```

---

# 7. Integrating Ollama with Python

Ollama exposes a REST API that runs locally.

Default Endpoint:

```text
http://localhost:11434
```

---

## Chat API

```text
http://localhost:11434/api/chat
```

---

# Project Setup

Create a virtual environment.

```bash
uv venv
```

Activate it.

macOS/Linux

```bash
source .venv/bin/activate
```

Windows

```powershell
.venv\Scripts\activate
```

---

## Install Packages

```bash
uv pip install ollama
```

```bash
uv pip install requests
```

---

## VS Code

Select the virtual environment.

```
Cmd + Shift + P

↓

Python: Select Interpreter
```

---

# Sample Python Application

```python
import requests
import json

url = "http://localhost:11434/api/chat"

payload = {
    "model": "llama3.2:latest",
    "messages": [
        {
            "role": "user",
            "content": "What is Python?"
        }
    ]
}

response = requests.post(
    url,
    json=payload,
    stream=True
)

if response.status_code == 200:

    print("Streaming response from Ollama:\n")

    for line in response.iter_lines(decode_unicode=True):

        if line:

            try:

                json_data = json.loads(line)

                if (
                    "message" in json_data
                    and "content" in json_data["message"]
                ):
                    print(
                        json_data["message"]["content"],
                        end=""
                    )

            except json.JSONDecodeError:

                print(
                    f"Failed to parse line: {line}"
                )

    print()

else:

    print(response.status_code)
    print(response.text)
```

---

# Understanding the Code

## Import Libraries

```python
import requests
import json
```

- **requests** sends HTTP requests.
- **json** parses JSON responses from Ollama.

---

## API Endpoint

```python
url = "http://localhost:11434/api/chat"
```

Explanation:

- `localhost` → Your own computer
- `11434` → Default Ollama port
- `/api/chat` → Chat API endpoint

---

## Payload

```python
payload = {
    "model": "llama3.2:latest",
    "messages": [
        {
            "role": "user",
            "content": "What is Python?"
        }
    ]
}
```

The payload specifies:

- Which model to use
- The conversation history
- The user's question

---

## Sending the Request

```python
response = requests.post(
    url,
    json=payload,
    stream=True
)
```

This sends a POST request to the Ollama server.

`stream=True` enables real-time streaming of the model's response.

---

## Reading the Stream

```python
for line in response.iter_lines():
```

Instead of waiting for the full response, the application receives tokens as they are generated.

This creates a ChatGPT-like streaming experience.

---

## Parsing JSON

Each streamed line is returned as a JSON object.

Example:

```json
{
  "message": {
    "content": "Python is..."
  }
}
```

The application extracts only the generated text.

---

## Displaying Output

```python
print(json_data["message"]["content"], end="")
```

This prints the response continuously without adding new lines.

---

# Benefits of Streaming

Compared to waiting for the entire response:

- Faster user experience
- Real-time generation
- Better responsiveness
- Suitable for chat applications

---

# Demo

During the demonstration, we will:

- Install Ollama
- Download an LLM
- Run a local chat session
- Explore CLI commands
- Build a Python application
- Connect using the REST API
- Stream responses in real time

---

# Key Takeaways

- Hugging Face is the leading platform for open-source AI models, datasets, and applications.
- Models perform AI tasks such as text generation, translation, and image recognition.
- Datasets are used for training and evaluating AI systems.
- Spaces provide browser-based AI demos built with Gradio, Streamlit, or Docker.
- Ollama enables you to run LLMs locally without cloud APIs.
- Local inference improves privacy and eliminates API costs.
- Ollama exposes a REST API that can be integrated with Python applications.
- Streaming responses create a smoother and more interactive user experience.

---

# Module Summary

In this module, you learned:

- Hugging Face fundamentals
- Models, Datasets, and Spaces
- Installing and using Ollama
- Running LLMs locally
- Core Ollama CLI commands
- Building a Python application with Ollama
- Calling the local REST API
- Streaming AI responses in real time

You are now ready to build local AI applications using open-source Large Language Models without relying on cloud services.
