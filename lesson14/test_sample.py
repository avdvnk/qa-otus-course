from lesson14.functions import Test


def test_concatenate_strings():
    assert Test.concatenate_strings('aaa', 'bbb') == 'aaabbb'


def test_square_number():
    assert Test.square_number(4) == 16


def test_is_positive_int():
    assert Test.is_positive_int(14) is True


def test_even_number():
    assert Test.even_number(15) is False


def test_exist_key():
    dictionary = {
        'hp': '110',
        'mp': '50',
        'exp': '112',
    }
    assert Test.exist_key(dictionary, 'mp') is True


def test_length_array():
    array = [1, 2, 3, 4, 10]
    assert Test.length_array(array) == 5


def test_to_upper():
    string = 'hello, world'
    result = Test.to_upper(string)
    assert result.isupper()


def test_sum_of_couple():
    value = (2, 4, 4)
    assert Test.sum_of_couple(value) == 10


def test_min_element():
    array = [10, 6, 3, 8, 15]
    assert Test.min_element(array) == 3


def test_last_symbol_in_string():
    string = 'Hello, World!'
    assert Test.last_symbol_in_string(string) == '!'
