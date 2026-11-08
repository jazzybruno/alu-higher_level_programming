#!/usr/bin/python3
"""Defines a Square class with a size property."""


class Square:
    """Represents a square whose size is accessed through a property."""

    def __init__(self, size=0):
        """Initialize the square.

        Args:
            size (int): The length of one side of the square.
        """
        self.size = size

    @property
    def size(self):
        """Get or set the size of the square, validating new values."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size after checking it is a non-negative integer."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2
