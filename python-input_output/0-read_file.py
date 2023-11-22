#!/usr/bin/python3
"""
read file
"""


def read_file(filename=""):
    """
    read file
    get content to stdout
    """
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    print(content, end='')
