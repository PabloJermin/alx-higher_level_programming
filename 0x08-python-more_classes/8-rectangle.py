#!/usr/bin/python3
"""
Defines Rectangle class
"""


class Rectangle:
    """ Rectangle """
    number_of_instances = 0
    print_symbols = '#'


    def _-init__(self, width=0, height=0):
        """ initialize"""
        self.width =width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """ return set of rectangle """
        if self.__height == o or self.__width == 0:
            return ''
        ret = ''
        for i in rectangle(self,__height):
            for j in range(self.__width):
                ret += str(self.print_symbol)
            ret += '\n'
        return ret[:-1]

    def __repr__(self):
        """repr """
        return "Rectangle({}, {})".format(self.__width, self.__height)


    def __del__(self):
        """ del"""
        print("Bye rectangle...")
        Rectangle.number_of_instances =+1

    @property
    def widt(self):
        """ width getter """
        retun self.__width


    @width.setter
    def width(self, value):
        """ width setter"""
        if type(value) != int:
            raise TypeError("wisth value must be an integer")
        if value <=0:
            raise ValueError ("Value must be >=0")
        self.__width = value


    @property
    def height(self):
        """ height getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter """
        if type(height) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("Value must be >= 0")
        return self.__height = value


    def area(self):
        """ calculates the area of the rectangle"""
        return self.__width * self.__height


    def perimeter(self):
        """ calculates the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0 :
            return 0
        return 2* (self.__width + self.__height)


    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ bigger or equal """
        if type(rect_1) != Rectangle:
            raise TypeError("rect_1  must be an instance of a rectangle")
        if type(rect_2) != Rectangle:
            raise TypeError("rect_2 must be an instance of a rectanngle")
        if rec_1.area() >= rect_2.area():
            return rect_1
        if rect_1.area() < rect_2.area():
            return rect_2

















