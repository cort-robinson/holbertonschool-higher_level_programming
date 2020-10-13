#!/usr/bin/python3
"""Define class Rectangle which inherits from class Base"""
from models.base import Base


class Rectangle(Base):
    """Rectangle model class inheriting from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return self.width * self.height

    def display(self):
        if self.width == 0 or self.height == 0:
            print("")
        row = (' ' * self.x) + ('#' * self.width) + '\n'
        print(('\n' * self.y) + row * (self.height - 1) + (
            (' ' * self.x) + ('#' * self.width)))

    def __str__(self):
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args):
        if len(args) == 1:
            self.id = args[0]
        elif len(args) == 2:
            self.id, self.width = [arg for arg in args]
        elif len(args) == 3:
            self.id, self.width, self.height = [arg for arg in args]
        elif len(args) == 4:
            self.id, self.width, self.height, self.x = [arg for arg in args]
        elif len(args) == 4:
            self.id, self.width, self.height, self.x, = [arg for arg in args]
