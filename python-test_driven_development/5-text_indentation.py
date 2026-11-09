#!/usr/bin/python3
"""Defines text_indentation, which splits text after . ? and :"""


def text_indentation(text):
    """Print text with two new lines after each '.', '?' and ':'.

    Spaces at the start and end of every printed line are removed.
    Raises TypeError if text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    line = ""
    for char in text:
        line += char
        if char in ".?:":
            print(line.strip(" "), end="\n\n")
            line = ""
    print(line.strip(" "), end="")
