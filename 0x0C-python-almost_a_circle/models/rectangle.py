#!/usr/bin/python3
""" A rectangle class that inherits from Base class """


class Rectangle(Base):
    """ creating the rectangle class that inherits base class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ class constructors with private instance attributes """
        super().__init__(id)
        """ super class with id - calls the
        use of __init__ of the Base class """
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, value):
            if type(value) != int:
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.width = value

        """ getters and setter for height """
        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            if type(value) != int:
                raise TypeError("height must be an integer")
            if value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value

        """ setters and getters for value x """
        @property
        def x(self):
            return self.__x

        @x.setter
        def x(self, value):
            if type(value) != int:
                raise TypeError("x must be an integer")
            if value < 0:
                raise ValueError("x must be > 0")

            self.__x = value

        """ getters and setters for value y """

        @property
        def y(self, value):
            if type(value) != int:
                raise TypeError("y must be an integer")
            if value < 0:
                raise ValueError("y must be > 0")
            self.__y = value
