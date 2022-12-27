#!/usr/bin/python3
""" Define a square """


class Square:
    """ A class that defines a square"""
    def __init__(self, size):
        """ Initialize with size"""
        if type(size) is not int:
            raise TypeError("size must be an intger")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
