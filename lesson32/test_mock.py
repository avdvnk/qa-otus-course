import json
from unittest.mock import patch

import pytest

from lesson32.dog.dog_api import DogAPI


def test_random_image():
    with patch("dog.dog_api.requests.get") as mock_get:
        mock_get.return_value.text = '{"message":"https:\\/\\/images.dog.ceo\\/breeds\\/terrier-lakeland' \
                                     '\\/n02095570_889.jpg", "status":"success"}'
        response = DogAPI.get_random_image()
        result = json.loads(response.text)
        assert result.get("status", None) == "success"


@pytest.mark.usefixtures("get_next_breed")
def test_random_breed_image(get_next_breed):
    with patch("dog.dog_api.requests.get") as mock_get:
        mock_get.return_value.text = '{"message":"https:\\/\\/images.dog.ceo\\/breeds\\/akita\\/Akita_Dog.jpg",' \
                                     '"status":"success"} '
        response = DogAPI.get_random_image_from_breed(get_next_breed)
        result = json.loads(response.text)
        assert result.get("status", None) == "success"


@pytest.mark.usefixtures("get_next_count")
def test_random_count_images(get_next_count):
    with patch("dog.dog_api.requests.get") as mock_get:
        mock_get.return_value.text = '{"message":["https:\\/\\/images.dog.ceo\\/breeds\\/chow\\/n02112137_2220.jpg"],' \
                                     '"status":"success"} '
        response = DogAPI.get_multiply_random_image(get_next_count)
        result = json.loads(response.text)
        assert result.get("status", None) == "success" and len(result.get("message")) == get_next_count


@pytest.mark.usefixtures("get_next_pair")
def test_random_multiply_breed_images(get_next_pair):
    with patch("dog.dog_api.requests.get") as mock_get:
        mock_get.return_value.text = '{"message":["https:\\/\\/images.dog.ceo\\/breeds\\/akita\\/Japaneseakita.jpg"],' \
                                     '"status":"success"} '
        response = DogAPI.get_multiply_images_from_breed(get_next_pair[0], get_next_pair[1])
        result = json.loads(response.text)
        assert result.get("status", None) == "success" and len(result.get("message")) == get_next_pair[1]


@pytest.mark.usefixtures("get_next_sub_breed_list")
def test_sub_breed_list(get_next_sub_breed_list):
    with patch("dog.dog_api.requests.get") as mock_get:
        mock_get.return_value.text = '{"message":["chesapeake","curly","flatcoated","golden"],"status":"success"}'
        dictionary = get_next_sub_breed_list[1].get(get_next_sub_breed_list[0], None)
        response = DogAPI.get_sub_breeds(get_next_sub_breed_list[0])
        result = json.loads(response.text)
        assert len(dictionary) == len(result.get("message", None))
