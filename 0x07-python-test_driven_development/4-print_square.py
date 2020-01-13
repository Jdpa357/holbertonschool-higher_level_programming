#!/usr/bin/python3
"""
print square Module
prints a square with the character #
"""


def print_square(size):
    """This function prints a square with the character #
    using the parameter size as the number of rows and columns
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if not isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for row in range(size):
        print('#' * size)
