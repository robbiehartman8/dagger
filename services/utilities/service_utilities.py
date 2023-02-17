# this file contains general utilities for the services

class ServiceUtilities:

    def getResponse(self, response_attributes, raw_response_data):
        response = {}
        raw_response_data = {k.lower(): v for k, v in raw_response_data.items()}
        for key in response_attributes:
            try:
                response[key] = raw_response_data[key]
            except: 
                response[key] = ""
        return response