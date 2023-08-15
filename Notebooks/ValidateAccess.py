# Databricks notebook source
# MAGIC %fs ls /mnt/bronze

# COMMAND ----------

configs = {"fs.azure.account.auth.type": "OAuth",
           "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
           "fs.azure.account.oauth2.client.id": "<<sp_client_id>>",
           "fs.azure.account.oauth2.client.secret": "<<sp_client_secret>>",
           "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/<<tenant_id>>/oauth2/token"}

# Mount the Data Lake Gen2 account
dbutils.fs.mount(
  source = "abfss://gold@<<your_azure_databricks>>.dfs.core.windows.net/",
  mount_point = "/mnt/gold",
  extra_configs = configs)

