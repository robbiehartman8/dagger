# this file contains all of the contants used in the identity service

# attributes
identity_select_attribute_list = [
    "identity_id", "create_ts",
    "update_ts", "hr_id",
    "user_id", "legal_first_name",
    "legal_middle_name", "legal_last_name",
    "preferred_first_name", "preferred_middle_name",
    "preferred_last_name", "job_title_code",
    "job_title_description", "job_title_level",
    "location_code", "location_name",
    "location_address", "phone_number_work",
    "phone_number_work_mobile", "phone_number_home",
    "phone_number_home_mobile", "email_work:primary",
    "email_home:primary", "status",
    "hire_start_date", "termination_date",
    "leave_of_absense_start_date", "leave_of_absense_end_date",
    "employee_type", "cost_center",
    "manager_identity_id", "manager_hr_id",
    "manager_user_id"
]

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