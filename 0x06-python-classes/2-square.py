#!/usr/bin/python3
'''Defines a class Square.'''


class Square:
    '''Represents a square.'''

    def __init__(self, size):
        """Initializes a new Square.

        Args:
            size: length of a side of the square.

        Raises:
            TypeError: If size is not an integer
            ValuoError: If size is less than 0
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
