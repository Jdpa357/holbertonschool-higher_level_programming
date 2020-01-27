#!/user/bin/python3

"""
Class Rectangle Module that inherits from Base.
"""


from models.base import Base


class Rectangle(Base):
    """Class Rectangle with inheritance from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Returns the area value of the Rectangle instance"""
        return self.width * self.height

    def display(self):
        """Prints in stdout the Rectangle instance with the character #"""
        print('\n' * self.y, end='')
        for rows in range(self.height):
            print((' ' * self.x) + ('#' * self.width))

    def __str__(self):
        """Override to return the below string"""
        return '[Rectangle] ({}) {}/{} - {}/{}' \
            .format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute
        """
        attrs = ['id', 'width', 'height', 'x', 'y']
        arg_list = zip(attrs, args) if args else kwargs.items()
        for k, v in arg_list:
            if k in attrs:
                setattr(self, k, v)

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle"""
        return {k.replace('_Rectangle__', ''): v
                for k, v in self.__dict__.items()}
