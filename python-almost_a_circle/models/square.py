#!/usr/bin/python3
"""class Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Args:
        Rectangle (Base)
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Square __init__ function

        Args:
            size (int): height and width of the square
            x (int, optional): position in the x-axis. Defaults to 0.
            y (int, optional): position in the y-axis. Defaults to 0.
            id (int, optional): identifier. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """The print method.
        Prints rectangle in stdout with the character _print_symbol_.
        """
        return f"[{self.__class__.__name__}] " + \
            f"({self.id}) {self.x}/{self.y} - " + \
            f"{self.width}"

    @property
    def size(self):
        """The width getter.
        Retrieves the width of a rectangle.
        """
        return self.width

    @size.setter
    def size(self, value):
        """The width setter.
        """
        self.width = value
        self.height = value
