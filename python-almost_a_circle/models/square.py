#!/usr/bin/python3
"""Defines the Square class, a Rectangle with equal sides."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """A square: a rectangle whose width and height are the same."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square of the given size and offset."""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get or set the size (width and height) of the square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Return [Square] (<id>) <x>/<y> - <size>."""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Assign attributes from positional args or else from kwargs."""
        names = ("id", "size", "x", "y")
        if args:
            for name, value in zip(names, args):
                setattr(self, name, value)
        else:
            for name, value in kwargs.items():
                if name in names:
                    setattr(self, name, value)

    def to_dictionary(self):
        """Return the dictionary representation of the square."""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
