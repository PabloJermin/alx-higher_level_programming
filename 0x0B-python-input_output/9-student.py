#!/usr/bin/python3
"""
Module for class
"""

class Student:
    """
    a class student thatdefines students by
    Attributes:
    first_name (str): name of student
    last_name: last name of student
    ae (int): ae of student
    Methods:
    __int__ - initilizes the Student class
    """
    def __init__ (self, first_name, last_name, age):
        """
        initializes Student instance
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self);
    """
    retrieves a dictionary to json format
    """
    return self.__dict__
