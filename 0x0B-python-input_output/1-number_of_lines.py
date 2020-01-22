#!/usr/bin/python3

"""
Number of lines module
"""


def number_of_lines(filename=""):
    """Returns the number of lines of a text file"""
    i = 0
    with open(filename, 'r') as fl:
        for line in fl:
            i = i + 1
    return i
