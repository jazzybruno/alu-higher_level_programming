#!/usr/bin/python3
"""Defines a Square built on Rectangle, with its own str."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square with a validated private size."""

    def __init__(self, size):
        """Initialize the square after validating its size.

        Args:
            size (int): The length of one side.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Return the description [Square] <width>/<height>."""
        return "[Square] {}/{}".format(self.__size, self.__size)
