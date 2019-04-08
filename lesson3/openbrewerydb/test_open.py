import json

import pytest
from open_api import OpenAPI

state = ["California", "New York", "Alaska", "Colorado"]
name = ["cooper", "mad"]
ids = [11, 131, 454]
page_and_per_page = [(2, 30)]


@pytest.fixture(params=state)
def get_next_state(request):
    print("Next state is {}".format(request.param))
    return request.param


@pytest.fixture(params=name)
def get_next_name(request):
    print("Next name is {}".format(request.param))
    return request.param


@pytest.fixture(params=ids)
def get_next_id(request):
    print("Next id is {}".format(request.param))
    return request.param


@pytest.fixture(params=page_and_per_page)
def get_next_pair(request):
    print("Next pair is {} {}".format(request.param[0], request.param[1]))
    return request.param[0], request.param[1]


@pytest.mark.usefixtures("get_next_pair")
def test_page_and_per_page(get_next_pair):
    page = get_next_pair[0]
    per_page = get_next_pair[1]
    response = OpenAPI.get_pagination_and_per_page(page, per_page)
    result = json.loads(response)
    assert len(result) == per_page


@pytest.mark.usefixtures("get_next_id")
def test_get_by_id(get_next_id):
    response = OpenAPI.get_by_id(get_next_id)
    result = json.loads(response)
    assert result.get("id", None) == get_next_id


@pytest.mark.usefixtures("get_next_state")
def test_get_by_state(get_next_state):
    response = OpenAPI.get_by_state(get_next_state)
    result = json.loads(response)
    for item in result:
        if get_next_state not in item.get("state", None):
            assert False
    assert True


@pytest.mark.usefixtures("get_next_name")
def test_get_by_name(get_next_name):
    response = OpenAPI.get_by_name(get_next_name)
    result = json.loads(response)
    for item in result:
        if get_next_name not in item.get("name", None).lower():
            assert False
    assert True
