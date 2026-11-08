#!/usr/bin/python3
"""Defines BaseGeometry with an unimplemented area method."""


class BaseGeometry:
    """Base class for geometry shapes."""

    def area(self):
        """Raise an Exception because subclasses must implement area."""
        raise Exception("area() is not implemented")
