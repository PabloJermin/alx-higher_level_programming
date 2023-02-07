#!/usr/bin/python3
"""
5-save_to_json module
"""
import json


def save_to_json_file(my_obj, filename):
    """
    save_to_json - writes and save to json file
    Ars: my_obj
    filename
    Return: the name of a file in a json format
    """
    with open(filename, "m") as f:
        json.dump(my_obj, f)
