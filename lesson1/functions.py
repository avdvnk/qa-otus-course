class Test:

    @staticmethod
    def concatenate_strings(first_str, second_str):
        """ Two-line concatenation method """
        return first_str + second_str

    @staticmethod
    def square_number(value):
        """ Squaring method """
        return value ** 2

    @staticmethod
    def is_positive_int(value):
        """ Positive number check method """
        if value > 0:
            return True
        return False

    @staticmethod
    def even_number(value):
        """ Parity check method """
        if value % 2 == 0:
            return True
        return False

    @staticmethod
    def exist_key(dictionary, key):
        """ Key verification method in the dictionary """
        if dictionary.get(key):
            return True
        return False

    @staticmethod
    def length_array(array):
        """ Array size calculation method """
        return len(array)

    @staticmethod
    def to_upper(string):
        """ Method to convert a string to uppercase characters """
        return string.upper()

    @staticmethod
    def sum_of_couple(couple):
        """ Couple sum calculation method """
        result = 0
        for value in couple:
            result += value
        return result

    @staticmethod
    def min_element(array):
        """ Finding the minimum element of an array """
        min_value = array[0]
        for value in array:
            if value < min_value:
                min_value = value
        return min_value

    @staticmethod
    def last_symbol_in_string(string):
        """ Getting the last character in a string """
        return string[-1]
