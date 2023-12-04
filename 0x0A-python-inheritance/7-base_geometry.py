#!/usr/bin/python4
'''Module for base_geometry class.'''

class BaseGeometry:
    '''A BaseGeometry calss'''
    def area(self):
        '''Methods to compute this area'''
        raise Exception('area() is not implemented')
    def integer_validator(self, name, value):
        '''Method for validing the value'''
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
