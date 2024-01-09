#!/usr/bin/python3

import json

def load_from_json_file(filename):
    """
    Creates a Python object from a JSON file.

    Args:
        filename (str): Name of the JSON file to load the object from.

    Returns:
        Python object: The object represented by the JSON content of the file.

    Notes:
        Uses the `json.load()` method to read the content from the specified JSON file
        and convert it into a Python object. The file must contain valid JSON data
        representing an object.

        If the file doesn't exist or the JSON content is not correctly formatted,
        an error message is displayed.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
