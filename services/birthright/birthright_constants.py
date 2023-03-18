# queries

read_birthright_rule_query = """ 
select {0}
from birthright.birthright_rule
where {1} = '{2}'
"""

access_data_string = """
'{"access_data": "' ,access_catalog_id,'"}'
"""

get_access_select_query = """ 
select access_catalog_id::varchar as access_data
from birthright.birthright_rule
where {1}
"""
get_access_where_clause = "(rule:{0}::varchar = '{1}' or rule:location_code::varchar = 'NULL' or rule:location_code::varchar is null)"

