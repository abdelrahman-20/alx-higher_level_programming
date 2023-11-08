#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
		
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    result = 0
    value = 0

    for char in reversed(roman_string):
        value += roman_values[char]
        result += value if result < value * 5 else -value

    return (result)
