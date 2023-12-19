#!/usr/bin/python3

class Square:
    """Class Square that defines a square."""

    def __init__(self, size=0):
        """Initialize the Square instance with a private attribute: size."""
        self.__size = 0  # Default size is set to 0
        self.size = size  # Utilize the setter method for validation

    @property
    def size(self):
        """Retrieve the size of the Square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the Square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Compute the area of the Square."""
        return self.__size ** 2
