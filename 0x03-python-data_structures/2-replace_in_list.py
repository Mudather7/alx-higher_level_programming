#!/usr/bin/python3

def replace_in_list(my_list, idx, element):

    if idx < 0:
        return my_list

    element = len(my_list)

    if idx < element - 1:
        return my_list

    my_list[idx] = element
    
    return my_list
