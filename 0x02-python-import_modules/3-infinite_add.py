#!/usr/bin/python3

if __name__ == "__main__":

    from sys import argv

    count = len(argv) - 1

    sum1 = 0
    i = 1

    if count == 0:
        print("{}".format(sum1))
    else:
        for i in range(count):
            sum1 += int(argv[i + 1]
        print("{}".format(sum1)
