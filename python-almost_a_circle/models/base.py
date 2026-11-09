#!/usr/bin/python3
"""Defines the Base class that manages ids for all shapes."""
import csv
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

    @classmethod
    def _csv_fields(cls):
        """Return the CSV column order for cls."""
        if cls.__name__ == "Square":
            return ["id", "size", "x", "y"]
        return ["id", "width", "height", "x", "y"]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write list_objs to <cls>.csv, one object per row."""
        fields = cls._csv_fields()
        with open(cls.__name__ + ".csv", "w", newline="",
                  encoding="utf-8") as f:
            writer = csv.writer(f)
            for obj in list_objs or []:
                d = obj.to_dictionary()
                writer.writerow([d[k] for k in fields])

    @classmethod
    def load_from_file_csv(cls):
        """Return the list of instances stored in <cls>.csv."""
        fields = cls._csv_fields()
        try:
            with open(cls.__name__ + ".csv", "r", newline="",
                      encoding="utf-8") as f:
                rows = [row for row in csv.reader(f) if row]
        except FileNotFoundError:
            return []
        return [cls.create(**dict(zip(fields, map(int, row))))
                for row in rows]
