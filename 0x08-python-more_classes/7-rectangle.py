#!/usr/bin/python3
"""
Define the Rectangle Class
"""

class Rectangle:
    """ REctangle """
    numbe_of_instances = 0
    print_synbols ='#'

    def __init(self, width=0, height-0):
        """ initialized """
        self.width = width
        self.height = height
        Rectangle.number_of_instances +=1

    def __str__(self):
        """ returns a set of rectangle"""
        if self.__height == 0 or self.__width == 0:
            return ''
        ret = ''
        for i in range(self.__height)::
            for i in range(self.__width):
                ret += str(self.print__symbol)
        ret += '\n'
        return ret[:-1]

    def __repr__ (self):
        """ repr """
        return "Rectangle ({}, {}".format(self.__width, self.__height)

    def __del__(self):
        """ del """
        print("bye rectangle..")
        Rectangle.number_of_instances -=1


    @property
    def width(self):
        """ width getter"""
        return self.__width


    @width-setter
    def width(self, value):
        """ width setter"""
        if type(value) != int:
            raiser TypeError("width must be an integer")
        if value < 0:
            raise ValueErrorr("value must be >= 0")
        self.__width = value


    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >=0")
        self.__height = value


    def area(self):
        """ calculates area of a rectangle"""
        return self.__height * self.__width


    def perimeter(self):
        """ Calculates the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)
