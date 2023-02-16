# this file contains all of the contants used in the identity service

import identity_pb2

# queries
read_identity_query = "select hr_id, user_id from identity.identity where hr_id = '{0}'"
create_identity_query = """
merge into identity i
using 
	(select ? as s) m on i.hr_id = m.s
when matched then update set i.legal_first_name = ?
when not matched then insert (identity_id, hr_id, user_id) 
values (?, ?, ?);
"""

response_data_null = identity_pb2.iamData(
    hr_id = None, 
    user_name = None
)
