#!/usr/bin/python3
""" Module for minOperations function """

def minOperations(n):
    """ Determined minimum number of operations to result in exactly n numbers
    of character H. retunrs ) if impossible"""
    if n == 1:
        return 0
    total_operations = 2
    total_chars = 2
    clipboard = 1
    remnant = n - total_chars
    while total_chars < n:
        if clipboard > remnant:
            return 0
        if remnant % total_chars:
            total_chars += clipboard
            total_operations += 1
            remnant = n - total_chars
        else:
            clipboard = total_chars
            total_chars += clipboard
            total_operations += 2
            remnant = n - total_chars
    return total_operations if total_chars == n else 0

