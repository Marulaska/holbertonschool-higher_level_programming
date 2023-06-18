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
    __size = 0
    __position = (0, 0)

    def __init__(self, size=0, position=(0, 0)):
        """The __init__ method.

        Creates an instance of a square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if position is not None:
            positionok = True
            if not isinstance(position, tuple):
                positionok = False
            if not all(isinstance(x, int) for x in position):
                positionok = False
            if position[0] < 0 or position[1] < 0:
                positionok = False
            if not positionok:
                raise
                TypeError("position must be a tuple of 2 positive integers")
            self.__position = position
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

    @property
    def position(self):
        """The position getter.
        Retrieves the coordinates of a square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """The size setter.
        Set the new position of a square.
        """
        positionok = True
        if not isinstance(position, tuple):
            positionok = False
        if not all(isinstance(x, int) for x in position):
            positionok = False
        if position[0] < 0 or position[1] < 0:
            positionok = False
        if not positionok:
            raise
            TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def my_print(self):
        """The my_print method.
        Prints square in stdout with the character #.
        """
        for y in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for x in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()

        if self.__size == 0:
            print()
