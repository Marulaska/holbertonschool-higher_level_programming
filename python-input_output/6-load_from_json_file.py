#!/usr/bin/python3
"""json load"""
import json


def load_from_json_file(filename):
    """load from json"""
    with open(filename, 'r', encoding='utf-8') as f:
        content = json.load(f)
    return content
