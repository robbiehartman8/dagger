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
            response[attribute] = request_data[attribute]
        response["status_message"] = message
        return response

    def getID(self, table, value):
        concat = table.strip() + value.strip()
        md5 = hashlib.md5(concat.encode()).hexdigest()
        return md5