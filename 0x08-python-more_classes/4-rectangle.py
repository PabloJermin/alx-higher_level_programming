#!/usr/bin/python3

"""

Defines Rectangle class

"""

class Rectangle:
    """Rectangle"""
   def __init__(self, height = 0, width= 0):
       """initialize"""
       self.width = width
       self.height = height

    def __str__(self):
        """returns set of rectangles"""
        if self.__height == 0 or self.__width == 0:
            return ''
        ret = ''
        for i in range(self.__height):
            for j in range(self.__width):
                ret += "#"
            ret += '\n'
        retun ret[:-1]

    def __repr__(self):
        """repr"""
        return "Rectangle({}, {}))".format(self.__width, self.__height)

    @property
    def width(self):
        """width getter"""
        return self.__width


    @width.setter
    def width(self, value):
        """width setter"""
        if type (value) is not int:
            raise TypeError("width must be 0")
        self.__width = value

    @propert
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >=0")
        self.__height = value

    def area(self):
        """calculate area of a rectangle """
       return self.__width * self.__height

   def perimeter(self):
       """ calculates the perimeter of a rectangle """
       if self.__height == 0 or self.__width == 0:
           return 0
       return 2 * (self.__width + self.__height)

