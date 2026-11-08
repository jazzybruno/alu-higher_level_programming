#!/usr/bin/python3
"""Defines a function that lists the attributes and methods of an object."""


def lookup(obj):
    """Return the list of attributes and methods available on obj."""
    return dir(obj)
