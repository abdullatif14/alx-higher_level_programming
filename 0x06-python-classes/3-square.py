#!/usr/bin/python3

""" A class that defines a square"""


class Square:
    """ Defining the class Sqaure"""
    def __init__(self, size=0):
        """ initialize size"""
        if type(size) is not int:
            raise TypeError("size must be integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
