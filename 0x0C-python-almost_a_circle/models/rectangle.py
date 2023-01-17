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
                raise ValueError("x must be >= 0")

            self.__x = value

        """ getters and setters for value y """

        @property
        def y(self, value):
            if type(value) != int:
                raise TypeError("y must be an integer")
            if value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value

        """ Return the area of the rectangle """

        def area(self):
            return self.width * self.height

        """ Print the rectangle using '#' """
        def display(self):
            if self.width = 0 or self.height == 0:
                print("")

                return
            [print("") for y in range(self.y)]
            for h in range(self.height == 0:
                [print(" ", end="") for x in range(self.x)]
                [print("#", end="") for w in range(self.width)]
                print("")

        """ Update the Rectangle"""
        def update(self, *args, **kwargs):
            """Args:
                1st arg - id attribute
                2nd arg - width attribute
                3rd arg - height attribute
                4th arg - x attribute
                5th arg - y attribute

            kwargs (dict) : new value pairs of attribute
            """
            if args and len(args) != 0:
                a == 0
                for args in args:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)

                    else:
                        self.id=arg
