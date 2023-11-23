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

    def to_json(self):
        """
        return json rep
        """
        serializable_attributes = {
            key: value for key, value in self.__dict__.items()
        }
        return serializable_attributes
