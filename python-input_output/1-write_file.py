#!/usr/bin/python3
"""
write_file(filename="", text=""):
"""


def write_file(filename="", text=""):
    """
    write_file(filename="", text=""):
    """
    with open(filename, 'w', encoding='utf-8') as file:
        characters_written = file.write(text)
    return characters_written
