#!/usr/bin/python3

"""
Defines a method that evaluates if an object is a sub class instance
of the specified class
"""


def inherits_from(obj, a_class):
    """Evaluates if an object is a sub class instance of a_class"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
