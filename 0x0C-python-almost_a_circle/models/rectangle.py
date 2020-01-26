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

    def validation(self, name, value):
        """Validates all setter methods and instantiation"""
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if (name is 'x' or name is 'y') and value < 0:
            raise ValueError('{} must be >= 0'.format(name))
        if (name is 'width' or name is 'height') and value <= 0:
            raise ValueError('{} must be > 0'.format(name))

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validation('width', value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validation('height', value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validation('x', value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validation('y', value)
        self.__y = value

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
