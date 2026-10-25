#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    for i, ch in enumerate(roman_string):
        value = values.get(ch, 0)
        following = values.get(roman_string[i + 1], 0) \
            if i + 1 < len(roman_string) else 0
        total += -value if value < following else value
    return total
