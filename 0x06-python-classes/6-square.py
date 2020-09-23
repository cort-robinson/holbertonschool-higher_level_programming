#!/usr/bin/python3
"""Write a class Square that defines a square by: (based on 5-square.py)"""


class Square:
    """It's a square"""
    def __init__(self, size=0, position=(0, 0)):
        self._size = size
        self._position = position

    @property
    def size(self):
        """"Getter"""
        return self._size

    @size.setter
    def size(self, value):
        """Setter"""
        if isinstance(value, int):
            self.size = value
        else:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        """Getter"""
        return self._position

    @position.setter
    def position(self, value):
        """Setter"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] >= 0 and value[1] >= 0:
            raise ValueError("size must be >= 0")
        else:
            self.position = value

    def area(self):
        """Returns area of Square instance"""
        return self.size ** 2

    def my_print(self):
        """Print the Square instance to stdout"""
        if self.position[1] > 0:
            print('\n' * self.position[1], end="")
        for _ in range(self.size):
            print(" " * self.position[0], end="")
            print('#' * self.size)
        if self.size == 0:
            print()
