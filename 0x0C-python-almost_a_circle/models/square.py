#!/usr/bin/python3
"""
Class Square Module
"""
from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square with inheritance from Base and Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value
        self.width = value
        self.height = value

    def __str__(self):
        """Override to return the below"""
        return '[Square] ({}) {}/{} - {}' \
            .format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """Assigns an argument to each attribute"""
        attrs = ['id', 'size', 'x', 'y']
        arg_list = zip(attrs, args) if args else kwargs.items()
        for k, v in arg_list:
            if k in attrs:
                setattr(self, k, v)

    def to_dictionary(self):
        """Returns the dictionary representation of Square"""
        new_dict = {k.replace('_Square__', '').replace('_Rectangle__', ''): v
                    for k, v in self.__dict__.items()}
        del_keys = ['width', 'height']
        for i in del_keys:
            del new_dict[i]
        return new_dict
