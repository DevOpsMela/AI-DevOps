terraform {
  required_version = ">= 1.0.0"
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "4.78.0"
    }
  }
}

provider "azurerm" {
  features {}
  subscription_id = "f09178e6-305f-4469-a7c1-b8d45d4607b3"
}