#!/usr/bin/python3
"""unittest for class Square"""
import unittest
import pep8
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test class for class Square"""

    def test_attributes(self):
        """Test attribute initialization"""
        s1 = Square(98, 99, 100, 101)
        self.assertEqual(s1.size, 98)
        self.assertEqual(s1.x, 99)
        self.assertEqual(s1.y, 100)
        self.assertEqual(s1.id, 101)

    def test_pep8_conformance(self):
        """Test that we conform to PEP8."""
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")
