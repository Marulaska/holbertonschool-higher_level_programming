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

    def _intvalidator(self, field, value):
        """_intvalidator

        Args:
            field (str): field we're validating
            value (any): I hope it's an int

        Raises:
            TypeError: if not `int`.
            ValueError: if value under 0.
        Returns:
            True if no errors found.
        """
        if not isinstance(value, int):
            raise TypeError(f"{field} must be an integer")
        if value <= 0 and (field == "width" or field == "height"):
            raise ValueError(f"{field} must be > 0")
        if value < 0 and (field == "x" or field == "y"):
            raise ValueError(f"{field} must be >= 0")
        return True


    def area(self):
        """The area method.
        Calculates the area of the rectangle.
        """
        return self.__height * self.__width

    def __init__(self, width, height, x=0, y=0, id=None):
        """__init__ function

        Args:
            width (int): _description_
            height (int): _description_
            x (int, optional): _description_. Defaults to 0.
            y (int, optional): _description_. Defaults to 0.
            id (_type_, optional): _description_. Defaults to None.
        """

        if self._intvalidator("width", width):
            self.__width = width
        if self._intvalidator("height", height):
            self.__height = height
        if self._intvalidator("x", x):
            self.__x = x
        if self._intvalidator("y", y):
            self.__y = y

        super().__init__(id)

    @property
    def width(self):
        """The width getter.
        Retrieves the width of a rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """The width setter.
        """
        if self._intvalidator("width", value):
            self.__width = value

    @property
    def height(self):
        """The height getter.
        Retrieves the height of a rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height setter.
        """
        if self._intvalidator("height", value):
            self.__height = value

    @property
    def x(self):
        """The x getter.
        Retrieves the x of a rectangle.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """The x setter.
        """
        if self._intvalidator("x", value):
            self.__x = value

    @property
    def y(self):
        """The y getter.
        Retrieves the y of a rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """The y setter.
        """
        if self._intvalidator("y", value):
            self.__y = value
