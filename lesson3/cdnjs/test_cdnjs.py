import json

import pytest
from cdnjs_api import CdnjsAPI

search_examples = ["reactive", "jquery", "1140", "16pixels"]
special_fields = [["description", "homepage", "keywords", "license", "repository", "autoupdate", "author", "assets", "version"],
                  ]
pairs = [(example, field) for example in search_examples for field in special_fields]


@pytest.fixture(params=search_examples)
def get_next_example(request):
    print("Next example is {}".format(request))
    return request.param


@pytest.fixture(params=pairs)
def get_next_pair(request):
    print("Next fields {}".format(request))
    return request.param[0], request.param[1]


def test_get_all_libs():
    response = CdnjsAPI.get_all_libs()
    result = json.loads(response)
    assert result.get("results", None) is not None


@pytest.mark.usefixtures("get_next_example")
def test_get_by_search(get_next_example):
    response = CdnjsAPI.get_by_search(get_next_example)
    result = json.loads(response)
    array = result.get("results", None)
    for item in array:
        if item.get("name", None) is None:
            assert False
    assert True


@pytest.mark.usefixtures("get_next_pair")
def test_get_by_search_with_fields(get_next_pair):
    search_name = get_next_pair[0]
    search_fields = get_next_pair[1]
    response = CdnjsAPI.get_by_search_with_fields(search_name, search_fields)
    result = json.loads(response)
    assert result.get("results") is not None
