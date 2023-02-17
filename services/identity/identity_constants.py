# this file contains all of the contants used in the identity service

# queries
read_identity_query = """
select {0}
from identity.identity
where {1} = '{2}'
"""

create_identity_query = """
merge into identity i
using 
	(select ? as s) m on i.hr_id = m.s
when matched then update set i.legal_first_name = ?
when not matched then insert (identity_id, hr_id, user_id) 
values (?, ?, ?);
"""