#!/usr/bin/python3
'''Defineing write_file function'''


def write_file(filename="", text=""):
    '''reads filename witj utf-8'''
    with open(filename, "w", encoding='utf-8') as f:
        return f.write(text)
