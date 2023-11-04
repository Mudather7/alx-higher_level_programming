#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    for x in matrix:
        count = 0
        for y in x:
            count += 1
            print("{:d}".format(y), end="")
            if count < len(x):
                print(" ", end="")
        print()
