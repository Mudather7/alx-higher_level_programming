#!/usr/bin/python3

def safe_print_division(a, b):

    try:
        result = a / d

    except (ZeroDivisionError, TypeError):

        pass

    finally:

        print("Inside result: {}".format(result))

        return result