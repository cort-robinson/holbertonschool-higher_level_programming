#!/usr/bin/python3
"""unittest for class Base"""
import unittest
import pep8
from models.base import Base


class TestBase(unittest.TestCase):
    """Test class for class Base"""

    def test_id(self):
        """Test for id functionality"""
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(98)
        self.assertEqual(b3.id, 98)
        b4 = Base(256)
        self.assertEqual(b4.id, 256)
        b5 = Base()
        self.assertEqual(b5.id, 3)
        b6 = Base(-98)
        self.assertEqual(b6.id, -98)
        b7 = Base(None)
        self.assertEqual(b7.id, 4)

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


if __name__ == "__main__":
    unittest.main()
