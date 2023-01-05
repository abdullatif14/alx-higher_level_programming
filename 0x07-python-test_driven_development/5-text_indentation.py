#!/usr/bin/python3

""" Function that prints 2 new
lines after each character """


def text_indentation(text):
    """ text must be a string """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    indent = False

    for char in text:
        if char in '.?:':
            indent = True
            print(char, end='')

        else:
            if indent:
                print('\n\n', end='')
                indent = False

            print(char, end='')
