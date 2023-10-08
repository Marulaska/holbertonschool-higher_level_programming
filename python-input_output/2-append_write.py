#!/usr/bin/python3
"""
write_file(filename="", text=""):
"""


def append_write(filename="", text=""):
    """
    write_file(filename="", text=""):
    """
    with open(filename, 'a', encoding='utf-8') as file:
        characters_added = file.write(text)
    return characters_added
