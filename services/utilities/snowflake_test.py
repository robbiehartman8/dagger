from snowflake_connection_utilities import SnowflakeConnetion
import sys
sys.path.insert(1, "/Users/roberthartman/Desktop/repos/dagger/services/identity")
from identity_utilities import IdentityUtilities


read_user_id_query = """
select user_id
from identity.identity
where user_id like '{0}%'
"""

conn = SnowflakeConnetion().getConnection()

first_name = "robert"
middle_name = ""
last_name = "hartman"

user_id = IdentityUtilities().getUserId(conn, first_name, middle_name, last_name, read_user_id_query)

print(user_id)
