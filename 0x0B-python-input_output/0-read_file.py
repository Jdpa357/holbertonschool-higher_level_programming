#!/usr/bin/python3
"""
Defines a class that reads a file and prints it to standard ouput
"""


def read_file(filename=""):
    """Reads a text file"""
    with open(filename, 'r') as fl:
        read_data = fl.read()
    print(read_data, end="")
        
