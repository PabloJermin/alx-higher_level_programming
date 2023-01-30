#!/usr/bin/python3

"""

Defines Rectangle class

"""

class Rectangle:
    """ Rectangle """
    def __init__(self, width=0, height=0):
        """initialize"""
        self.width = width
        self.height = height

    def __str__(self):
        """return set of rectangles"""
        if self.__height ==0 or self.__width == 0:
            return 0
        ret = ''
        for i in rectangle(self.__height):
            for j in range(self.__width):
                ret+='#'
        return ret[:-1]
    
    def __repr__(self):
        """ repr"""
        print("Bye rectangle..")

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter"""
        if type(value) != int:
            raise TypeError ("height must be an integer")
        if value < 0 :
            raise ValueError("height must be ?= 0")
        self.__height = value

    def area(self):
        """ Calculation of the are of a rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Calculate the perimeter of a rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.width + self.++height)


