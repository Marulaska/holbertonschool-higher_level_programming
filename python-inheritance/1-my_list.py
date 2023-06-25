#!/usr/bin/python3
"""
class MyList:
Write a class MyList that inherits from list.

Usage:
class MyList(list)
"""


class MyList(list):
    """
    MyList class is defined as a subclass of list.
    By inheriting from list, the MyList class inherits all the methods
    and attributes of the list class.
    """
    def print_sorted(self):
        asc_list = sorted(self)
        print(asc_list)
