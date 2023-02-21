# this file contains all of the contants used in the identity service

# queries
read_identity_query = """
select {0}
from identity.identity
where {1} = '{2}'
"""

create_update_identity_query = """
merge into identity.identity i
using 
	(select '{0}' as s) m on i.hr_id = m.s
when matched then update set update_ts = current_timestamp, {1}
when not matched then insert ({2}) 
values ({3});
"""

read_user_id_query = """
select count(user_id) as user_id_count
from identity.identity
where user_id like '{0}%'
"""

create_update_required_attributes_success = ["identity_id", "hr_id", "user_id"]
create_update_required_attributes_failed = []

create_update_success_message = "Success: Identity created or updated."
create_update_fail_message = "Failed: Something went wrong trying to create or update the identity. Make sure you have the hr_id in the request."
