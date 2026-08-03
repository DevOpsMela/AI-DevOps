resource "azurerm_resource_group" "myrg" {
  name     = var.rg
  location = var.location
}

resource "azurerm_storage_account" "mystorageaccount" {
  name                     = var.storage_account_name
  resource_group_name      = azurerm_resource_group.myrg.name
  location                 = azurerm_resource_group.myrg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}