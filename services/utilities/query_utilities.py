# this file helps construct queries for the services

from snowflake_connection_utilities import SnowflakeConnetion
from snowflake.connector import DictCursor

class QueryUtilities:

    def getSelectQuery(self, attribute_list):
        select = ""
        for attribute in attribute_list:
            select = select + f"{attribute}::string as {attribute.replace(':', '_')},"
        return select[:-1]

    def getMergeQuery(self, reuqest_data, merge_statement):
        set_statement = ""
        columns_statement = ""
        value_count_stament = ""
        for key, value in list(reuqest_data.items()):
            set_statement = set_statement + f"i.{key} = '{value}', "
            columns_statement = columns_statement + f"{key}, "
            value_count_stament = value_count_stament + f"'{value}', "
        merge_statement = merge_statement.format(reuqest_data["hr_id"], set_statement[:-2], columns_statement[:-2], value_count_stament[:-2])
        return merge_statement

    def getSelectData(self, read_query, snowflake_connection):
        while True:
            try:
                curr = snowflake_connection.cursor(DictCursor)
                results = curr.execute(read_query).fetchall()
                break
            except:
                snowflake_connection = SnowflakeConnetion().getConnection()
        return results




    
