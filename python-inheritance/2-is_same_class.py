#!/usr/bin/python3
"""
function that returns True if the object is exactly an instance
of the specified class ; otherwise False.
"""


def is_same_class(obj, a_class):
    is_same_class = isinstance(obj, a_class)
    if is_same_class:
        print("Yes")
    else:
        print("No")
