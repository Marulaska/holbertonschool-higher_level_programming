#!/usr/bin/python3
"""
read file
"""


def read_file(filename=""):
    """
    READ FILE
    GET FILE TOP SDTOUT
    """
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    print(content)
