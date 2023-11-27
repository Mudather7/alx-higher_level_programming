#!/usr/bin/python3
'''Define a class Rectangle'''


class Rectangle:
    '''Representation of a Rectangle'''

    def __init__(self, width=0, height=0):
        '''Initializes the rectangle'''
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''Calculate the area of the rectangle'''
        return self.__width * self.__height

    def perimeter(self):
        '''Calculate the perimeter of the rectangle'''
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.height * 2)

    def __str__(self):
        '''print the rectangle'''
        string = ""

        if self.__width != 0 and  self.__height != 0:
            string += "\n".join("#", self.__width
                                for i in range(self.__height))
            return string
