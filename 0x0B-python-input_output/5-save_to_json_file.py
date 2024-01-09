#!/usr/bin/python3

import json

def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using its JSON representation.

    Args:
        my_obj: Python object to be serialized to JSON and written to the file.
        filename: Name of the file to which the JSON
        representation will be written.

    Note:
        Uses the `json.dump()` method to serialize `my_obj` and
        write it to `filename`.
        The file will be created or overwritten with the JSON
        representation of `my_obj`.

    Returns:
        None
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
