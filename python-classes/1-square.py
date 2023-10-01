#!/usr/bin/python3

# -*- coding: utf-8 -*-
"""Square class definition

This module defines how to create a square object.

Example:
    $ python3 0-square.py

Attributes:
    side (int): lenght of one side
"""


class Square:
    """class that defines a square
    """
    __size = ()

    def __init__(self, newsize=None):
        """The __init__ method.

        Creates an instance of a square.
        """
        if newsize is not None:
            self.__size = newsize
