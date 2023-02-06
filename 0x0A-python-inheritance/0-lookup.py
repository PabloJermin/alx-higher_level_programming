#!/usr/bin/python3
"""Returns a function lookup"""

def lookup(obj):
    """Function that returns a list of attributes and methods
    Args:
        obj (class): object

    Returns:
        list: list of available attributes and functions"""
        return dir(obj)
