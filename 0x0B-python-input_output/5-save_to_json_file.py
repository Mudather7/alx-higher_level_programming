#!/usr/bin/python3
'''Defineing save_to_json_file function'''


import json


def save_to_json_file(my_obj, filename):
    '''writes an Object to a text file'''
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)