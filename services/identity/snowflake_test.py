import sys
sys.path.insert(1, '/Users/roberthartman/Desktop/repos/dagger/services/utilities')

from snowflake.connector import DictCursor
from snowflake import connector

from snowflake_connection import SnowflakeConnetion

connector.paramstyle='qmark'


query1 = "select hr_id, user_id from identity.identity where hr_id = '{0}'".format("18874754")

conn = SnowflakeConnetion().getConnection()

cur = conn.cursor(DictCursor)


# values = ("kdkdkdk", "jdjdjdjdj", "jsdjjdjd")
# create_identity_query = "insert into identity.identity (IDENTITY_ID, HR_ID, USER_ID) values (?, ?, ?)"
# conn.cursor().execute(create_identity_query, values)
# conn.cursor().commit()

create_identity_query = """
merge into identity.identity i
using 
	(select ? as s) m on i.hr_id = m.s
when matched then update set i.legal_first_name = ?
when not matched then insert (identity_id, hr_id, user_id) 
values (?, ?, ?);
"""
values = ("nothing", "rob", "identity", "hr", "user")

conn.cursor().execute(create_identity_query, values)


conn.close()