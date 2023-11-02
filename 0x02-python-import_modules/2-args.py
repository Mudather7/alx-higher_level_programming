#!/usr/bin/python3

if __name__ == "__main__":

    from sys import argv

    count = len(argv) - 1

    if count == 0:
        print("0 argument.")
    elif count == 1:
        print("1 argument:")
    else:
        print("{} argument:".format(count))

    for i in range(count):
        print("{}: {}".format(i + 1, argv[i + 1]))