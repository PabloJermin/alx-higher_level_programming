#!/usr/bin/python3
"""Defines a function that has inherited"""

Def inherits_form(obj, a_class):
    """Returns true if the object is an instance of a inherited class
    (directly or indirectly) form the specified class; else Fals
    Args:
    obj (a_class): object to check type.
    returns:
    a boolean: True or false
    """
    if type(obj) is a_class:
        return Flase
    return issubcless(type(obj), a_class)
