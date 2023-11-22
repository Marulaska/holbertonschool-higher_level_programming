#!/usr/bin/python3
"""
read file
"""
import os

def read_file(filename=""):
    """
    read file
    get content to stdout
    """
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    os.write(1, content.encode())
