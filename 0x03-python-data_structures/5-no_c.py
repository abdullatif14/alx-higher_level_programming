#!/usr/bin/python3
def no_c(my_string):
    for i in my_string:
        print(my_string.translate({ord('c', 'C', '\n'): None}))
