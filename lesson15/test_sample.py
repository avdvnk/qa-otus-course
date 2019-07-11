import allure

from lesson15.functions import Test


@allure.story("epic_1")
def test_concatenate_strings():
    assert Test.concatenate_strings('aaa', 'bbb') == 'aaabbb'


@allure.story("epic_1")
def test_square_number():
    assert Test.square_number(4) == 16


@allure.story("epic_1")
def test_is_positive_int():
    assert Test.is_positive_int(14) is True


@allure.story("epic_1")
def test_even_number():
    assert Test.even_number(15) is False


@allure.story("epic_1")
def test_exist_key():
    dictionary = {
        'hp': '110',
        'mp': '50',
        'exp': '112',
    }
    assert Test.exist_key(dictionary, 'mp') is True


@allure.story("epic_1")
def test_length_array():
    array = [1, 2, 3, 4, 10]
    assert Test.length_array(array) == 5


@allure.story("epic_2")
def test_to_upper():
    string = 'hello, world'
    result = Test.to_upper(string)
    assert result.isupper()


@allure.story("epic_2")
def test_sum_of_couple():
    value = (2, 4, 4)
    assert Test.sum_of_couple(value) == 10


@allure.story("epic_2")
def test_min_element():
    array = [10, 6, 3, 8, 15]
    assert Test.min_element(array) == 3


@allure.story("epic_2")
def test_last_symbol_in_string():
    string = 'Hello, World!'
    assert Test.last_symbol_in_string(string) == '!'
