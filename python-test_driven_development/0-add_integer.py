#!/usr/bin/python3
"""Defines add_integer, which adds two numbers as integers.

Floats are cast to integers before the addition; anything that is not an
int or a float raises a TypeError.
"""


def add_integer(a, b=98):
    """Return the integer sum of a and b.

    Raises TypeError if a or b is not an int or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
