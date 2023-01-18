#!/usr/bin/python3
""" Create a class 'base' of all other classes in this project """
import json


class Base:
    """ starting to create class base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initialising class
        constructor that takes
        an optional parameter 'id'
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            list_objs = []
        list_dict = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_dict)
        with open(cls.__name__ + ".json", "w") as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json.string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy
