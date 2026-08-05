# Module 6 – Agentic AI, CrewAI & Azure SRE Agent

## 📖 Overview

Large Language Models (LLMs) are excellent at generating responses, but they are limited to answering a single prompt at a time. Modern AI applications often require planning, reasoning, memory, tool usage, and collaboration between multiple AI agents.

This is where **Agentic AI** comes into the picture.

In this module, you'll learn what Agentic AI is, how AI agents work together, the popular Agentic AI frameworks available today, and how to build multi-agent systems using **CrewAI**. Finally, you'll build an **Azure Site Reliability Engineering (SRE) Agent** that automates troubleshooting and operational tasks.

---

# 📚 Course Agenda

1. Agentic AI – Introduction
2. Understanding Agentic AI Workflow
3. Agentic AI Frameworks
4. CrewAI
5. CrewAI – Introduction
6. Anatomy of CrewAI
   - Role
   - Goal
   - Backstory
   - Memory
7. Azure SRE Agent – Introduction
8. Characteristics of Azure SRE Agent
9. Demo

---

# 1. Agentic AI – Introduction

## What is Agentic AI?

Agentic AI refers to AI systems that can **reason, plan, make decisions, use tools, collaborate with other agents, and complete complex tasks autonomously**.

Unlike traditional LLMs that simply respond to prompts, AI Agents can:

- Plan tasks
- Break large problems into smaller steps
- Use external tools
- Search the web
- Read documents
- Execute code
- Remember previous interactions
- Collaborate with other agents

Think of an AI Agent as an intelligent digital employee rather than just a chatbot.

---

## Traditional LLM vs Agentic AI

| Traditional LLM | Agentic AI |
|-----------------|------------|
| Answers one prompt | Solves complete tasks |
| No planning | Plans before acting |
| Limited memory | Can maintain memory |
| Single response | Multi-step workflows |
| No collaboration | Multiple agents collaborate |
| Limited tool usage | Uses APIs, databases, and tools |

---

## Real-World Examples

- Customer Support Agents
- DevOps Assistants
- Site Reliability Engineering (SRE) Agents
- Coding Assistants
- Research Assistants
- HR Agents
- Financial Advisors
- Travel Planning Agents

---

# 2. Agentic AI Workflow

Most AI Agents follow a common workflow.

```text
User Request
        │
        ▼
Reasoning & Planning
        │
        ▼
Task Breakdown
        │
        ▼
Select Appropriate Tools
        │
        ▼
Execute Tasks
        │
        ▼
Collect Results
        │
        ▼
Validate Output
        │
        ▼
Final Response
```

---

## Example

User asks:

> "Find why my AKS cluster is unhealthy."

The AI Agent may:

1. Check Azure Monitor.
2. Query Kubernetes events.
3. Inspect pod logs.
4. Analyze node status.
5. Review recent deployments.
6. Identify the root cause.
7. Suggest or perform remediation.

Instead of answering directly, the agent performs multiple actions before responding.

---

# 3. Agentic AI Frameworks

Several frameworks simplify the development of AI agents.

| Framework | Description |
|-----------|-------------|
| CrewAI | Multi-agent collaboration framework |
| LangGraph | Stateful workflows built on LangChain |
| AutoGen | Multi-agent conversations by Microsoft |
| Semantic Kernel | AI orchestration framework by Microsoft |
| OpenAI Agents SDK | Build AI agents using OpenAI APIs |
| LlamaIndex Workflows | Retrieval and workflow orchestration |

---

## Why Use Frameworks?

Frameworks provide:

- Agent orchestration
- Memory management
- Tool integration
- Task scheduling
- Multi-agent collaboration
- Workflow automation

---

# 4. CrewAI

## What is CrewAI?

CrewAI is an open-source framework for building teams of AI agents that collaborate to complete complex tasks.

Instead of relying on a single agent, CrewAI enables multiple specialized agents to work together.

Each agent has:

- A specific role
- A clear goal
- A unique backstory
- Access to tools
- Assigned tasks

This mirrors how teams collaborate in real organizations.

---

## CrewAI Workflow

```text
User Request
      │
      ▼
Crew
      │
      ▼
Agent 1 ──► Agent 2 ──► Agent 3
      │
      ▼
Shared Result
      │
      ▼
Final Answer
```

---

## Why CrewAI?

- Modular architecture
- Reusable agents
- Easy YAML configuration
- Tool integration
- Memory support
- Sequential or parallel execution
- Enterprise-ready workflows

---

# 5. Anatomy of CrewAI

A CrewAI application consists of Agents, Tasks, Tools, Memory, and the Crew that orchestrates everything.

---

## Role

The **Role** defines who the AI agent is.

Examples:

- Kubernetes Expert
- Azure Architect
- DevOps Engineer
- SRE Engineer
- Security Analyst
- HR Assistant

Example:

```yaml
role: Azure SRE Engineer
```

---

## Goal

The **Goal** defines what the agent is expected to accomplish.

Example:

```yaml
goal: Identify the root cause of Azure infrastructure issues and recommend solutions.
```

The goal keeps the agent focused on the desired outcome.

---

## Backstory

The **Backstory** provides background information that influences the agent's reasoning and communication style.

Example:

```yaml
backstory:
You are an experienced Azure Site Reliability Engineer with over 15 years of experience managing enterprise cloud environments. You specialize in troubleshooting Kubernetes clusters, Azure networking, monitoring, and production incidents.
```

A rich backstory helps the agent produce more relevant and domain-specific responses.

---

## Memory

Memory enables agents to retain information across tasks or conversations.

Types of memory include:

- Short-term memory
- Long-term memory
- Conversation history
- Knowledge base memory

Benefits:

- Avoids repeating work
- Maintains context
- Supports multi-step reasoning
- Improves user experience

---

# 6. CrewAI Project Structure

A typical CrewAI project contains the following files. :contentReference[oaicite:0]{index=0}

```text
my-first-crew/
│
├── agents.yaml
├── tasks.yaml
├── crew.py
├── main.py
├── .env
├── tools/
└── knowledge/
```

---

## Purpose of Each File

| File | Purpose |
|------|----------|
| `agents.yaml` | Define AI agents and their roles |
| `tasks.yaml` | Configure tasks and workflows |
| `crew.py` | Orchestrate agents and tasks |
| `main.py` | Entry point of the application |
| `.env` | Store API keys and environment variables |
| `tools/` | Custom tools used by agents |
| `knowledge/` | Knowledge base and reference documents |

---

# 7. Azure SRE Agent – Introduction

A Site Reliability Engineering (SRE) Agent assists cloud engineers by automating operational tasks and troubleshooting.

Instead of manually checking logs, dashboards, and Kubernetes resources, the SRE Agent performs these activities automatically.

---

## Typical Responsibilities

- Monitor Azure resources
- Analyze application logs
- Troubleshoot AKS clusters
- Investigate incidents
- Validate deployments
- Review Infrastructure as Code
- Generate operational reports
- Recommend remediation steps

---

# Azure SRE Agent Workflow

```text
Incident Raised
        │
        ▼
Collect Monitoring Data
        │
        ▼
Check Azure Resources
        │
        ▼
Analyze Logs
        │
        ▼
Inspect Kubernetes
        │
        ▼
Identify Root Cause
        │
        ▼
Recommend Fix
```

---

# 8. Characteristics of an Azure SRE Agent

An effective Azure SRE Agent should have the following characteristics:

## Azure Expertise

- Virtual Machines
- App Services
- AKS
- Azure Monitor
- Log Analytics
- Azure Networking
- Azure Storage

---

## Kubernetes Knowledge

- Pods
- Deployments
- Services
- Ingress
- ConfigMaps
- Secrets
- Events
- Logs

---

## Observability

The agent should analyze:

- Metrics
- Logs
- Alerts
- Dashboards
- Application Insights
- Prometheus
- Grafana

---

## Incident Response

The agent should be capable of:

- Detecting failures
- Identifying root causes
- Suggesting remediation
- Generating incident summaries

---

## Infrastructure Knowledge

The SRE Agent should understand:

- Terraform
- Bicep
- ARM Templates
- Azure DevOps Pipelines
- GitHub Actions
- CI/CD Workflows

---

## Security Awareness

The agent should identify:

- Misconfigured resources
- RBAC issues
- Secret exposure
- Network vulnerabilities
- Compliance concerns

---

# Demo

During the live demonstration, we will:

- Install and configure CrewAI
- Create a new CrewAI project
- Understand the project structure
- Configure agents using `agents.yaml`
- Define workflows in `tasks.yaml`
- Build an Azure SRE Agent
- Execute the Crew locally
- Observe how multiple agents collaborate to troubleshoot Azure infrastructure

---

# Key Takeaways

- Agentic AI extends LLMs with reasoning, planning, memory, and tool usage.
- AI agents can autonomously perform complex, multi-step workflows.
- CrewAI enables teams of specialized AI agents to collaborate effectively.
- Every CrewAI agent is defined by its **Role**, **Goal**, **Backstory**, and **Memory**.
- CrewAI projects are organized using configuration files such as `agents.yaml` and `tasks.yaml`.
- Azure SRE Agents automate cloud monitoring, incident response, and troubleshooting, improving operational efficiency.

---

# Module Summary

In this module, you learned:

- What Agentic AI is
- How Agentic AI workflows operate
- Popular Agentic AI frameworks
- CrewAI fundamentals
- Anatomy of a CrewAI agent
- CrewAI project structure
- Azure SRE Agent architecture
- Key characteristics of an enterprise SRE Agent

You are now ready to design and build intelligent multi-agent systems capable of automating real-world DevOps and Site Reliability Engineering workflows.

