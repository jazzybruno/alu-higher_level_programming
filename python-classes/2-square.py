#!/usr/bin/python3
"""Defines a Square class with a validated private size."""


class Square:
    """Represents a square defined by a validated size."""

    def __init__(self, size=0):
        """Initialize the square.

        Args:
            size (int): The length of one side of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
