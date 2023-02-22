    # def generateUserId(self, redis_client, first_name, middle_name, last_name, query, logger):

    #     if username_generator_config["username_generator"][0] == "firstinitial-lastname-number":
    #         if len(first_name) > 0:
    #             first_initial = first_name[0:1]
    #             user_name_format = f"{first_initial}{last_name}"
    #         else: 
    #             user_name_format = f"{last_name}"
    #         while True:
    #             try:
    #                 curr = snowflake_connection.cursor(DictCursor)
    #                 result = curr.execute(query.format(user_name_format)).fetchall()
    #                 if result[0]["USER_ID_COUNT"] > 0:
    #                     number = result[0]["USER_ID_COUNT"]
    #                 else:
    #                     number = ""
    #                 user_id = f"{user_name_format}{number}"
    #                 break
    #             except:
    #                 snowflake_connection = SnowflakeConnetion().getConnection(logger)

    #     if username_generator_config["username_generator"][0] == "random":
    #         while True:
    #             try:
    #                 curr = snowflake_connection.cursor(DictCursor)
    #                 user_id = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(username_generator_config["username_generator"][1]))
    #                 result = curr.execute(query.format(user_id)).fetchone()
    #                 if result[0]["USER_ID_COUNT"] == 0:
    #                     break
    #             except:
    #                 snowflake_connection = SnowflakeConnetion().getConnection(logger)


    #     if username_generator_config["username_generator"][0] == "firstname-middleinitial-lastname-number":
    #         if len(middle_name) > 0 :
    #             middle_initial = middle_name[0:1]
    #             user_name_format = f"{first_name}.{middle_initial}.{last_name}"
    #         else: 
    #             user_name_format = f"{first_name}.{last_name}"
    #         while True:
    #             try:
    #                 curr = snowflake_connection.cursor(DictCursor)
    #                 result = curr.execute(query.format(user_name_format)).fetchall()
    #                 if result[0]["USER_ID_COUNT"] > 0:
    #                     number = str(result[0]["USER_ID_COUNT"])
    #                 else:
    #                     number = ""
    #                 user_id = f"{user_name_format}{number}"
    #                 break
    #             except:
    #                 snowflake_connection = SnowflakeConnetion().getConnection(logger)
        
    #     return user_id