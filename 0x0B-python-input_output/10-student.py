#!/usr/bin/python3
"""
Module for calsss Student
"""

class Student:
    """
    a class student that define students by:
    Attribuytes:
    first_name: the first name of student
    last_name: last name of student
    age: ae of student
    Methods:
    __init__ - initialize the student instance.
    to_json - retrieves a dictionary rep if students
    """
    def __init__(self, first_name, last_name, age):
        """
        initialize the instance
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=Npne):
        """
        retrieves a dictionary representation of student
        Args:
        attr (list): attribute names that are to be retrieved.
        """
        if attr is not None:
            res = {k: self,__dict__[k] for k in self.__dict__.keys() & attr)
                return res
        else:
            return self.__dict__
