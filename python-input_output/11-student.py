#!/usr/bin/python3
"""
class student
"""


class Student:
    """
    Student Class
    """
    def __init__(self, first_name, last_name, age):
        """
        Args:
            first_name
            last_name
            age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        return json rep
        """
        if attrs is None:
            attrs = self.__dict__.keys()

        serializable_attributes = {}
        for key in attrs:
            if key in self.__dict__:
                serializable_attributes[key] = self.__dict__[key]
        return serializable_attributes

    def reload_from_json(self, json):
        """_summary_

        Args:
            json (_type_): _description_
        """
        for key, value in json.items():
            setattr(self, key, value)
