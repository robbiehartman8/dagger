# this file contains utilities for the identity services

from snowflake_connection_utilities import SnowflakeConnetion
from snowflake.connector import DictCursor
import random
import string
from config_utilities import username_generator_config
import re

class IdentityUtilities:

    def cleanName(self, name_list):
        # change to have special characters later
        for index in range(len(name_list)):
            name = name_list[index].strip().lower()
            name = re.sub(r'[^a-zA-Z0-9]', '', name)
            name_list[index] = name

        return name_list[0:3], name_list[3:]

    def getUserId(self, snowflake_connection, first_name, middle_name, last_name, query):

        if username_generator_config["username_generator"][0] == "firstinitial-lastname-number":
            if len(first_name) > 0 and first_name.isalnum():
                first_initial = first_name[0:1]
                user_name_format = f"{first_initial}{last_name}"
            else: 
                user_name_format = f"{last_name}"
            while True:
                try:
                    curr = conn.cursor(DictCursor)
                    result = curr.execute(query.format(user_name_format)).fetchall()
                    if result[0]["USER_ID_COUNT"] > 0:
                        number = result[0]["USER_ID_COUNT"]
                    else:
                        number = ""
                    user_id = f"{user_name_format}{number}"
                    break
                except:
                    conn = SnowflakeConnetion().getConnection()

        if username_generator_config["username_generator"][0] == "random":
            while True:
                try:
                    curr = conn.cursor(DictCursor)
                    user_id = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(username_generator_config["username_generator"][1]))
                    result = curr.execute(query.format(user_id)).fetchone()
                    if result[0]["USER_ID_COUNT"] == 0:
                        break
                except:
                    conn = SnowflakeConnetion().getConnection()


        if username_generator_config["username_generator"][0] == "firstname-middleinitial-lastname-number":
            if len(middle_name) > 0 and middle_name.isalnum():
                middle_initial = middle_name[0:1]
                user_name_format = f"{first_name}.{middle_initial}.{last_name}"
            else: 
                user_name_format = f"{first_name}.{last_name}"
            while True:
                try:
                    curr = conn.cursor(DictCursor)
                    result = curr.execute(query.format(user_name_format)).fetchall()
                    if result[0]["USER_ID_COUNT"] > 0:
                        number = str(result[0]["USER_ID_COUNT"])
                    else:
                        number = ""
                    user_id = f"{user_name_format}{number}"
                    break
                except:
                    conn = SnowflakeConnetion().getConnection()
        
        return user_id

    def checkNameStatus(self, legal_name_list, preferred_name_list):
        name_status = False
        for i in zip(legal_name_list, preferred_name_list):
            if i[0] != i[1]:
                name_status = True
                break
        if name_status is True:
            return name_status, preferred_name_list
        else:
            return name_status, legal_name_list
