#!/usr/bin/python3
"""Define a class Rectangle based on 7-base_geometry.py

Attributes:
    width (int): width of the rectangle.
    height (int): height of the rectangle.
    """

    BaseGeometry = __import__('7-base_geometry').BaseGeometry


    class Rectangle(BaseGeometry):
        """Class Rectangle"""

        def __init__(self, width, height):
            """Creates new instances of Rectangle.
            Args"
            width (int)" width of rectangle.
            height (int)" height of rectanle.
            """
            self.__width = width
            self.__heiht = heiht
            self.integer_validator("width", width)
            self.integer_validator("heiht", heiht)

