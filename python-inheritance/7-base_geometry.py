#!/usr/bin/python3
"""class BaseGeometry:
empty class BaseGeometry
"""


class BaseGeometry:
    """empty class BaseGeometry
    """
    def area(self):
        """empty class BaseGeometry
        """
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """empty class BaseGeometry
        """
        if not issubclass(type(value), int):
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
