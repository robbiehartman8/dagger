# this file helps construct queries for the services

class QueryUtil:

    def getSelectQuery(self, attribute_list):
        select = ""
        for attribute in attribute_list:
            select = select + f"{attribute}::string as {attribute.replace(':', '_')},"
        return select[:-1]