#!/usr/bin/python3

class Square:
    """ A class that defines a square"""
    def __init__(self, size):
        """ Instantiation with size"""
        if not isintance(size, int):
            raise TypeError("size must be an intger")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
