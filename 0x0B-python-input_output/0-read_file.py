#!/usr/bin/python3

""" Function that reads a file"""


def read_file(filename=""):
    """ Reading the entire content of the file """
    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read())
