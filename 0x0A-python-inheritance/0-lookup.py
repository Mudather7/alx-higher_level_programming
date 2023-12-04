#!/usr/bin/python3
'''Module for looking for a method.'''


def lookup(obj):
    '''Looks up object attributes and methods.

    Args:
        obj: the object to list

    Return:
        list: the list of attributes.
    '''

    return dir(obj)
