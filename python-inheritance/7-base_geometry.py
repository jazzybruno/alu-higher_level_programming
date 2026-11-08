#!/usr/bin/python3
"""Defines BaseGeometry with area and integer validation."""


class BaseGeometry:
    """Base class for geometry shapes."""

    def area(self):
        """Raise an Exception because subclasses must implement area."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Check that value is a positive integer.

        Args:
            name (str): The name used in error messages.
            value: The value to validate.

        Raises:
            TypeError: If value is not an integer (booleans are rejected).
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
