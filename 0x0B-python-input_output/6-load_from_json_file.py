#!/usr/bin/python3
"""
6-load_from_json_file.py
"""
import json


def load_from_json_file(filename):
    """
    load_from_json_file - loads an object from JSON file
    Ars:
    filename: name of the file
    """
    with open (filename, mode="r") as f:
        my_obj = json.load(f)
        return my_obj
