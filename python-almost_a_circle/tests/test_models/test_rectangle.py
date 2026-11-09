#!/usr/bin/python3
"""Unit tests for models/rectangle.py."""
import io
import os
import unittest
from contextlib import redirect_stdout
from models.base import Base
from models.rectangle import Rectangle


def captured(func):
    """Return what func prints to stdout."""
    buf = io.StringIO()
    with redirect_stdout(buf):
        func()
    return buf.getvalue()


class TestRectangle(unittest.TestCase):
    """Tests for the Rectangle class."""

    def setUp(self):
        """Reset the object counter before each test."""
        Base._Base__nb_objects = 0

    def test_docs(self):
        """The module, class and methods are documented."""
        self.assertTrue(len(Rectangle.__doc__) > 5)
        for name in ("area", "display", "update", "to_dictionary"):
            self.assertTrue(len(getattr(Rectangle, name).__doc__) > 5)

    def test_is_base(self):
        """Rectangle inherits from Base."""
        self.assertTrue(issubclass(Rectangle, Base))
        self.assertIsInstance(Rectangle(1, 2), Base)

    def test_ids(self):
        """Ids follow the Base rules."""
        self.assertEqual(Rectangle(10, 2).id, 1)
        self.assertEqual(Rectangle(2, 10).id, 2)
        self.assertEqual(Rectangle(10, 2, 0, 0, 12).id, 12)

    def test_attributes(self):
        """Constructor arguments are stored and readable."""
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual((r.width, r.height, r.x, r.y, r.id),
                         (1, 2, 3, 4, 5))
        r = Rectangle(1, 2)
        self.assertEqual((r.x, r.y), (0, 0))

    def test_private_attributes(self):
        """Width, height, x and y are private."""
        r = Rectangle(1, 2, 3, 4)
        for name in ("__width", "__height", "__x", "__y"):
            with self.assertRaises(AttributeError):
                getattr(r, name)

    def test_setters(self):
        """Setters update the values."""
        r = Rectangle(1, 2)
        r.width, r.height, r.x, r.y = 10, 20, 30, 40
        self.assertEqual((r.width, r.height, r.x, r.y), (10, 20, 30, 40))

    def test_missing_args(self):
        """Width and height are required."""
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(1)
        with self.assertRaises(TypeError):
            Rectangle(1, 2, 3, 4, 5, 6)

    def test_type_errors(self):
        """Non integers raise TypeError with the attribute name."""
        bad = ["1", 1.5, None, [1], {}, (1,), True, float("inf")]
        for value in bad:
            for args, name in (((value, 1), "width"), ((1, value), "height"),
                               ((1, 1, value), "x"), ((1, 1, 0, value), "y")):
                with self.assertRaisesRegex(TypeError,
                                            "^{} must be an integer$"
                                            .format(name)):
                    Rectangle(*args)

    def test_value_errors(self):
        """Out of range values raise ValueError with the right message."""
        cases = (((0, 1), "width must be > 0"),
                 ((-1, 1), "width must be > 0"),
                 ((1, 0), "height must be > 0"),
                 ((1, -1), "height must be > 0"),
                 ((1, 1, -1), "x must be >= 0"),
                 ((1, 1, 0, -1), "y must be >= 0"))
        for args, msg in cases:
            with self.assertRaisesRegex(ValueError, "^{}$".format(msg)):
                Rectangle(*args)

    def test_validation_order(self):
        """Width is checked first, then height, x and y."""
        with self.assertRaisesRegex(TypeError, "width"):
            Rectangle("1", "2")
        with self.assertRaisesRegex(ValueError, "width"):
            Rectangle(0, "2")
        with self.assertRaisesRegex(TypeError, "height"):
            Rectangle(1, "2", "3")
        with self.assertRaisesRegex(TypeError, "x"):
            Rectangle(1, 2, "3", "4")

    def test_setter_validation(self):
        """Setters validate like the constructor."""
        r = Rectangle(10, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.width = -10
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.x = {}
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.height = "3"
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.y = -1
        self.assertEqual((r.width, r.height, r.x, r.y), (10, 2, 0, 0))

    def test_area(self):
        """area returns width * height."""
        self.assertEqual(Rectangle(3, 2).area(), 6)
        self.assertEqual(Rectangle(2, 10).area(), 20)
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)
        big = Rectangle(999999999999, 999999999999)
        self.assertEqual(big.area(), 999999999998000000000001)
        with self.assertRaises(TypeError):
            Rectangle(1, 1).area(1)

    def test_display(self):
        """display prints the rectangle with '#'."""
        self.assertEqual(captured(Rectangle(4, 6).display), "####\n" * 6)
        self.assertEqual(captured(Rectangle(2, 2).display), "##\n##\n")
        self.assertEqual(captured(Rectangle(1, 1).display), "#\n")

    def test_display_offset(self):
        """display honours x and y."""
        self.assertEqual(captured(Rectangle(2, 3, 2, 2).display),
                         "\n\n  ##\n  ##\n  ##\n")
        self.assertEqual(captured(Rectangle(3, 2, 1, 0).display),
                         " ###\n ###\n")
        self.assertEqual(captured(Rectangle(1, 2, 0, 1).display),
                         "\n#\n#\n")

    def test_str(self):
        """__str__ uses the required format."""
        self.assertEqual(str(Rectangle(4, 6, 2, 1, 12)),
                         "[Rectangle] (12) 2/1 - 4/6")
        self.assertEqual(str(Rectangle(5, 5, 1)),
                         "[Rectangle] (1) 1/0 - 5/5")

    def test_update_args(self):
        """update assigns positional args in order."""
        r = Rectangle(10, 10, 10, 10)
        self.assertEqual(str(r), "[Rectangle] (1) 10/10 - 10/10")
        expected = ["[Rectangle] (89) 10/10 - 10/10",
                    "[Rectangle] (89) 10/10 - 2/10",
                    "[Rectangle] (89) 10/10 - 2/3",
                    "[Rectangle] (89) 4/10 - 2/3",
                    "[Rectangle] (89) 4/5 - 2/3"]
        args = (89, 2, 3, 4, 5)
        for i, text in enumerate(expected):
            r.update(*args[:i + 1])
            self.assertEqual(str(r), text)

    def test_update_no_args(self):
        """update with nothing changes nothing."""
        r = Rectangle(1, 2, 3, 4, 5)
        r.update()
        self.assertEqual(str(r), "[Rectangle] (5) 3/4 - 1/2")

    def test_update_args_validation(self):
        """update validates values like the setters."""
        r = Rectangle(1, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(1, "2")
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(1, 2, 0)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(y=-1)

    def test_update_kwargs(self):
        """update assigns keyword arguments."""
        r = Rectangle(10, 10, 10, 10)
        r.update(height=1)
        self.assertEqual(str(r), "[Rectangle] (1) 10/10 - 10/1")
        r.update(width=1, x=2)
        self.assertEqual(str(r), "[Rectangle] (1) 2/10 - 1/1")
        r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(r), "[Rectangle] (89) 3/1 - 2/1")
        r.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(r), "[Rectangle] (89) 1/3 - 4/2")

    def test_update_args_skip_kwargs(self):
        """kwargs are ignored when args are given."""
        r = Rectangle(10, 10, 10, 10)
        r.update(89, 2, height=7, id=5)
        self.assertEqual(str(r), "[Rectangle] (89) 10/10 - 2/10")

    def test_update_unknown_kwarg(self):
        """Unknown keys are ignored."""
        r = Rectangle(1, 2)
        r.update(color="red")
        self.assertFalse(hasattr(r, "color"))

    def test_to_dictionary(self):
        """to_dictionary returns every attribute."""
        r1 = Rectangle(10, 2, 1, 9)
        d = r1.to_dictionary()
        self.assertIsInstance(d, dict)
        self.assertEqual(d, {"x": 1, "y": 9, "id": 1,
                             "height": 2, "width": 10})
        r2 = Rectangle(1, 1)
        r2.update(**d)
        self.assertEqual(str(r2), str(r1))
        self.assertNotEqual(r1, r2)

    def test_to_dictionary_is_copy(self):
        """Changing the dictionary does not change the rectangle."""
        r = Rectangle(1, 2)
        d = r.to_dictionary()
        d["width"] = 50
        self.assertEqual(r.width, 1)

    def test_save_and_load(self):
        """Rectangle instances round-trip through Rectangle.json."""
        try:
            Rectangle.save_to_file(None)
            self.assertEqual(Rectangle.load_from_file(), [])
            Rectangle.save_to_file([])
            self.assertEqual(Rectangle.load_from_file(), [])
            Rectangle.save_to_file([Rectangle(1, 2, 0, 0, 7)])
            out = Rectangle.load_from_file()
            self.assertEqual(len(out), 1)
            self.assertIsInstance(out[0], Rectangle)
            self.assertEqual(out[0].to_dictionary(),
                             Rectangle(1, 2, 0, 0, 7).to_dictionary())
        finally:
            if os.path.exists("Rectangle.json"):
                os.remove("Rectangle.json")

    def test_load_from_missing_file(self):
        """Loading without a file gives an empty list."""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        self.assertEqual(Rectangle.load_from_file(), [])


if __name__ == "__main__":
    unittest.main()
