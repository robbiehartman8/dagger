import sys
sys.path.insert(1, '/Users/roberthartman/Desktop/repos/dagger/services/utilities')

from snowflake_connection import SnowflakeConnetion






conn = SnowflakeConnetion().getConnection()

cur = conn.cursor()
hr_id = "18874754"
results = cur.execute(f"select hr_id, user_id from identity.identity where hr_id = '{hr_id}'").fetchall()

print(results[0][0])

conn.close()