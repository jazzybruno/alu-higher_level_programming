#!/usr/bin/python3
"""Defines a function that prints the content of a UTF-8 text file."""


def read_file(filename=""):
    """Print the content of filename to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
