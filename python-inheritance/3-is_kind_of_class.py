#!/usr/bin/python3
"""Defines a function that checks instance or subclass-instance status."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or of a subclass."""
    return isinstance(obj, a_class)
