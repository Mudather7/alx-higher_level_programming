#!/usr/bi/python3
'''Module for print_square method'''


def print_square(size):
    '''Method for printing a square with a character #.

    Args:
        size: the size length of the square.

    Raises:
        TypeError: If the size is not an integer.
        TypeError: If size is a float and is less than zero.
        ValueError: If size is less than zero.
    '''

    if not isinstance(size, int):
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')

    print((("#" * size + "\n") * size), end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
