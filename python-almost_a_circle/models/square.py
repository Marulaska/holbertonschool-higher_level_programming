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

    def update(self, *args, **kwargs):
        """Updater using *args
        Args:
            1st argument should be the id attribute
            2nd argument should be the size attribute
            3th argument should be the x attribute
            4th argument should be the y attribute
        """
        if args:
            if not isinstance(args[0], int):
                raise TypeError("id must be an integer")
            self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
                self.height = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def __str__(self):
        """The print method.
        Prints rectangle in stdout with the character _print_symbol_.
        """
        return f"[{self.__class__.__name__}] " + \
            f"({self.id}) {self.x}/{self.y} - " + \
            f"{self.width}"

    def to_dictionary(self):
        """to_dictionary

        Returns:
            json-type string
        """
        return {
            'id': self.id,
            'x': self.x,
            'size': self.size,
            'y': self.y,
        }

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
