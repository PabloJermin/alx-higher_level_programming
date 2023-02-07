#!/usr/bin/python3
"""
4-from_json_strin module
"""

import json


def from_json_string(my_str):
    """
    from _json_string - returns an object (Python data structure) represented by a JSON strin
    Ars:
    my_str: json strin to represent 
    Return: object
    """
    return json.loads(my_str)
