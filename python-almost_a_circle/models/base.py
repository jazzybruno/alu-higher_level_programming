#!/usr/bin/python3
"""Defines the Base class that manages ids for all shapes."""
import json


class Base:
    """Base of every shape: manages the id attribute of instances."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base with the given id or the next free one."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of a list of dicts."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Return the list of dicts represented by a JSON string."""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON representation of list_objs to <cls>.json."""
        dicts = []
        if list_objs is not None:
            dicts = [obj.to_dictionary() for obj in list_objs]
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(dicts))

    @classmethod
    def create(cls, **dictionary):
        """Return an instance of cls with all attributes from dictionary."""
        if cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return the list of instances stored in <cls>.json."""
        try:
            with open(cls.__name__ + ".json", "r", encoding="utf-8") as f:
                dicts = cls.from_json_string(f.read())
        except FileNotFoundError:
            return []
        return [cls.create(**d) for d in dicts]

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw every Rectangle and Square in a turtle window."""
        import turtle

        pen = turtle.Turtle()
        pen.screen.bgcolor("#f0f0f0")
        pen.pensize(3)
        pen.speed(0)
        colors = ["#1f77b4", "#d62728", "#2ca02c", "#9467bd"]
        shapes = list(list_rectangles or []) + list(list_squares or [])
        for i, shape in enumerate(shapes):
            pen.color(colors[i % len(colors)])
            pen.penup()
            pen.goto(shape.x, shape.y)
            pen.pendown()
            for _ in range(2):
                pen.forward(shape.width)
                pen.left(90)
                pen.forward(shape.height)
                pen.left(90)
        turtle.exitonclick()
