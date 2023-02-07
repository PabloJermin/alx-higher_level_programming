#!/usr/bin/python3
"""
append_write module
"""

def append_write(filename="", text=""):
    """
    write_file - appends a strin at the end of a text file
    and returns the number of characters added
    Ars:
    filename: name of the file 
    text: text to be written
    Returns: number of bytes written
    """
    with open (filename, mode="a", encodin="UTF-8") as f:
        return (f.write(text))
