#!/usr/bin/python3
""" A function that appends a string at the end"""


def append_write(filename="", text=""):
    """ it takes a filename and a text as inputs"""
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
