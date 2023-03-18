import birthright_constants as con

class BirthrightUtilities:
    
    def getBirthrightSelect(self, identity_response):
        where_list = []
        for column, value in identity_response.items():
            where_list.append(con.get_access_where_clause.format(column, value))
        return con.get_access_select_query.format(" and ".join([str(item) for item in where_list]))

