#!/usr/bin/python3
"""Module containing def read_file(filename="")"""


def read_file(filename=""):
    """Reads a file and prints to stout.

    Args:
        filename (str, optional): name of file to read. Defaults to "".
    """

    with open(filename, 'r', encoding='utf-8') as file:
        print(file.read(), end='')
