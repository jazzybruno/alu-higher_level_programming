#!/usr/bin/python3
"""Unit tests for models/base.py."""
import json
import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Tests for the Base class."""

    def setUp(self):
        """Reset the object counter before each test."""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Remove JSON files written by the tests."""
        for name in ("Base.json", "Rectangle.json", "Square.json"):
            if os.path.exists(name):
                os.remove(name)

    def test_module_doc(self):
        """The module and class are documented."""
        self.assertTrue(len(__import__("models.base").base.__doc__) > 5)
        self.assertTrue(len(Base.__doc__) > 5)

    def test_auto_id(self):
        """Ids increment automatically when none is given."""
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base().id, 2)
        self.assertEqual(Base(None).id, 3)

    def test_given_id(self):
        """A given id is used and does not touch the counter."""
        self.assertEqual(Base(12).id, 12)
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base(-5).id, -5)
        self.assertEqual(Base("abc").id, "abc")

    def test_mixed_ids(self):
        """Mixing given and automatic ids follows the spec example."""
        ids = [Base().id, Base().id, Base().id, Base(12).id, Base().id]
        self.assertEqual(ids, [1, 2, 3, 12, 4])

    def test_private_counter(self):
        """The counter is not reachable by its plain name."""
        with self.assertRaises(AttributeError):
            Base.__nb_objects

    def test_too_many_args(self):
        """The constructor takes at most one argument."""
        with self.assertRaises(TypeError):
            Base(1, 2)

    def test_to_json_string(self):
        """Lists of dicts are serialized to JSON."""
        d = {"id": 1, "width": 10, "height": 7, "x": 2, "y": 8}
        out = Base.to_json_string([d])
        self.assertIsInstance(out, str)
        self.assertEqual(json.loads(out), [d])
        two = Base.to_json_string([d, {"id": 2}])
        self.assertEqual(json.loads(two), [d, {"id": 2}])

    def test_to_json_string_empty(self):
        """None and empty lists give the string '[]'."""
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_no_arg(self):
        """to_json_string needs exactly one argument."""
        with self.assertRaises(TypeError):
            Base.to_json_string()
        with self.assertRaises(TypeError):
            Base.to_json_string([], [])

    def test_from_json_string(self):
        """JSON strings are turned back into lists of dicts."""
        data = [{"id": 89, "width": 10, "height": 4},
                {"id": 7, "width": 1, "height": 7}]
        out = Base.from_json_string(Base.to_json_string(data))
        self.assertIsInstance(out, list)
        self.assertEqual(out, data)

    def test_from_json_string_empty(self):
        """None and empty strings give an empty list."""
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_no_arg(self):
        """from_json_string needs exactly one argument."""
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_save_to_file_rectangle(self):
        """Rectangles are saved to Rectangle.json."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as f:
            data = json.loads(f.read())
        self.assertEqual(data, [r1.to_dictionary(), r2.to_dictionary()])

    def test_save_to_file_square(self):
        """Squares are saved to Square.json."""
        s = Square(10, 7, 2, 8)
        Square.save_to_file([s])
        with open("Square.json", "r") as f:
            self.assertEqual(json.loads(f.read()), [s.to_dictionary()])

    def test_save_to_file_none_and_empty(self):
        """None and empty lists save an empty JSON list."""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_to_file_overwrites(self):
        """Saving again replaces the previous file content."""
        Rectangle.save_to_file([Rectangle(1, 2), Rectangle(3, 4)])
        Rectangle.save_to_file([Rectangle(5, 6)])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(len(json.loads(f.read())), 1)

    def test_save_to_file_no_arg(self):
        """save_to_file needs exactly one argument."""
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_create_rectangle(self):
        """create builds an equal but distinct Rectangle."""
        r1 = Rectangle(3, 5, 1, 2, 7)
        r2 = Rectangle.create(**r1.to_dictionary())
        self.assertEqual(str(r1), str(r2))
        self.assertIsNot(r1, r2)
        self.assertNotEqual(r1, r2)
        self.assertIsInstance(r2, Rectangle)

    def test_create_square(self):
        """create builds an equal but distinct Square."""
        s1 = Square(3, 1, 2, 7)
        s2 = Square.create(**s1.to_dictionary())
        self.assertEqual(str(s1), str(s2))
        self.assertIsNot(s1, s2)
        self.assertIsInstance(s2, Square)

    def test_create_partial(self):
        """create works with only some attributes given."""
        self.assertEqual(Rectangle.create(id=89).id, 89)
        r = Rectangle.create(id=89, width=1, height=2)
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 1/2")
        s = Square.create(id=89, size=1, x=2, y=3)
        self.assertEqual(str(s), "[Square] (89) 2/3 - 1")

    def test_load_from_file_missing(self):
        """A missing file gives an empty list."""
        self.assertEqual(Rectangle.load_from_file(), [])
        self.assertEqual(Square.load_from_file(), [])

    def test_load_from_file_rectangle(self):
        """Rectangles round-trip through the file."""
        rects = [Rectangle(10, 7, 2, 8), Rectangle(2, 4)]
        Rectangle.save_to_file(rects)
        out = Rectangle.load_from_file()
        self.assertEqual([str(r) for r in out], [str(r) for r in rects])
        self.assertTrue(all(type(r) is Rectangle for r in out))

    def test_load_from_file_square(self):
        """Squares round-trip through the file."""
        squares = [Square(5), Square(7, 9, 1)]
        Square.save_to_file(squares)
        out = Square.load_from_file()
        self.assertEqual([str(s) for s in out], [str(s) for s in squares])
        self.assertTrue(all(type(s) is Square for s in out))


if __name__ == "__main__":
    unittest.main()
