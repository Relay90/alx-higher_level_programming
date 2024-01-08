#!/usr/bin/python3
"""
===================================
module with class BaseGeometry
===================================
"""


class BaseGeometry:
        """BaseGeometry class"""

    @classmethod
    def area(self):
        """Raises an Exception indicating that area() is not implemented"""
        raise Exception("area() is not implemented")
