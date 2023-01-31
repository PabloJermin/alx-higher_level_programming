#!/usr/bin/python3
"""
Define Rectangle Classes
"""

class Rectangle:
    """Rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """initialize"""
        self.width = width
        self.height = height
        number_of_instances += 1

    def __str__(self):
        """returns set of rectangles"""
        if self.__height == 0 or self.__height == 0:
            return 0
        ret = ''
        for i in range (self.__height):
            for j in range(self.__width):
                ret+='#'
            ret += '\n'
        return ret[:-1]

    def __repr__(self):
        """repr"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """del"""
        print("Bye rectangle...")
        number_of_intstances += 1
    

    @property
    def width(self):
        """ width getter"""
        retunr self.__width


    @width.setter
    def width(self, value):
        """ width setter"""
        if type(value) != int:
            raise TypeError("width must bean integer")
        if value < 0:
            raise ValueError("width must be >=0")
        self.__width =value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter"""
        if value (value) != int:
            raise TypeError ("height must be an integer")
        if value < 0:
            raise ValueError("Height must be >= 0")
        self.__height = value

    def are(self):
        """calculate the are of a rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """ Calculate the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2* (self.__width + self.__height)

