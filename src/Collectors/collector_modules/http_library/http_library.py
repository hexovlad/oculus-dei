import json
import requests


class HttpRequest:
    def __init__(self, endpoint: str):
        """Constructor"""
        self.__endpoint = endpoint

    @staticmethod
    def __make_headers(header_type: dict = None):
        """Makes the headers for the requests"""
        match header_type:
            case None:
                return {"user-agent": "curl/7.74.0", "accept": "*/*"}

            case "connect":
                return {"user-agent": "application/x-www-form-urlencoded"}

    @staticmethod
    def make_payload(secret: str or dict = None, payload_type: str = None):
        """Creates and returns the payload"""

        match payload_type:
            case None:
                return {}

            case "connect":
                payload = (
                )
                return payload

    # request_data = Union[str, dict, None]  # Making a union for the data

    def do_get(self, data: str or dict, header: dict = None):
        """Does an HTTP GET request to the specified endpoint"""

        headers = None
        match header:
            case None:
                """In case there are no headers, we create them with our private method"""
                headers = self.__make_headers()
            case _:
                headers = header

        if data:
            req = requests.get(self.__endpoint, headers=headers, data=json.dumps(data))
        else:
            req = requests.get(self.__endpoint, headers=headers, data=None)

        try:
            req.raise_for_status()
        except Exception as e:
            print(e)
            return None

        return req

    def do_post(self, data: str or dict, header: dict = None):
        """Does an HTTP POST request to the specified endpoint"""

        headers = None
        match header:
            case None:
                """In case there are no headers, we create them with our private method"""
                headers = self.__make_headers()
            case _:
                headers = header

        if data:
            req = requests.post(self.__endpoint, headers=headers, data=json.dumps(data))
        else:
            req = requests.post(self.__endpoint, headers=headers, data=None)

        try:
            req.raise_for_status()
        except Exception as e:
            print(e)
            return None

        return req

    def do_delete(self, data: str or dict, header: dict = None):
        """Does an HTTP DELETE request to the specified endpoint"""
        headers = None
        match header:
            case None:
                """In case there are no headers, we create them with our private method"""
                headers = self.__make_headers()
            case _:
                headers = header

        if data:
            req = requests.delete(
                self.__endpoint, headers=headers, data=json.dumps(data)
            )
        else:
            req = requests.delete(self.__endpoint, headers=headers, data=None)

        try:
            req.raise_for_status()
        except Exception as e:
            print(e)
            return None

        return req
