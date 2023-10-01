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

    def __init__(self, size=0):
        """The __init__ method.

        Creates an instance of a square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """The area method.
        Calculates the area of a square.
        """
        return self.__size * self.__size

    @property
    def size(self):
        """The size getter.
        Retrieves the size of a square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """The size setter.
        Creates an instance of a square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """The my_print method.
        Prints square in stdout with the character #.
        """
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()

        if self.__size == 0:
            print()
