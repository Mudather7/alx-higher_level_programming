#!/usr/bin/python3
'''Module for test_indentation method'''


def text_indentation(text):
    '''Method for adding two new line after '.?:' chars.

    Args:
        text: the string text.

    Raises:
        TypeError: If text is not a string.
    '''

    if not isinstance(text, str):
        raise TypeError('text must be a string')

    for delim in ".?:":
        # print(delim, text.split(delim))
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print(text, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
