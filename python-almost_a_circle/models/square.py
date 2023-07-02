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
