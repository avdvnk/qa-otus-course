import requests

api = "https://dog.ceo/api"


class DogAPI:
    @staticmethod
    def __send_command(method, url):
        print("Send " + url)
        response = method(url)
        print("Response: {} {}".format(response.status_code, response.reason))
        return response.text

    @staticmethod
    def get_random_image():
        url = "{}/breeds/image/random".format(api)
        response = DogAPI.__send_command(requests.get, url)
        return response

    @staticmethod
    def get_multiply_random_image(count="1"):
        url = "{}/breeds/image/random/{}".format(api, count)
        response = DogAPI.__send_command(requests.get, url)
        return response

    @staticmethod
    def get_random_image_from_breed(breed):
        url = "{}/breed/{}/images/random".format(api, breed)
        response = DogAPI.__send_command(requests.get, url)
        return response

    @staticmethod
    def get_multiply_images_from_breed(breed, count=1):
        url = "{}/breed/{}/images/random/{}".format(api, breed, count)
        response = DogAPI.__send_command(requests.get, url)
        return response

    @staticmethod
    def get_sub_breeds(breed):
        url = "{}/breed/{}/list".format(api, breed)
        response = DogAPI.__send_command(requests.get, url)
        return response
