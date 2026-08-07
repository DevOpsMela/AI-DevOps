````markdown
# #  Module 8 – Azure DevOps (ADO) MCP Integration with Claude Desktop

## Agenda

- Azure DevOps – Introduction
- Understanding the basic concepts of Azure DevOps
- Azure DevOps MCP – Introduction
- Azure DevOps MCP Integration with Claude Desktop
- Azure DevOps MCP Configuration
- Demo
- Q&A

---

# Step 1: Prerequisites

Before configuring the Azure DevOps MCP server, ensure the following requirements are met:

## 1. Claude Desktop

Download and install **Claude Desktop** from Anthropic.

## 2. Node.js

Install **Node.js** on your machine. It is required to execute the MCP server using `npx`.

## 3. Azure DevOps Personal Access Token (PAT)

1. Sign in to your Azure DevOps organization.
2. Navigate to:

   **User Settings** → **Personal Access Tokens**

3. Select **New Token**.
4. Provide a name (for example: `Claude MCP`).
5. Grant the required permissions such as:
   - Code
   - Work Items
   - Build
   - Release (optional)
6. Create the token.
7. **Copy and save the token immediately**, as it will not be shown again.

---

# Step 2: Configure Claude Desktop

## 1. Open Claude Configuration

Open Claude Desktop and navigate to:

```text
Settings → Developer → Edit Config
```

This opens:

```text
claude_desktop_config.json
```

---

## 2. Add Azure DevOps MCP Server

Add the following configuration under the `mcpServers` section.

```json
{
  "mcpServers": {
    "azure-devops": {
      "command": "npx",
      "args": [
        "-y",
        "@azure-devops/mcp",
        "meladevops",
        "--authentication",
        "envvar"
      ],
      "env": {
        "AZURE_DEVOPS_ORG_URL": "https://dev.azure.com/meladevops/",
        "ADO_MCP_AUTH_TOKEN": "<YOUR_PAT_TOKEN>"
      }
    }
  }
}
```

> Replace:
>
> - `<YOUR_PAT_TOKEN>` with your Azure DevOps Personal Access Token.
> - `meladevops` and the organization URL if using a different Azure DevOps organization.

---

## 3. Restart Claude Desktop

Completely close Claude Desktop and reopen it.

---

## 4. Verify the Connection

After Claude restarts, verify the MCP server is loaded.

You should see either:

- 🔨 **Hammer icon**, or
- **Available Tools**

inside the Claude prompt area.

---

# Step 3: Example Prompts

## ✅ Project Management

```text
List all projects in my organization "meladevops".
```

## ✅ Pipeline Management

```text
List all failed build pipelines in project "Azure-MCP-Server".
```

```text
Investigate build pipeline "demo-project", identify the failure cause, and suggest a solution.
```

## ✅ Repository / Code Management

```text
Create a new branch "feature" from the main branch in repository "demo-project" under project "Azure-MCP-Server".
```

```text
Create a pull request from feature to main and add "meladevops" as the approver.
```

## ✅ Work Item Management

```text
Create an Issue titled "Work on Hello World Application" in project "Azure-MCP-Server".
```

---

# Additional Test Prompts

## 📁 Project Management

- List all projects in my organization.
- Get details of project **MCP-Server**.
- Show all repositories in project **MCP-Server**.
- List all teams in project **MCP-Server**.
- Show all users who have access to project **MCP-Server**.
- List all service connections in project **MCP-Server**.

---

## 🚀 Pipeline Management

- List all build pipelines.
- List all release pipelines.
- Show the last 20 pipeline runs.
- Show today's failed pipeline runs.
- Which pipeline has failed most frequently in the last 30 days?
- Show pipeline execution duration for the last 10 runs.
- List all queued builds.
- Cancel the currently running build.
- Re-run the last failed pipeline.
- Trigger pipeline **demo-project**.
- Download logs for build **#105**.
- Analyze build **#105** and explain why it failed.
- Which task consumed the most execution time?
- Compare build **#105** and **#106**.

---

## 📦 Repository Management

- List all repositories.
- List all branches in repository **demo-project**.
- Show the latest commits on the main branch.
- Who made the latest commit?
- Create branch **feature/login**.
- Delete branch **feature/test**.
- Compare feature branch with main.
- Show all tags.
- Search for file **azure-pipelines.yml**.
- Search for **Dockerfile** across repositories.
- Find every YAML pipeline in the repository.

---

## 🔀 Pull Request Management

- List all open pull requests.
- Show pull requests assigned to me.
- Create a pull request from feature to main.
- Assign **Rohit Singh** as reviewer.
- Add **meladevops** as approver.
- Show pending reviewers.
- Approve PR **#25**.
- Complete PR **#25**.
- Abandon PR **#25**.
- List merged pull requests from last week.

---

## 📝 Work Item Management

- Create a Bug.
- Create a User Story.
- Create a Task.
- Create an Epic.
- Assign the work item to me.
- List my active work items.
- Show overdue work items.
- Update priority of Bug **#123**.
- Move User Story to **Active**.
- Close Task **#220**.
- Link Bug **#123** to User Story **#100**.
- List blocked work items.

---

## 🧪 Test Management

- List all test plans.
- Show failed test cases.
- List test suites.
- Show test execution history.
- List flaky test cases.
- Who executed the last test run?

---

## 📊 Analytics & Reporting

- Show deployment success rate.
- Generate sprint summary.
- List the top 10 active contributors.
- Which repository has the highest number of commits?
- Show build success percentage.
- Generate a DevOps dashboard summary.
- Show pipeline trends for the last 90 days.
- List inactive repositories.
- Find repositories with no commits in the last six months.

---

## 🔒 Security & Permissions

- List all users with Project Administrator access.
- Show all PAT tokens.
- List expired service connections.
- Show repository permissions.
- Find users without MFA enabled.
- List all variable groups.
- Show secrets used by pipeline **demo-project**.

---

## 🤖 AI Investigation Queries

- Why did the latest deployment fail?
- Analyze pipeline logs and suggest fixes.
- Find the root cause of build failures.
- Suggest improvements to reduce pipeline execution time.
- Identify flaky pipelines.
- Find duplicate work items.
- Which pipelines are using deprecated tasks?
- Analyze the YAML pipeline and recommend best practices.
- Find repositories without branch policies configured.
- Generate a health report for my Azure DevOps project.

---

# Validation Coverage

These prompts collectively validate the Azure DevOps MCP server's ability to:

- Retrieve Azure DevOps information
- Execute DevOps operations
- Manage repositories
- Manage pull requests
- Manage work items
- Work with test plans
- Analyze pipelines
- Generate reports
- Audit security settings
- Perform AI-assisted investigations
- Automate common Azure DevOps workflows

These scenarios provide comprehensive coverage for testing Azure DevOps MCP capabilities with Claude Desktop.
````
