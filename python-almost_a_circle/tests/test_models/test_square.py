#!/usr/bin/python3
"""Unit tests for models/square.py."""
import io
import unittest
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


def captured(func):
    """Return what func prints to stdout."""
    buf = io.StringIO()
    with redirect_stdout(buf):
        func()
    return buf.getvalue()


class TestSquare(unittest.TestCase):
    """Tests for the Square class."""

    def setUp(self):
        """Reset the object counter before each test."""
        Base._Base__nb_objects = 0

    def test_docs(self):
        """The class and methods are documented."""
        self.assertTrue(len(Square.__doc__) > 5)
        for name in ("update", "to_dictionary", "__str__"):
            self.assertTrue(len(getattr(Square, name).__doc__) > 5)

    def test_inheritance(self):
        """Square inherits from Rectangle and Base."""
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertIsInstance(Square(1), Base)

    def test_constructor(self):
        """Size sets width and height; ids follow Base."""
        s = Square(5)
        self.assertEqual((s.width, s.height, s.size, s.x, s.y, s.id),
                         (5, 5, 5, 0, 0, 1))
        s = Square(2, 3, 4, 7)
        self.assertEqual((s.size, s.x, s.y, s.id), (2, 3, 4, 7))
        self.assertEqual(Square(1).id, 2)

    def test_missing_args(self):
        """Size is required; at most four arguments."""
        with self.assertRaises(TypeError):
            Square()
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5)

    def test_no_new_attributes(self):
        """Square keeps only the Rectangle attributes."""
        s = Square(3)
        self.assertEqual(sorted(vars(s)),
                         sorted(vars(Rectangle(3, 3))))

    def test_validation(self):
        """Wrong values raise the Rectangle errors."""
        cases = ((("1",), TypeError, "width must be an integer"),
                 ((1.5,), TypeError, "width must be an integer"),
                 ((None,), TypeError, "width must be an integer"),
                 ((0,), ValueError, "width must be > 0"),
                 ((-1,), ValueError, "width must be > 0"),
                 ((1, "2"), TypeError, "x must be an integer"),
                 ((1, -2), ValueError, "x must be >= 0"),
                 ((1, 2, "3"), TypeError, "y must be an integer"),
                 ((1, 2, -3), ValueError, "y must be >= 0"))
        for args, err, msg in cases:
            with self.assertRaisesRegex(err, "^{}$".format(msg)):
                Square(*args)

    def test_area_display(self):
        """area and display come from Rectangle."""
        self.assertEqual(Square(5).area(), 25)
        self.assertEqual(captured(Square(2, 2).display), "  ##\n  ##\n")
        self.assertEqual(captured(Square(3, 1, 3).display),
                         "\n\n\n ###\n ###\n ###\n")

    def test_str(self):
        """__str__ uses the Square format."""
        self.assertEqual(str(Square(5)), "[Square] (1) 0/0 - 5")
        self.assertEqual(str(Square(2, 2)), "[Square] (2) 2/0 - 2")
        self.assertEqual(str(Square(3, 1, 3)), "[Square] (3) 1/3 - 3")

    def test_size(self):
        """size getter and setter keep width and height equal."""
        s = Square(5)
        self.assertEqual(s.size, 5)
        s.size = 10
        self.assertEqual((s.width, s.height), (10, 10))
        self.assertEqual(str(s), "[Square] (1) 0/0 - 10")

    def test_size_validation(self):
        """size setter raises the width messages."""
        s = Square(5)
        with self.assertRaisesRegex(TypeError, "^width must be an integer$"):
            s.size = "9"
        with self.assertRaisesRegex(ValueError, "^width must be > 0$"):
            s.size = 0
        self.assertEqual(s.size, 5)

    def test_update_args(self):
        """update assigns id, size, x and y in order."""
        s = Square(5)
        steps = (((10,), "[Square] (10) 0/0 - 5"),
                 ((1, 2), "[Square] (1) 0/0 - 2"),
                 ((1, 2, 3), "[Square] (1) 3/0 - 2"),
                 ((1, 2, 3, 4), "[Square] (1) 3/4 - 2"))
        for args, text in steps:
            s.update(*args)
            self.assertEqual(str(s), text)

    def test_update_kwargs(self):
        """update assigns keyword arguments when no args are given."""
        s = Square(5)
        s.update(1, 2, 3, 4)
        s.update(x=12)
        self.assertEqual(str(s), "[Square] (1) 12/4 - 2")
        s.update(size=7, y=1)
        self.assertEqual(str(s), "[Square] (1) 12/1 - 7")
        s.update(size=7, id=89, y=1)
        self.assertEqual(str(s), "[Square] (89) 12/1 - 7")

    def test_update_args_skip_kwargs(self):
        """kwargs are ignored when args are given."""
        s = Square(5)
        s.update(3, size=9)
        self.assertEqual(str(s), "[Square] (3) 0/0 - 5")

    def test_update_validation(self):
        """update validates the values."""
        s = Square(5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.update(1, "2")
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s.update(x=-1)

    def test_to_dictionary(self):
        """to_dictionary returns id, size, x and y."""
        s1 = Square(10, 2, 1)
        d = s1.to_dictionary()
        self.assertEqual(d, {"id": 1, "x": 2, "size": 10, "y": 1})
        s2 = Square(1, 1)
        s2.update(**d)
        self.assertEqual(str(s2), str(s1))
        self.assertNotEqual(s1, s2)


if __name__ == "__main__":
    unittest.main()
