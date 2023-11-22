#!/usr/bin/python3
"""
write_file(filename="", text=""):
"""
import json


def to_json_string(my_obj):
    """
    write_file(filename="", text=""):
    """
    j_object = json.dumps(my_obj)
    return j_object
