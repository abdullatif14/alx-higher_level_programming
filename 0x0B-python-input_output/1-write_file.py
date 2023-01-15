#!/usr/bin/python3
""" Function that writes a string to a text file """


def write_file(filename="", text=""):
    """ it takes filename and text as inputs """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
