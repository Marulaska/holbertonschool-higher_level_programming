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
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
