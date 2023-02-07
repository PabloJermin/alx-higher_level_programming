#!/usr/bin/python3
"""Defines a function is_kind_ofclass()"""
def is_kind_of_class(obj, a_class);
"""Returns True if the object is an instance of or is the object of the instance
a class that inherited from the specified class, otherwise false.
Args:
    obj (a_class): object to check type
    a_class (type): type of type o check.
returns:
    booleand: True or false.
    """
    #print("--->obj type {}".format(type(obj)))
    #print("--->a_class type {}".format(type(a_class)))
    return isinstance(obj, a_class)
