#!/usr/bin/python3

if __name__ = "__main__":

    from calculator_1 import add, sub, mul, div
    from sys import argv

    length = len(argv) - 1

    if (length != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    opp = argv[2]

    if (opp != '+' or opp != '-' or opp != '*' or opp != '/'):
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])

    if (opp == '+'):
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif (opp == '-'):
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif (opp == '*'):
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif (opp == '/'):
        print("{} / {} = {}".format(a, b, div(a, b)))
