import json

import pytest
from dog_api import DogAPI

breeds = ["akita", "beagle", "cairn", "chow", "pug", "retriever"]
count = [1, 2, 5, 3]
pairs = [(breed, counter) for breed in breeds for counter in count]
sub_breeds = [{"retriever": ["chesapeake", "curly", "flatcoated", "golden"]},
              {"beagle": []},
              {"akita": []},
              {"pug": []},
              {"cairn": [],
               "chow": []}
              ]


@pytest.fixture(params=breeds)
def get_next_breed(request):
    print("Next breed is ".format(request.param))
    return request.param


@pytest.fixture(params=count)
def get_next_count(request):
    print("Next count is ".format(request.param))
    return request.param


@pytest.fixture(params=pairs)
def get_next_pair(request):
    print("Next pair is {} : {}".format(request.param[0], request.param[1]))
    return request.param[0], request.param[1]


@pytest.fixture(params=sub_breeds)
def get_next_sub_breed_list(request):
    breed = next(iter(request.param))
    print("Next sub-breed list ".format(breed))
    return breed, request.param


def test_random_image():
    response = DogAPI.get_random_image()
    result = json.loads(response)
    assert result.get("status", None) == "success"


@pytest.mark.usefixtures("get_next_breed")
def test_random_breed_image(get_next_breed):
    response = DogAPI.get_random_image_from_breed(get_next_breed)
    result = json.loads(response)
    assert result.get("status", None) == "success"


@pytest.mark.usefixtures("get_next_count")
def test_random_count_images(get_next_count):
    response = DogAPI.get_multiply_random_image(get_next_count)
    result = json.loads(response)
    assert result.get("status", None) == "success" and len(result.get("message")) == get_next_count


@pytest.mark.usefixtures("get_next_pair")
def test_random_multiply_breed_images(get_next_pair):
    response = DogAPI.get_multiply_images_from_breed(get_next_pair[0], get_next_pair[1])
    result = json.loads(response)
    assert result.get("status", None) == "success" and len(result.get("message")) == get_next_pair[1]


@pytest.mark.usefixtures("get_next_sub_breed_list")
def test_sub_breed_list(get_next_sub_breed_list):
    dictionary = get_next_sub_breed_list[1].get(get_next_sub_breed_list[0], None)
    response = DogAPI.get_sub_breeds(get_next_sub_breed_list[0])
    result = json.loads(response)
    assert len(dictionary) == len(result.get("message", None))
