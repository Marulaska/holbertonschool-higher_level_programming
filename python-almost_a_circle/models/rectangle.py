#!/usr/bin/python3
"""class Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """Rectangle attributes

    Args:
        Base (_type_): _description_
    """

    __width = 0
    __height = 0
    __x = 0
    __y = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(self, id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """The size getter.
        Retrieves the size of a square.
        """
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """The size getter.
        Retrieves the size of a square.
        """
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        """The size getter.
        Retrieves the size of a square.
        """
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """The size getter.
        Retrieves the size of a square.
        """
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
