#!/usr/bin/python3

"""
Defines a class Square that inherits from Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A Class that represents a Square"""

    def __init__(self, size):
        """Constructor method
        Args:
            size (int): is the sizes of the square
        Raise:
            TypeError - if size is not an int
            ValueError - if size is less or equals to zero
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
