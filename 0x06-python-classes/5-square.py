#!/usr/bin/python3
'''Defines a class Square.'''


class Square:
    '''Represents a square.'''

    def __init__(self, size=0):
        """Initializes a new Square.

        Args:
            size: length of a side of the square.

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        """
        self.__size = size

    @property
    def size(self):
        '''Property for the length a side of the square.

        Raises:
            TypeError: If size is not an integer
            ValueError: If size is less than 0
        '''
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        '''Area of the square.

        Returns:
                the size squared
        '''
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the # character."""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
