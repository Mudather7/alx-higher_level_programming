#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last digit = number % 10
else:
    last digit = number % -10
if last digit > 5:
    print("last digit of {} is {} and is greater than 5".format(number, last digit))
elif last digit == 0:
    print("last digit of {} is {} and is 0".format(number, last digit))
else:
    print("last digit of {} is {} and is less than 6 and not 0".format(number, last digit))
