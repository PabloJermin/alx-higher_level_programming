#!/usr/bin/python3
"""
3-to_json_strin module
"""
import json


def to_json_string(my_obj):
    """
    to_json_strin - returns the JSON representation in a strin
    Ars:
    my_obj: strin to represent
    Return: json representation
    """
    return json.dumps(my_obj)
