#!/usr/bin/python3
"""
json load
"""


def class_to_json(obj):
    """
    class to json
    """
    if not hasattr(obj, '__dict__'):
        raise ValueError
    obj_dict = obj.__dict__
    serializable_attributes = {
        key: value for key, value in obj_dict.items()
    }
    return serializable_attributes
