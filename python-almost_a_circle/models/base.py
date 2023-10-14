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

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file

        Args:
            list_objs (_type_): _description_
        """
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        json_string = cls.to_json_string(
            [obj.to_dictionary() for obj in list_objs]
        )

        with open(filename, 'w') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """_summary_

        Args:
            json_string (_type_): _description_

        Returns:
            _type_: _description_
        """
        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == 'Rectangle':
            instance = cls(1, 1)
            instance.update(**dictionary)
            return instance
        elif cls.__name__ == 'Square':
            instance = cls(1)
            instance.update(**dictionary)
            return instance
        else:
            return None

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                json_string = file.read()
                data = cls.from_json_string(json_string)
                instances = []
                for item in data:
                    instance = cls.create(**item)
                    if instance is not None:
                        instances.append(instance)

                return instances
        except FileNotFoundError:
            return []
