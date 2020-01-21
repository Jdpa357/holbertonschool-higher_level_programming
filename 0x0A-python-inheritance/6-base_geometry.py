#!/usr/bin/python3

"""
Defines a class with unimplemented Area method
"""


class BaseGeometry():
    """A Class that represent a geometry form"""
    def area(self):
        """Returns the area of the Rectangle"""
        raise Exception("area() is not implementhed")
