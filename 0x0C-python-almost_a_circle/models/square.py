#!/usr/bin/python3
""" A class square that inherits from Rectangle """
from models.square import Square


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """ The class square inherits from the
        Rectangle class.
        The class constructor __init__ takes four
        argument"""

        super().__init__(size, size, x, y, id)
        """ super function is used to call methods
        of the parent class"""

        @property
        def size(self):
            return self.width

        @size.setter
        def size(self, value):
            self.width = value
            self.height = value

        def __str__(self):
            """ the __str__ method returns a string in
            format '[square] (<id>) <x>/<y> - <size>'
            where id is the id of the square , x,y are coordinates"""
            return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                     self.width)

        def update(self, *args, **kwargs):
            """ The method update checks if the
            args(id, size, x, y) exits and
            its not empty"""

            if args:
                if len(args) > 0:
                    self.id = args[0]
                if len(args) > 1:
                    self.size = args[1]
                if len(args) > 2:
                    self.x = args[2]
                if len(args) > 3:
                    self.y = args[3]

            else:
                for key, value in kwargs.items():
                    if hasattr(self, key):
                        setattr(self, key, value)

        def to_dictionary(self):
            """ Return the dictionary representation of square """
            return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
            }
