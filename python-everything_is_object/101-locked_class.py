#!/usr/bin/python3
"""Defines LockedClass, which only accepts a first_name attribute."""


class LockedClass:
    """Prevents new instance attributes other than first_name."""

    __slots__ = ["first_name"]
