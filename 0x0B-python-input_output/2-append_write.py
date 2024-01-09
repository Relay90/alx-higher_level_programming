#!/usr/bin/python3
"""Module containing the function append_write"""


def append_write(filename="", text=""):
    with open(filename, 'a', encoding='utf-8') as file:
        return file.write(text)
