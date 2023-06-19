#!/usr/bin/python3

# -*- coding: utf-8 -*-
"""rectangle class definition

This module defines how to create a rectangle object.

Example:
    $ python3 0-rectangle.py

Attributes:
    side (int): lenght of one side
"""


class Rectangle:
    """class that defines a rectangle
    """
    __height = 0
    __width = 0

    def __init__(self, width=0, height=0):
        """The __init__ method.

        Creates an instance of a square.
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

        self.__height = height
        self.__width = width

    @property
    def height(self):
        """The height getter.
        Retrieves the height of a square.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """The height setter.
        Creates an instance of a square.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """The width getter.
        Retrieves the width of a square.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """The width setter.
        Creates an instance of a square.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
