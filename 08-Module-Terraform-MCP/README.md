# # Module 8 – Terraform Fundamentals and Terraform MCP

## Agenda

1. Prerequisites
2. Terraform – Introduction
3. Setting Up Terraform Locally
4. Understanding the Terraform Workflow
5. Terraform State File and Providers – Explained
6. Terraform MCP – Introduction
7. Various Use Cases of Terraform MCP
8. Demo

---

# 1. Prerequisites

Before getting started with Terraform, install the following software:

* Terraform CLI
* Azure CLI
* Visual Studio Code (VS Code)
* HashiCorp Terraform Extension for VS Code
* Git Client

## 1.1 Install Git Client

Git is required when working with Terraform modules and version control.

Download Git:

[https://git-scm.com/downloads](https://git-scm.com/downloads)

Verify the installation:

```bash
git --version
```

---

## 1.2 Install Azure CLI

Download and install the Azure CLI for Windows:

[https://learn.microsoft.com/cli/azure/install-azure-cli-windows](https://learn.microsoft.com/cli/azure/install-azure-cli-windows)

Verify the installation:

```bash
az version
```

---

## 1.3 Install Terraform

Download Terraform:

[https://developer.hashicorp.com/terraform/downloads](https://developer.hashicorp.com/terraform/downloads)

### Installation Steps

1. Download the Terraform ZIP file.
2. Extract the downloaded package.
3. Create a folder such as:

```text
C:\terraform-binaries
```

4. Copy `terraform.exe` into the folder.
5. Add the folder to the Windows **PATH** environment variable.
6. Open a new Command Prompt or PowerShell window.
7. Verify the installation:

```bash
terraform version
```

---

## 1.4 Install Visual Studio Code

Download VS Code:

[https://code.visualstudio.com/](https://code.visualstudio.com/)

---

## 1.5 Install the HashiCorp Terraform Extension

1. Open Visual Studio Code.
2. Go to **Extensions** (`Ctrl + Shift + X`).
3. Search for **Terraform**.
4. Install the official extension published by **HashiCorp**.

---

## 1.6 Authenticate with Azure

Sign in to Azure using Azure CLI:

```bash
az login
```

### List Azure Subscriptions

```bash
az account list
```

### Set the Active Subscription

```bash
az account set --subscription="SUBSCRIPTION_ID"
```

### If Browser Login Fails

```bash
az login --use-device-code
```

---

# 2. Terraform – Introduction

## What is Terraform?

Terraform is an open-source Infrastructure as Code (IaC) tool developed by HashiCorp. It allows you to define, provision, and manage cloud infrastructure using code.

Terraform uses **HashiCorp Configuration Language (HCL)**, making infrastructure deployments repeatable, consistent, and version-controlled.

## Key Benefits

* Infrastructure as Code (IaC)
* Multi-cloud support
* Declarative configuration
* Version-controlled infrastructure
* Automation
* Reusable modules
* Large provider ecosystem
* Consistent deployments

---

# 3. Setting Up Terraform Locally

After installing the prerequisites:

* Verify Terraform installation.
* Verify Azure CLI installation.
* Verify Git installation.
* Install the Terraform extension in VS Code.
* Authenticate with Azure using Azure CLI.

### Verify All Tools

```bash
terraform version
git --version
az version
code --version
```

---

# 4. Understanding the Terraform Workflow

Terraform follows a simple workflow.

## Step 1 – Write Configuration

Create Terraform configuration files.

Example:

```hcl
resource "azurerm_resource_group" "rg" {
  name     = "demo-rg"
  location = "East US"
}
```

---

## Step 2 – Initialize

Downloads required providers.

```bash
terraform init
```

---

## Step 3 – Validate

Checks configuration syntax.

```bash
terraform validate
```

---

## Step 4 – Plan

Shows what Terraform will create, update, or delete.

```bash
terraform plan
```

---

## Step 5 – Apply

Deploys the infrastructure.

```bash
terraform apply
```

---

## Step 6 – Destroy

Deletes the deployed infrastructure.

```bash
terraform destroy
```

---

## Terraform Workflow Diagram

```text
Write Terraform Code
        │
        ▼
terraform init
        │
        ▼
terraform validate
        │
        ▼
terraform plan
        │
        ▼
terraform apply
        │
        ▼
Infrastructure Created
        │
        ▼
terraform destroy
```

---

# 5. Terraform State File and Providers – Explained

## Terraform State File

Terraform stores infrastructure information in a file named:

```text
terraform.tfstate
```

The state file stores:

* Resource IDs
* Current infrastructure status
* Dependencies
* Metadata
* Resource mappings

## Why Is the State File Important?

* Tracks deployed resources
* Detects infrastructure drift
* Maps configuration to real infrastructure
* Speeds up deployments

### Best Practice

Store the state remotely using:

* Azure Storage Account
* AWS S3
* Terraform Cloud

Do **not** commit the state file to Git.

---

## Terraform Providers

Providers allow Terraform to interact with cloud platforms and services.

Popular providers include:

* AzureRM
* AWS
* Google Cloud
* Kubernetes
* VMware
* GitHub

Example:

```hcl
provider "azurerm" {
  features {}
}
```

Providers are downloaded automatically during:

```bash
terraform init
```

---

# 6. Terraform MCP – Introduction

## What is Terraform MCP?

Terraform MCP (Model Context Protocol) enables AI assistants to understand Terraform configurations and interact with infrastructure projects using structured context.

Instead of only generating code, Terraform MCP enables AI to:

* Read Terraform projects
* Understand modules
* Explain resources
* Generate Terraform code
* Suggest best practices
* Troubleshoot deployment issues
* Improve developer productivity

---

# 7. Various Use Cases of Terraform MCP

## Code Generation

Generate Terraform code for:

* Resource Groups
* Storage Accounts
* Virtual Networks
* Virtual Machines
* AKS Clusters

---

## Infrastructure Analysis

* Explain resources
* Understand dependencies
* Review modules
* Analyze variables and outputs

---

## Documentation Generation

Generate:

* Resource documentation
* Module documentation
* Infrastructure summaries
* Architecture explanations

---

## Security Review

* Detect insecure configurations
* Recommend best practices
* Validate provider settings

---

## Troubleshooting

Assist with:

* Terraform errors
* State file issues
* Provider errors
* Dependency problems
* Syntax issues

---

## Learning Assistant

Terraform MCP can:

* Explain HCL
* Explain Terraform commands
* Generate examples
* Recommend best practices
* Answer Terraform questions

---

# 8. Demo

## Demonstration Objectives

During the demo, you will:

* Create a Terraform project
* Configure the Azure provider
* Initialize Terraform
* Validate the configuration
* Generate an execution plan
* Deploy an Azure Resource Group
* Verify deployment in the Azure Portal
* Destroy the deployed infrastructure

## Demo Commands

```bash
terraform init

terraform validate

terraform plan

terraform apply

terraform destroy
```

---

# Summary

By the end of this session, you will understand:

* Terraform fundamentals
* Local environment setup
* Terraform workflow
* Terraform state management
* Providers
* Terraform MCP
* Practical Terraform MCP use cases
* End-to-end infrastructure deployment using Terraform

---
