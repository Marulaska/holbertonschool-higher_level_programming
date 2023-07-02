#!/usr/bin/python3
"""class Base
"""


class Base:
    """Base attributes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
            self.id = Base.__nb_objects
        else:
            Base.__nb_objects += 1
