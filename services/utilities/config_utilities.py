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

# put into kv
kafka_config = {
    "kafka_host": ["kafka1:19092"]
}

redis_config = {
    "redis_host": "redis-stack",
    "redis_port": 6379,
    "redis_database": 0
}

service_config = {
    # identity
    "createUpdateIdentity": {"host": "server_create_update_identity", "port": "50051", "workers": 10},
    "readIdentity": {"host": "server_read_identity", "port": "50052", "workers": 10},
    "deleteIdentity": {"host": "server_delete_identity", "port": "50053", "workers": 10},
    "appearUserId": {"host": "server_appear_user_id_identity", "port": "50054", "workers": 10},
    # birthright
    "readBirthright": {"host": "server_read_birthright", "port": "50055", "workers": 10},
    "getAccessBirthright": {"host": "server_get_access_birthright", "port": "50056", "workers": 10},
}

# ["firstinitial-lastname-number"], ["random", length_of_username], ["firstname-middleinitial-lastname-number"]
username_generator_config = {
    "username_generator": ["firstname-middleinitial-lastname-number"]
}

company_email_config = {
    "email_ending": "hartmancorp.com"
}

kafka_partitions = {
    "identity": {"identity_create": 4, "identity_update": 4, "identity_delete": 4},
    "provisioning": {"provisioning": 4, "deprovisioning": 4}
}