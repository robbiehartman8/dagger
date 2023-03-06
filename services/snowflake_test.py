import logging
import sys
sys.path.insert(1, "/Users/roberthartman/Desktop/repos/dagger/services/utilities")

from snowflake_connection_utilities import SnowflakeConnetion
from query_utilities import QueryUtilities

logger = logging.getLogger()
logger.setLevel(logging.INFO)

snow = SnowflakeConnetion().getConnection(logger)

merge = """
merge into identity.identity i
using 
	(select '929292' as s) m on i.hr_id = m.s
when matched then update set update_ts = current_timestamp
when not matched then insert (identity_id, hr_id, user_id) 
values ('929292', '929292', '939393');
"""

update = """ 
update identity.identity
set update_ts = current_timestamp
"""

result = QueryUtilities().executeCreateUpdate(merge, "create_update", snow, logger)

print(result)





