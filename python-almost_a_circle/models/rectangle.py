#!/usr/bin/python3
"""Defines the Rectangle class, a Base with validated dimensions."""
from models.base import Base


class Rectangle(Base):
    """A rectangle with width, height and an (x, y) offset."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle and validate every attribute."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @staticmethod
    def _validate(name, value, positive):
        """Raise if value is not an int or out of its allowed range."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if positive and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        if not positive and value < 0:
            raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self):
        """Get or set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        self._validate("width", value, True)
        self.__width = value

    @property
    def height(self):
        """Get or set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        self._validate("height", value, True)
        self.__height = value

    @property
    def x(self):
        """Get or set the horizontal offset of the rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        self._validate("x", value, False)
        self.__x = value

    @property
    def y(self):
        """Get or set the vertical offset of the rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        self._validate("y", value, False)
        self.__y = value

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Print the rectangle with '#', shifted by x and y."""
        print("\n" * self.y, end="")
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return [Rectangle] (<id>) <x>/<y> - <width>/<height>."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Assign attributes from positional args or else from kwargs."""
        names = ("id", "width", "height", "x", "y")
        if args:
            for name, value in zip(names, args):
                setattr(self, name, value)
        else:
            for name, value in kwargs.items():
                if name in names:
                    setattr(self, name, value)

    def to_dictionary(self):
        """Return the dictionary representation of the rectangle."""
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
