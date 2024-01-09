#!/usr/bin/python3
"""
===================================
module with method is_kind_of_class
===================================
"""


def inherits_from(obj, a_class):
    """Returns True if the object inherits from the specified class"""

    return issubclass(type(obj), a_class) and type(obj) != a_class
