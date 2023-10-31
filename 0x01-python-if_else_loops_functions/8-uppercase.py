#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= ord('a') and ord(i) <= ord('z'):
              char = chr(ord(i) - 32)
        else:
            char = i
         print("{:c}".format(ord(i) - num), end="")
    print('')
