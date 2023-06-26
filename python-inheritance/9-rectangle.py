#!/usr/bin/python3
"""class Rectangle:
empty class BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """_summary_

    Args:
        BaseGeometry (_type_): _description_
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        return self.__height * self.__width

    def __str__(self):
        a = "[{}] {}/{}"
        output = a.format(self.__class__.__name__, self.__width, self.__height)
        return output

    def print(self):
        a = "[{}] {}/{}"
        output = a.format(self.__class__.__name__, self.__width, self.__height)
        print(output)
