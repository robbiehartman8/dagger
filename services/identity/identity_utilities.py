# this file contains utilities for the identity services
import sys
sys.path.insert(1, "/Users/roberthartman/Desktop/repos/dagger/services/utilities")

from snowflake.connector import DictCursor
import random
import string
from config_utilities import username_generator_config
from redis_utilities import RedisUtilities
import re

class IdentityUtilities:

    def cleanName(self, name_list):
        # change to have special characters later
        for index in range(len(name_list)):
            name = name_list[index].strip().lower()
            name = re.sub(r'[^a-zA-Z0-9]', '', name)
            name_list[index] = name

        return name_list[0:3], name_list[3:]

    def getUserId(self, redis_client, identity_id, first_name, middle_name, last_name, logger):

        if username_generator_config["username_generator"][0] == "firstname-middleinitial-lastname-number":
            if len(middle_name) > 0:
                middle_initial = middle_name[0:1]
                user_name_format = f"{first_name}.{middle_initial}.{last_name}"
            else: 
                user_name_format = f"{first_name}.{last_name}"
            number = 0
            RedisUtilities().getRedisLock(redis_client, "grpc-username", 5)
            user_id = redis_client.get(f"identity/{identity_id}")
            if user_id is None:
                while True:
                    if number != 0:
                        user_id = f"{user_name_format}{number}"
                    else:
                        user_id = f"{user_name_format}"

                    if redis_client.get(f"user_id/{user_id}") is not None:
                        pass
                    else:
                        redis_client.set(f"user_id/{user_id}", 1)
                        redis_client.set(f"identity/{identity_id}", user_id)
                        break
                    number += 1
            redis_client.delete("grpc-username")
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
