#!/usr/bin/python3
"""Write a function that prints a square with the character #"""


def print_square(size):
    """Prints a square with the character #"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        print('#' * size)
