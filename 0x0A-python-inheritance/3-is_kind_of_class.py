#!/usr/bin/python3

"""
Defines a method that evaluates if an object is an instance of the same class
"""


def is_kind_of_class(obj, a_class):
    """Evaluate if a given object is an instance
    or subclass instance of a_class"""
    return isinstance(obj, a_class)
