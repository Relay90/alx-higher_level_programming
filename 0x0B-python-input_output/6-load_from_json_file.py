#!/usr/bin/python3
"""Module containing the function load_from_json_file"""
import json


def load_from_json_file(filename):
    """Creates an Object from a JSON file.

    Args:
        filename (str): Name of the file.

    Returns:
        object: Loaded object.
    """
    with open(filename, 'r', encoding="utf-8") as file:
        loaded_object = json.load(file)
    return loaded_object
