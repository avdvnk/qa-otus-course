import json
import pytest

from lesson32.dog.dog_api import DogAPI


def test_random_image():
    response = DogAPI.get_random_image()
    result = json.loads(response.text)
    assert result.get("status", None) == "success"


@pytest.mark.usefixtures("get_next_breed")
def test_random_breed_image(get_next_breed):
    response = DogAPI.get_random_image_from_breed(get_next_breed)
    result = json.loads(response.text)
    assert result.get("status", None) == "success"


@pytest.mark.usefixtures("get_next_count")
def test_random_count_images(get_next_count):
    response = DogAPI.get_multiply_random_image(get_next_count)
    result = json.loads(response.text)
    assert result.get("status", None) == "success" and len(result.get("message")) == get_next_count


@pytest.mark.usefixtures("get_next_pair")
def test_random_multiply_breed_images(get_next_pair):
    response = DogAPI.get_multiply_images_from_breed(get_next_pair[0], get_next_pair[1])
    result = json.loads(response.text)
    assert result.get("status", None) == "success" and len(result.get("message")) == get_next_pair[1]


@pytest.mark.usefixtures("get_next_sub_breed_list")
def test_sub_breed_list(get_next_sub_breed_list):
    dictionary = get_next_sub_breed_list[1].get(get_next_sub_breed_list[0], None)
    response = DogAPI.get_sub_breeds(get_next_sub_breed_list[0])
    result = json.loads(response.text)
    assert len(dictionary) == len(result.get("message", None))
