#!/usr/bin/python3
"""Defines a Square class with a private size."""


class Square:
    """Represents a square defined by its size."""

    def __init__(self, size):
        """Initialize the square.

        Args:
            size: The length of one side of the square.
        """
        self.__size = size
