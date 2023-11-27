#!/usr/bin/python3
'''Define a class Rectangle'''


class Rectangle:
    '''Representation of a Rectangle'''

    number_of_instance = 0

    def __init__(self, width=0, height=0):
        '''Initializes the rectangle'''
        self.height = height
        self.width = width
        Rectangle.number_of_instance += 1

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height
        if not type(int):
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >=0')
        self.__height = height

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        '''print the rectangle'''
        if self.width == 0 or self.height == 0:
            return ""
        return ((("#" * self.width) + "\n") * self.height)[:-1]

    def __repr__(self):
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
