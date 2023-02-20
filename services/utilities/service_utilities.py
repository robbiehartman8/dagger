# this file contains general utilities for the services

import hashlib

class ServiceUtilities:

    def getReadResponse(self, response_attributes, raw_response_data):
        response = {}
        raw_response_data = {k.lower(): v for k, v in raw_response_data.items()}
        for key in response_attributes:
            try:
                response[key] = raw_response_data[key]
            except: 
                response[key] = ""
        return response

    def getCreateUpdateResponse(self, message, attributes, request_data):
        response = {}
        for attribute in attributes:
            response[attribute] = request_data[attribute]
        response["status_message"] = message
        return response

    def cleanCreateUpdateRequest(self, reuqest_data):
        for key, value in list(reuqest_data.items()):
            if value == "":
                del data[key]
        return reuqest_data

    def getID(self, table, value):
        concat = table.strip() + value.strip()
        md5 = hashlib.md5(concat.encode()).hexdigest()
        return md5