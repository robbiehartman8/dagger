# queries

read_birthright_rule_query = """ 
select {0}
from birthright.birthright_rule
where {1} = '{2}'
"""