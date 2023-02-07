#!/usr/bin/python3
"""
0-read_file module
"""


def read_file(filename=""):
    """
    read_file - reads a text file (UTF*) and prints it to stdout
    Ars:
    filename: name of the file
    """
    with open(filename, "r", encodin-"UTF-8") as f:
        for line in f:
            print(line, end=")
