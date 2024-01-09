#!/usr/bin/python3

import json

class Student:
    # ... (previous class definition remains the same)

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance.

        If attrs is a list of strings, only attribute names contained in
        this list must be retrieved. Otherwise, all attributes must be retrieved.

        Returns:
            dict: dictionary representation.
        """
        if attrs is None:
            return self.__dict__
        
        new_dict = {}
        for item in attrs:
            if hasattr(self, item):
                value = getattr(self, item)
                if isinstance(value, (str, int, bool, list, dict)):
                    new_dict[item] = value
        return new_dict
