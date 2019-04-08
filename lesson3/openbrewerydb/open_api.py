import requests

api = "https://api.openbrewerydb.org/breweries"


class OpenAPI:
    @staticmethod
    def __send_command(method, url):
        print("Send " + url)
        response = method(url)
        print("Response: {} {}".format(response.status_code, response.reason))
        return response

    @staticmethod
    def get_by_state(state):
        url = "{}?by_state={}".format(api, state)
        response = OpenAPI.__send_command(requests.get, url)
        return response.text

    @staticmethod
    def get_by_name(name):
        url = "{}?by_name={}".format(api, name)
        response = OpenAPI.__send_command(requests.get, url)
        return response.text

    @staticmethod
    def get_by_id(input_id):
        url = "{}/{}".format(api, input_id)
        response = OpenAPI.__send_command(requests.get, url)
        return response.text

    @staticmethod
    def get_pagination_and_per_page(page, per_page):
        url = "{}?page={}&per_page={}".format(api, page, per_page)
        response = OpenAPI.__send_command(requests.get, url)
        return response.text
