import snowflake.connector
from azure.keyvault.secrets import SecretClient
from azure.identity import DefaultAzureCredential
from config_utilities import keyvault_config
from config_utilities import snowflake_config

# TODO: fix the logging

class SnowflakeConnetion:
    
    def __init__(self):
        # establish connection with azure key vault
        self.keyVaultName = keyvault_config["kv_name"]
        self.KVUri = f"https://{self.keyVaultName}.vault.azure.net/"
        self.credential = DefaultAzureCredential()
        self.client = SecretClient(vault_url=self.KVUri, credential=self.credential)

        # get snowflake creds
        self.snow_username = self.client.get_secret(snowflake_config["username_key"]).value
        self.snow_password = self.client.get_secret(snowflake_config["password_key"]).value
        self.snow_account = self.client.get_secret(snowflake_config["account_key"]).value
        self.snow_warehouse = self.client.get_secret(snowflake_config["warehouse_key"]).value
        self.snow_database = self.client.get_secret(snowflake_config["database_key"]).value

    def getConnection(self):
        try:
            conn = snowflake.connector.connect(user=self.snow_username, password=self.snow_password, account=self.snow_account, warehouse=self.snow_warehouse, database=self.snow_database)
            return conn
        except:
            print('ERROR')