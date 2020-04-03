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
        """
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Returns a informal representation of Square Class"""
        return "[{}] {}/{}".format("Square", self.__size, self.__size)
