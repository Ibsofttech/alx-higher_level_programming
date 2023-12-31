#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_numerals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    result = 0
    prev_value = 0

    for i in range(len(roman_string) - 1, -1, -1):
        value = roman_numerals.get(roman_string[i])
        if value < prev_value:
            result -= value
        else:
            result += value
        prev_value = value

    return result
