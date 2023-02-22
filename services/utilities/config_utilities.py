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
    "createUpdateIdentity": 15,
    "readIdentity": 15,
    "deleteIdentity": 10,
    "appearUserId": 15
}