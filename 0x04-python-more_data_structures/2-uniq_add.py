#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq = set(my_list)
    num = 0

    for i in uniq:
        num += i

    return num
