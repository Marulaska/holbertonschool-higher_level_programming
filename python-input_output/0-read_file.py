#!/usr/bin/python3
"""
write_file(filename="", text=""):
"""



def read_file(filename=""):
    """
    write_file(filename="", text=""):
    """
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    print(content)
