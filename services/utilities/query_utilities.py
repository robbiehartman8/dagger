# this file helps construct queries for the services

from snowflake_connection_utilities import SnowflakeConnetion
from snowflake.connector import DictCursor

class QueryUtilities:

    def createSelectStatement(self, attribute_list):
        select = ""
        for attribute in attribute_list:
            select = select + f"{attribute}::string as {attribute.replace(':', '_')},"
        return select[:-1]

    def createMergeStatement(self, reuqest_data, merge_statement):
        set_statement = ""
        columns_statement = ""
        value_count_stament = ""
        for key, value in list(reuqest_data.items()):
            if value is None:
                set_statement = set_statement + f"i.{key} = NULL, "
                value_count_stament = value_count_stament + "NULL, "
            else:
                set_statement = set_statement + f"i.{key} = '{value}', "
                value_count_stament = value_count_stament + f"'{value}', "
            columns_statement = columns_statement + f"{key}, "
        merge_statement = merge_statement.format(reuqest_data["hr_id"], set_statement[:-2], columns_statement[:-2], value_count_stament[:-2])
        return merge_statement

    def executeSelect(self, select_statement, snowflake_connection, logger):
        while True:
            try:
                curr = snowflake_connection.cursor(DictCursor)
                results = curr.execute(select_statement).fetchall()
                break
            except:
                snowflake_connection = SnowflakeConnetion().getConnection(logger)
        return results

    def executeMerge(self, merge_statement, snowflake_connection, logger):
        while True:
            try:
                curr = snowflake_connection.cursor()
                curr.execute(merge_statement)
                break
            except:
                snowflake_connection = SnowflakeConnetion().getConnection(logger)




    
