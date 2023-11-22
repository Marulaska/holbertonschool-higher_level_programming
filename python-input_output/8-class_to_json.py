#!/usr/bin/python3
"""json load"""
import json


def class_to_json(obj):
    """class to json"""
    if not hasattr(obj, '__dict__'):
        raise ValueError
    obj_dict = obj.__dict__
    serializable_attributes = {
        key: value for key, value in obj_dict.items() if is_serializable(value)
    }

    return serializable_attributes

def is_serializable(value):
    """serializable"""
    if isinstance(value, (list, dict, str, int, bool)):
        return True
    elif hasattr(value, '__dict__'):
        return all(is_serializable(v) for v in value.__dict__.values())
    else:
        return False
