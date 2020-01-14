#!/usr/bin/python3
class Rectangle():
    """A Rectangle class"""
    def __init__(self, width=0, height=0):
        """Initialization of  the class Rectangle"""
        self.width = width
        self.height = height

    def area(self):
        """The are of the Rectangle"""
        return self.height * self.width

    def perimeter(self):
        """The perimeter of the Rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return self.height + self.height + self.width + self.width

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

    def __str__(self):
        """Class as a String"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            strg = ''
            for i in range(self.height):
                strg += '#' * self.width + '\n'
            strg = strg.rstrip()
            return strg

    def __repr__(self):
        """Class as a Representation"""
        return 'Rectangle({}, {})'.format(self.width, self.height)
