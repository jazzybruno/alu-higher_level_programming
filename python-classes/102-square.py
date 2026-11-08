#!/usr/bin/python3
"""Defines a Square class that compares squares by area."""


class Square:
    """Represents a square that supports comparison operators."""

    def __init__(self, size=0):
        """Initialize the square.

        Args:
            size (int or float): The length of one side of the square.
        """
        self.size = size

    @property
    def size(self):
        """Get or set the size of the square, validating new values."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size after checking it is a non-negative number."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Return True if both squares have the same area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Return True if the squares have different areas."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Return True if this square's area is smaller."""
        return self.area() < other.area()

    def __le__(self, other):
        """Return True if this square's area is smaller or equal."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Return True if this square's area is larger."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Return True if this square's area is larger or equal."""
        return self.area() >= other.area()
