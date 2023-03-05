# this file contains all of the configs for the utilities

keyvault_config = {
    "kv_name": "kv-dagger"
}

snowflake_config = {
    "username_key": "snowflake-username",
    "password_key": "snowflake-password",
    "account_key": "snowflake-account",
    "warehouse_key": "snowflake-warehouse",
    "database_key": "snowflake-database"
}

# ["firstinitial-lastname-number"], ["random", length_of_username], ["firstname-middleinitial-lastname-number"]
username_generator_config = {
    "username_generator": ["firstname-middleinitial-lastname-number"]
}

company_email = {
    "email_ending": "hartmancorp.com"
}

service_ports = {
    "createUpdateIdentity": "50051",
    "readIdentity": "50052",
    "deleteIdentity": "50053",
    "appearUserId": "50054"
}

service_workers = {
    "createUpdateIdentity": 10,
    "readIdentity": 10,
    "deleteIdentity": 10,
    "appearUserId": 10
}

kafka_partitions = {
    "identity": {"identity_create": 4, "identity_update": 4, "identity_delete": 4},
    "provisioning": {"provisioning": 4, "deprovisioning": 4}
}