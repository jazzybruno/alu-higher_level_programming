#!/usr/bin/python3
"""Defines a function that checks for an instance of a strict subclass."""


def inherits_from(obj, a_class):
    """Return True if obj's class is a strict subclass of a_class."""
    return isinstance(obj, a_class) and type(obj) is not a_class
