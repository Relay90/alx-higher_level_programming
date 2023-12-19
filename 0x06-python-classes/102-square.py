#!/usr/bin/python3

class Square:
    """Class Square that defines a square."""

    def __init__(self, size=0):
        """Initialize the Square instance with size."""
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the Square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the Square."""
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Compute the area of the Square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Equality comparator based on the square areas."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Non-equality comparator based on the square areas."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Less than comparator based on the square areas."""
        return self.area() < other.area()

    def __le__(self, other):
        """Less than or equal comparator based on the square areas."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Greater than comparator based on the square areas."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Greater than or equal comparator based on the square areas."""
        return self.area() >= other.area()
