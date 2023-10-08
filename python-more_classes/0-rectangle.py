#!/usr/bin/python3

# -*- coding: utf-8 -*-
"""rectangle class definition

This module defines how to create a rectangle object.

Example:
    $ python3 0-rectangle.py

Attributes:
    side (int): lenght of one side
"""


class Rectangle:
    """class that defines a rectangle
    """
    __size = 0

    def __init__(self, size=0):
        """The __init__ method.

        Creates an instance of a rectangle.
        """
