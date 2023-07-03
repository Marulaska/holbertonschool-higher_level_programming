#!/usr/bin/python3
"""class Base
"""
import json


class Base():
    """Base attributes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """__init__

        Args:
            id (_type_, optional): _description_. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string
        Returns:
            same object but jsonified
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
