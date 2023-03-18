# (rule:location_code::varchar = '1003' or rule:location_code::varchar = 'NULL' or rule:location_code::varchar is null)

response_attributes = ["items"]

value = [{'ACCESS_DATA': '2'}, {'ACCESS_DATA': '3'}]

def getMVReadResponse(response_attributes, raw_response_data):
    for item in range(len(raw_response_data)):
        raw_response_data[item] = {k.lower(): v for k, v in raw_response_data[item].items()}
        print(raw_response_data[item])
    response = {response_attributes[0]: raw_response_data}
    return response

print(getMVReadResponse(response_attributes, value))
