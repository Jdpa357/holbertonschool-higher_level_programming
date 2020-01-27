#!/usr/bin/python3

"""
Class Base Module
"""
import json


class Base():
    """Base Class"""

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation of list_dictionaries"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes JSON string representation of list_objs to a file"""
        if list_objs is None:
            json_string = "[]"
        else:
            json_string = cls.to_json_string([obj.to_dictionary()
                                              for obj in list_objs])
        with open(cls.__name__ + '.json', mode='w+',
                  encoding='utf-8') as a_file:
            a_file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes set"""
        new = cls(42, 42, 42)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        try:
            with open(cls.__name__ + '.json', mode='r+',
                      encoding='utf-8') as json_file:
                json_string = json_file.read()
            json_list = Base.from_json_string(json_string)
            instance_list = []
            for a_dict in json_list:
                instance_list.append(cls.create(**a_dict))
            return instance_list
        except FileNotFoundError:
            return []
