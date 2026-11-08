#!/usr/bin/python3
"""Defines a function that inserts text after matching lines of a file."""


def append_after(filename="", search_string="", new_string=""):
    """Insert new_string after every line that contains search_string."""
    with open(filename, encoding="utf-8") as f:
        lines = f.readlines()
    with open(filename, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
