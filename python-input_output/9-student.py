#!/usr/bin/python3
"""Defines a Student class that can describe itself as a dict."""


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

    def to_json(self):
        """Return the dictionary representation of the student."""
        return self.__dict__
