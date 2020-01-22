#!/usr/bin/python3

"""
Class Student module definition
"""


class Student:
    """Class Student definition"""

    def __init__(self, first_name, last_name, age):
        """Initialization of class Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of the instance"""
        return self.__dict__
