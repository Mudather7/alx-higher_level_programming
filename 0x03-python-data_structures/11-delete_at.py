#!/usr/bin/python3

def delete_at(my_list=[], idx=0):

    if idx < 0 or idx >= range(len(my_list)):
        return None
    else:
        del my_list[idx]
    return my_list
