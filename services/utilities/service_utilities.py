# this file contains general utilities for the services

import hashlib
import json

class ServiceUtilities:

    def convertToDict(self, value):
        if "{" in value:
            return json.loads(value)
        else:
            return value

    def getReadResponse(self, response_attributes, raw_response_data):
        response = {}
        raw_response_data = {k.lower(): v for k, v in raw_response_data.items()}
        for key in response_attributes:
            try:
                response[key] = ServiceUtilities().convertToDict(raw_response_data[key])
            except: 
                response[key] = ""
        return response

    def getMVReadResponse(self, response_attributes, raw_response_data):
        for item in range(len(raw_response_data)):
            raw_response_data[item] = {k.lower(): v for k, v in raw_response_data[item].items()}
        response = {response_attributes[0]: raw_response_data}
        return response

    def cleanCreateUpdateRequest(self, request_data, request_attributes):
        for attribute in request_attributes:
            if attribute in request_data and request_data[attribute] == "":
                request_data[attribute] = None
            elif attribute in request_data and request_data[attribute] != "":
                pass
            else:
                request_data[attribute] = None
        return request_data

    def getCreateUpdateResponse(self, message, attributes, request_data):
        response = {}
        for attribute in attributes:
            if attribute == "status_message":
                response["status_message"] = message
            else:
                response[attribute] = request_data[attribute]
        return response

    def getTablePK(self, table, value):
        concat = table.strip().lower() + value.strip().lower()
        md5 = hashlib.md5(concat.encode()).hexdigest()
        return md5