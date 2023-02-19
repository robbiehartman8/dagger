# this file contains utilities for the identity services

from snowflake_connection_utilities import SnowflakeConnetion
from snowflake.connector import DictCursor
import random
import string
from config_utilities import username_generator_config
import re

class IdentityUtilities:

    def getUserId(self, snowflake_connection, first_name, middle_name, last_name, query):
        
        first_name = first_name.strip().lower()
        first_name = re.sub(r'[^a-zA-Z0-9]', '', first_name)
        middle_name = middle_name.strip().lower()
        middle_name = re.sub(r'[^a-zA-Z0-9]', '', middle_name)
        last_name = last_name.strip().lower()
        last_name = re.sub(r'[^a-zA-Z0-9]', '', last_name)

        print(first_name, middle_name, last_name)

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

        