#!/usr/bin/python3
"""_summary_
"""


def read_file(filename=""):
    """0-read_file.py"""
    with open(filename, 'r') as file:
        content = file.read()
    print(content)
    file.close()
