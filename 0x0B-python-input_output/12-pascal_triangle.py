#!/usr/bin/python3
'''defineing pascal_triangle function'''


def pascal_triangle(n):
    '''returns a list of lists of integers representing the Pascal’s triangle'''

    if n <= 0:
        return []

    array = [[1]]

    while len(array) != n:
        tri = array[-1]
        tmp = [1]

        for x in range(len(tri) - 1):
            tmp.append(tri[x] + tri[x + 1])
        tmp.append(1)
        array.append(tmp)

    return array
