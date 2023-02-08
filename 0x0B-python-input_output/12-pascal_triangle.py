#!/usr/bin/python3
"""
Module for pasca_triangle method
"""


def pascal_triangle(n):
    """
    returns a list of integers
    Args:
    n(int): number of list and digits
    Returns: list of lists
    """
    rows = [[ for j in range(i + 1)] for i in range (n)]
    for n in range(n):
        for i in range(n - 1):
            rows[n][i + 1] = sum(rows[n =1][i:i + 2])
    return rows
