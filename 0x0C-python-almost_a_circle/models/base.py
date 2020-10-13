#!/usr/bin/python3
"""Define class Base"""


class Base:
    """Base class for other classes. Manages id attribute in
    all future classes and avoids duplicating the same code"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
