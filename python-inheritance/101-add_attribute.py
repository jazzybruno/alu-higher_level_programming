#!/usr/bin/python3
"""Defines a function that adds an attribute to an object when possible."""


def add_attribute(obj, name, value):
    """Set obj.name to value.

    Raises:
        TypeError: If obj cannot hold new attributes.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
