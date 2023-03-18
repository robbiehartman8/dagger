# queries

read_birthright_rule_query = """ 
select {0}
from birthright.birthright_rule
where {1} = '{2}'
"""

get_access_select_query = """ 
select birthright_rule_id::string as, access_catalog_id::string as
from birthright.birthright_rule
where {0}
"""
get_access_where_clause = "(rule:{0}::varchar = '{1}' or rule:location_code::varchar = 'NULL' or rule:location_code::varchar is null)"

