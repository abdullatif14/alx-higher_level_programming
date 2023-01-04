#!/usr/bin/python3

""" A function that adds 2 integers """


def add_integer(a, b=98):
    """ function that adds two integers
    or float.

    Raises: TypeError if not an integer

    """

    if type(a) is not [int, float]:
        raise TypeError('a must be an integer')
    if type(b) is not [int, float]:
        raise TypeError('b must be an integer')
    return int(a) + int(b)
