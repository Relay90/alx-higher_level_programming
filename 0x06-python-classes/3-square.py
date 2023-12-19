#!/usr/bin/python3

class Square:
    """Class Square that defines a square."""

    def __init__(self, size=0):
        """Initialize the Square instance with a private attribute: size."""
        self.__size = 0  # Default size is set to 0

        if not isinstance(size, int):
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Compute the area of the Square."""
        return self.__size ** 2
