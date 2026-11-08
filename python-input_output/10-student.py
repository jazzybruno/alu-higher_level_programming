#!/usr/bin/python3
"""Defines a Student class that can describe itself as a filtered dict."""


class Student:
    """Represents a student with a first name, last name and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize the student.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the student's attributes as a dict.

        Args:
            attrs (list): If a list of strings, only these attributes are
                returned; otherwise every attribute is returned.
        """
        if (isinstance(attrs, list) and
                all(isinstance(name, str) for name in attrs)):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__
