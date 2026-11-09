#!/usr/bin/python3
"""Defines print_square, which prints a square of # characters."""


def print_square(size):
    """Print a square of side size made of #.

    Raises:
        TypeError: If size is not an integer (including negative floats).
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int) or isinstance(size, bool):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
