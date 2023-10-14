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

    def __str__(self):
        """The print method.
        Prints rectangle in stdout with the character _print_symbol_.
        """
        return f"[{self.__class__.__name__}] " + \
            f"({self.id}) {self.__x}/{self.__y} - " + \
            f"{self.__width}/{self.__height}"

    def area(self):
        """The area method.
        Calculates the area of the rectangle.
        """
        return self.__height * self.__width

    def display(self):
        """The display method.
        Prints rectangle in stdout using the character #.
        """
        for y in range(self.__y):
            print()
        for i in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

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

    def update(self, *args, **kwargs):
        """Updater using *args
        Args:
            1st argument should be the id attribute
            2nd argument should be the width attribute
            3rd argument should be the height attribute
            4th argument should be the x attribute
            5th argument should be the y attribute
        """
        if args:
            self.id = args[0]
            if not isinstance(args[0], int):
                raise TypeError("id must be an integer")
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """to_dictionary

        Returns:
            json-type string
        """
        return {
            'x': self.x,
            'width': self.width,
            'id': self.id,
            'height': self.height,
            'y': self.y
        }

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
