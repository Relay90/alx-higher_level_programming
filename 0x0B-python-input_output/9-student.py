#!/usr/bin/python3

import json

class Student:
    # ... (previous class definition remains the same)

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance.

        Returns:
            dict: dictionary representation.
        """
        student_dict = self.__dict__.copy()
        # For non-serializable attributes, convert to a serializable type
        # Example: Converting a custom object to a string representation
        # student_dict['custom_attribute'] = str(student_dict['custom_attribute'])
        return student_dict
