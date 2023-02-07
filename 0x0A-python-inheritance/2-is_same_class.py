#!/usr/bin/python3
"""Defines a function that returns true if the instaces are the same"""
def is_same_class(obj, a_class):
    """Returns True if the object is an instance of the specified class; otherwise False.
    Args:
    obj (a_class): object to check type.
    a_class (type): type of type to check.
    Returns: Boolean: True or False"""
    return type(obj) == a_class
