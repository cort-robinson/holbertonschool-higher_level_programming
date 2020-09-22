#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 2-square.py)"""


class Square:
    """It's a square"""
    def __init__(self, size=0):
        """Constructor to initialize class values"""
        if isinstance(size, int):
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Returns area of Square instance"""
        return self.__size ** 2
