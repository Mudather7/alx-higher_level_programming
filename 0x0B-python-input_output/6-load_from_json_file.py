#!/usr/bin/python3
'''Defineing loas_from_json_file function'''


import json


def load_from_json_file(filename):
    ''' creates an Object from json file'''
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
