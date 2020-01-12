#!/usr/bin/python3
"""
add-integer Module
adds two integers
"""


def add_integer(a, b=98):
    """This function returns the result
    of an addition between two integers
    or error if the parameters are not
    integers or float
    """

    if type(a) != int or type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int or type(b) != float:
        raise TypeError("b must be an integer")

    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)

    return a+b
