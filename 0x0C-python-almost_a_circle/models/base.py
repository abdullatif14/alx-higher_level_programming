#!/usr/bin/python3
""" Create a class 'base' of all other classes in this project """


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
