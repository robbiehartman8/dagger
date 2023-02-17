d = {"identity_id": "some shit", "hr_id": "some shit", "not here": "some shit"}

sql_data = {"identity_id": "data", "hr_id": "data", "not there": "data"}

keys_list = list(d.keys())

response = {}


for i in keys_list:
    try:
        response[i] = sql_data[i.lower()]
    except: 
        response[i] = "data"

print(response)