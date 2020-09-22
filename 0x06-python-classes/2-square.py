#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 1-square.py)"""


class Square:
    """Class Square checks if size attribute is int"""
    def __init__(self, size=0):
        """Constructor to initialize class values"""
        if isinstance(size, int):
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
