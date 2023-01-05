#!/usr/bin/python3

""" A function that prints a square with a character """


def print_square(size):
    """ defining the function, size is the length of the square"""
    if not isinstance(size, int):
        if isinstance(size, float) an d size < 0:
            raise TypeError('size must be an integer')
        raise TypeError('size must be an integer')

    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        print('#' * size)
