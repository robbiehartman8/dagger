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

create_update_required_attributes = ["identity_id", "hr_id", "user_id"]

create_update_success_message = "Identity created or updated."
create_update_fail_message = "Identity creation or update failed."
