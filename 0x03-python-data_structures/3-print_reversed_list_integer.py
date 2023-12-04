#!/usr/bin/python3
def print_reversed_list_integer(my_list):
    """Prints integers of a list in reverse order."""
    if not isinstance(my_list, list):
        print("Input is not a list.")
        return

    for i in range(len(my_list) - 1, -1, -1):
        print(my_list[i])
