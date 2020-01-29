#!/usr/bin/python3

"""
Class Base Module
"""
import json
import os
import csv

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
        aux = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
        aux.update(**dictionary)
        return aux

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

    @classmethod
    def save_to_file_csv(cls, data):
        """CSV"""
        if type(data) != list and data is not None:
            raise TypeError("list_objs must be a list")
        if not all(isinstance(i, cls) for i in data):
            raise TypeError("list_objs must be a list")
        filename = cls.__name__ + ".csv"
        with open(filename, "w") as f:
            if data is not None:
                data = [i.to_dictionary() for i in data]
                sfields = ['id', 'size', 'x', 'y']
                rfields = ['id', 'width', 'height', 'x', 'y']
                if cls.__name__ == "Rectangle":
                    writer = csv.DictWriter(f, fieldnames=rfields)
                else:
                    writer = csv.DictWriter(f, fieldnames=sfields)
                writer.writeheader()
                writer.writerows(data)

    @classmethod
    def load_from_file_csv(cls):
        """CSV"""
        filename = cls.__name__ + ".csv"
        sheader = ["id", "size", "x", "y"]
        rheader = ["id", "width", "height", "x", "y"]
        if cls.__name__ == "Rectangle":
            header = rheader
        else:
            header = sheader
        result = []
        if os.path.exists(filename):
            with open(filename, "r") as f:
                reader = csv.reader(f, delimiter=',')
                for i, row in enumerate(reader):
                    if i > 0:
                        new = cls(1, 1)
                        for x, y in enumerate(row):
                            if y:
                                setattr(new, header[x], int(y))
                        result.append(new)
        return result
