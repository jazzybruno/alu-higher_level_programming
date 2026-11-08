#!/usr/bin/python3
"""Defines a Square class that prints the same way with print()."""


class Square:
    """Represents a square with a size and an offset position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square.

        Args:
            size (int): The length of one side of the square.
            position (tuple): Horizontal and vertical offset for printing.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get or set the position, a tuple of 2 positive integers."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position after checking it is a tuple of 2 ints >= 0."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(n, int) and n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Return the square drawn with #, offset by position."""
        if self.__size == 0:
            return ""
        row = " " * self.__position[0] + "#" * self.__size
        return "\n" * self.__position[1] + "\n".join([row] * self.__size)

    def my_print(self):
        """Print the square with #, offset by position, or an empty line."""
        print(self)
