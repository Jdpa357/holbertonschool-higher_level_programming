#!/usr/bin/python3

"""
Defines a method to evaluate if an object is an instance of the specified class
"""


def is_same_class(obj, a_class):
    """Evaluates if the given object is an instance
    of the given class"""
    return type(obj) is a_class
