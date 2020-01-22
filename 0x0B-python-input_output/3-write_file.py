#!/usr/bin/python3
"""
write_file module
"""


def write_file(filename="", text=""):
    """Write a string to a text file(UTF-8)"""
    with open(filename, 'w') as fl:
        writer = fl.write(text)
    return writer
