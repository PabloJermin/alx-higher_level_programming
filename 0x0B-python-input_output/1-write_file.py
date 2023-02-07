#!/usr/bin/python3
"""
1-write_file module
"""

def write_file(filename="". text=""):
    """
    write_file - wrie a strin to a text file (UTF*),
    and returns the number of characters written:
    Ars:
    filena,e: name of the file 
    text: text to be written
    Return: Number of bytes written
    """
    with open(filename, mode="w", encodin="UTF-8) as f:
    return (f.srite(text))
