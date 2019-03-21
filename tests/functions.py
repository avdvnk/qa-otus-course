

class Test:
    def __init__(self):
        pass

    @staticmethod
    def concatenate_strings(first_str, second_str):
        return first_str + second_str

    @staticmethod
    def square_number(value):
        return value ^ 2

    @staticmethod
    def is_positive_int(value):
        if value > 0:
            return True
        return False

    @staticmethod
    def even_number(value):
        if value % 2 == 0:
            return True
        return False

    @staticmethod
    def exist_key(dictionary, key):
        if dictionary.get(key):
            return True
        return False

    @staticmethod
    def length_array(array):
        return len(array)

    @staticmethod
    def to_upper(string):
        return string.upper()

    @staticmethod
    def sum_of_couple(couple):
        result = 0
        for value in couple:
            result += value
        return result

    @staticmethod
    def min_element(array):
        min_value = array[0]
        for value in array:
            if value < min_value:
                min_value = value
        return min_value

    @staticmethod
    def last_symbol_in_string(string):
        return string[-1]
