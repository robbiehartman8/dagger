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
when matched then update set {1}
when not matched then insert ({2}) 
values ({3});
"""

mark_for_delete_query = """
update identity.identity
set update_ts = current_timestamp, to_be_deleted = 1
where {0} = '{1}'
"""

# messages
create_update_success_message = "Success: Identity created or updated."
create_update_fail_message = "Failed: Something went wrong trying to create or update the identity. Make sure you have the hr_id in the request."

appear_userid_success_message = "Success: recieved user_id"

mark_for_delete_success_message = "Success: user marked for delete"
mark_for_delete_fail_ude_message = "Failed: user doesnt exist"
mark_for_delete_fail_service_message = "Failed: did not complete request.  Make sure you have hr_id or identity_id in the request"
