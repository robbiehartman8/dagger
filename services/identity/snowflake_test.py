import sys
sys.path.insert(1, '/Users/roberthartman/Desktop/repos/dagger/services/utilities')

from snowflake_connection import SnowflakeConnetion






conn = SnowflakeConnetion().getConnection()

cur = conn.cursor()

results = cur.execute('select * from identity.identity').fetchall()
for rec in results:
    print(rec)

conn.close()