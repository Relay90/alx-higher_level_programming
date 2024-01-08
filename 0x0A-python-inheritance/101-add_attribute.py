#!/usr/bin/python3
"""
=============================
Module with a add_attribute 
=============================
"""


def add_attribute(obj, attribute, value):
    if hasattr(obj, "__dict__"):
        obj.__dict__[attribute] = value
    else:
        raise TypeError("can't add new attribute")
