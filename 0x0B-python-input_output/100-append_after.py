#!/usr/bin/python3
"""Module that contains the function append_after"""


def append_after(filename="", search_string="", new_string=""):
    """Function that inserts a line of text to a file, after each line,
    containing a specific string.

    Args:
        filename (str): Name of file.
        search_string (str): String to search.
        new_string (str): String to append.
    """
    try:
        with open(filename, "r+") as file:
            lines = file.readlines()
            file.seek(0)  # Move cursor to the beginning of the file

            for line in lines:
                file.write(line)
                if search_string in line:
                    file.write(new_string + '\n')  # Append new_string after line
    
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
