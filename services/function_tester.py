# (rule:location_code::varchar = '1003' or rule:location_code::varchar = 'NULL' or rule:location_code::varchar is null)

get_access_select_query = """ 
select birthright_rule_id, access_catalog_id
from birthright.birthright_rule
where {0}
"""


identity_data = {'identity_id': 'a695103c72ec15c903758592d7d7f294', 'create_ts': '2023-03-06 18:02:32.251', 'hr_id': '1', 'user_id': 'robert.h.hartman1', 'legal_first_name': 'robert', 'legal_middle_name': 'maurice', 'legal_last_name': 'hartman', 'preferred_first_name': 'robert', 'preferred_middle_name': 'maurice', 'preferred_last_name': 'hartman', 'use_preferred_name': 'false', 'job_title_code': 'ceo', 'job_title_description': 'chief executive officer', 'job_title_level': '100', 'location_code': '1001', 'location_name': 'norfolk', 'email_work_primary': 'robert.hartman@hartmancorp.com', 'status': 'A', 'hire_start_date': '2023-01-01', 'employee_type': 'FT', 'cost_center': '90000001', 'department_number': '1', 'department_name': 'executive department'}


where_list = []
for column, value in identity_data.items():
    where_clause = f"(rule:{column}::varchar = '{value}' or rule:location_code::varchar = 'NULL' or rule:location_code::varchar is null)"
    where_list.append(where_clause)

print(get_access_select_query.format(" and ".join([str(item) for item in where_list])))
