#!/usr/bin/python3
"""
===========================
Module with class MyList
===========================
"""


class MyList(list):
    def print_sorted(self):
        """Prints the list in ascending order"""
        sorted_list = sorted(self)
        print(sorted_list)
