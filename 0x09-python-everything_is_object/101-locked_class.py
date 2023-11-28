#!/usr/bin/python3
'''Define a locked class.'''


class LockeClass:
    '''Prevents the user from instantiaing new LockedClass  attributes
    for anything but attribute called first_name.
    '''

    __slots__ = ["First_name"]
