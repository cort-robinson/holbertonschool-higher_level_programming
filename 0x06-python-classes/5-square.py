#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 4-square.py)"""


class Square:
    """It's a square"""
    def __init__(self, size=0):
        """Constructor to initialize class values"""
        self._size = size

    def area(self):
        """Method returns area of Square instance"""
        return self._size ** 2

    @property
    def size(self):
        """Getter method for size"""
        return self._size

    @size.setter
    def size(self, value):
        """Setter value for size"""
        if isinstance(value, int):
            self._size = value
        else:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    def my_print(self):
        """Print the square to stdout"""
        for _ in range(self.size):
            print('#' * self.size)
        if self.size == 0:
            print()
