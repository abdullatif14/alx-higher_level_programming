#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    return (sorted(a_dictionary.items(), key=lambda item: item[1]))
