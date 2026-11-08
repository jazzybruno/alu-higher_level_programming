#!/usr/bin/python3
"""Defines MyList, a list subclass that can print itself sorted."""


class MyList(list):
    """A list that can print its elements in ascending order."""

    def print_sorted(self):
        """Print the list sorted in ascending order without changing it."""
        print(sorted(self))
