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
        if self.width == 0 or self.height == 0:
            return ""
        return ((("#" * self.width) + "\n") * self.height)[:-1]

    def __repr__(self):
        """Print the rectangle using eval."""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """Print a message when the rectangle is deleted."""
        print("Bye rectangle...")
