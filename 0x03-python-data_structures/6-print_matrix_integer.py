#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    for x in range(matrix):

        for y in range(x):

            print("{:2d}".format(y), end="")

            if y != (len(matrix[x]) - 1):

                print(" ", end="")

        print("")
