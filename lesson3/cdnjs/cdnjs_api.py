import requests

api = "https://api.cdnjs.com/libraries"


class CdnjsAPI:
    @staticmethod
    def __send_command(method, url):
        print("Send " + url)
        response = method(url)
        print("Response: {} {}".format(response.status_code, response.reason))
        return response.text

    @staticmethod
    def get_all_libs():
        url = "{}".format(api)
        response = CdnjsAPI.__send_command(requests.get, url)
        return response

    @staticmethod
    def get_all_libs_readable():
        url = "{}?output=human".format(api)
        response = CdnjsAPI.__send_command(requests.get, url)
        return response

    @staticmethod
    def get_by_search(input_string):
        url = "{}?search={}".format(api, input_string)
        response = CdnjsAPI.__send_command(requests.get, url)
        return response

    @staticmethod
    def get_by_search_with_fields(input_string, fields):
        url = "{}?search={}&fields=".format(api, str(input_string))
        for field in fields:
            url += "{},".format(str(field))
        url = url[:-1]
        response = CdnjsAPI.__send_command(requests.get, url)
        return response
