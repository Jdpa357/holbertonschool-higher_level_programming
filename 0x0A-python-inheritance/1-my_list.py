#!/usr/bin/python3

"""Class My List to inherit"""


class MyList(list):
    """Inheritance class"""

    def print_sorted(self):
        """Prints the sorted list"""
        cp = self[:]
        cp.sort()
        print(cp)
