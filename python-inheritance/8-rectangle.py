#!/usr/bin/python3
"""Defines a Rectangle built on BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle with a validated private width and height."""

    def __init__(self, width, height):
        """Initialize the rectangle after validating both sides.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
