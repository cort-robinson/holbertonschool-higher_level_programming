#!/usr/bin/python3
"""unittest for class Rectangle"""
import unittest
import pep8
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test class for class Rectangle"""

    def test_attributes(self):
        """Test attribute initialization"""
        r1 = Rectangle(98, 99, 100, 101, 102)
        self.assertEqual(r1.width, 98)
        self.assertEqual(r1.height, 99)
        self.assertEqual(r1.x, 100)
        self.assertEqual(r1.y, 101)
        self.assertEqual(r1.id, 102)
        r2 = Rectangle(98, 256)
        self.assertEqual(r2.width, 98)
        self.assertEqual(r2.height, 256)

    def test_area(self):
        """Test area method"""
        r1 = Rectangle(3, 4)
        self.assertEqual(r1.area(), 12)
        r2 = Rectangle(98, 256)
        self.assertEqual(r2.area(), 25088)

    def test__str__(self):
        r1 = Rectangle(98, 128, 256, 1024, 2048)
        self.assertEqual(r1.__str__(), "[Rectangle] (2048) 256/1024 - 98/128")

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


if __name__ == "__main__":
    unittest.main()
