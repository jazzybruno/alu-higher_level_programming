#!/usr/bin/python3
"""Defines MyInt, an int whose == and != operators are inverted."""


class MyInt(int):
    """An int that answers == with != and != with ==."""

    def __eq__(self, other):
        """Return True when the values differ."""
        return int(self) != other

    def __ne__(self, other):
        """Return True when the values are equal."""
        return int(self) == other
