#!/usr/bin/python3
class Rectangle():
    """A Rectangle class"""
    def __init__(self, width=0, height=0):
        """Initialization of  the class Rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """The width of the Rectangle"""
        return self.__width__

    @width.setter
    def width(self, value):
        """Set width of the Rectangle"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width__ = value

    @property
    def height(self):
        """The height of the Rectangle"""
        return self.__height__

    @height.setter
    def height(self, value):
        """Set height of the Rectangle"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height__ = value
