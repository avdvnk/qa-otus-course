import pytest

breeds = ["akita"]
count = [1]
pairs = [(breed, counter) for breed in breeds for counter in count]
sub_breeds = [{"retriever": ["chesapeake", "curly", "flatcoated", "golden"]}]


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
