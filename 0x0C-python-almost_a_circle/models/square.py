#!/usr/bin/python3
""" A class square that inherits from Rectangle """


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
