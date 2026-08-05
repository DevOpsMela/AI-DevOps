## Queries to be exetuted on Azure SRE Agent ## 

- Pull the recent alert activity around pythonapp-ai, then cross-check the App Insights resource for context and give a concise summary of what fired most recently.
RG # devopsmela-rg
Application Insights # pythonapp-ai

- Inspect the repo structure, key entry points, and any existing context first, then give a concise architecture summary with concrete improvement ideas.
Azure Project # AI-DevOps
Repo # SREProject

---------

Create a bug in Azure DevOps under Project **AI-DevOps**, Repository **SREProject** to investigate and fix the `/health` API endpoint.

**Issue Summary:**
The `/health` endpoint is not responding as expected (failing/returning incorrect status/intermittent issues).

**Priority:** High
**Tags:** SRE, API, HealthCheck, Production

Assign to the meladevops@gmail.com for immediate investigation.

--------

Create an Azure DevOps pipeline in Project **AI-DevOps**, Repository **SREProject** to build a Python Flask application.

**Requirements:**

* Detect Python version from project (default to Python 3.x if not specified)
* Install dependencies from `requirements.txt`
* Run basic validation (lint/test if available)
* Package the application as a build artifact

**Artifact Handling:**

* Copy all required application files and dependencies to a staging directory
* Publish artifacts to the default Azure DevOps **drop** location

**Pipeline Expectations:**

* Use YAML-based pipeline
* Trigger on changes to main branch
* Use Microsoft-hosted agent (Ubuntu latest)
* Ensure clear logging and failure visibility

**Output:**

* Generate complete working pipeline YAML
* Highlight any assumptions made about repo structure

--------

Analyze the build pipeline failure for CI **first_project-asp** in Azure DevOps Project **Azure_DevSecOps_11**.

**Instructions:**

1. Inspect the latest failed pipeline run, including logs, tasks, and error messages.
2. Identify the exact stage and step where the failure occurred.
3. Correlate failure with recent code changes, dependency updates, or pipeline modifications.
4. Check agent environment, tool versions, and external dependencies.
5. Validate build configuration (YAML/classic), variables, and secrets.

**Output Required:**

* Root cause of the failure (clear and specific)
* Impacted component (build, test, dependency, infra, etc.)
* Suggested fix with exact changes required
* Preventive measures to avoid recurrence

**Focus Areas:**

* Compilation/build errors
* Dependency resolution issues
* Authentication/permission failures
* Missing files or incorrect paths
* Pipeline misconfigurations

Keep the response concise, actionable, and aligned with SRE troubleshooting practices.

------