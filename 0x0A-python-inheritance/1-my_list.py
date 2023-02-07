#!/usr/bin/python3
"""Defines a class Mylist that inherits from list"""

class Mylist(list):
    """CLass that inherits form mylist.
    Args:
    list (list): List to sort in ascending order
    """
    def print_sorted(self):
        """prints a list in ascending order"""
        list_ = self[:]
        list_.sort()
        print(list_)
