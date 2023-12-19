#!/usr/bin/python3

class Square:
    """Class Square that defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the Square instance with size and position."""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieve the position of the Square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the Square."""
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(val, int) for val in value)
            or any(val < 0 for val in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Compute the area of the Square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square considering position."""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Return the string representation of the Square."""
        string_representation = ''
        if self.__size == 0:
            return string_representation
        else:
            for i in range(self.__position[1]):
                string_representation += '\n'
            for i in range(self.__size):
                string_representation += ' ' * self.__position[0] + '#' * self.__size + '\n'
        return string_representation[:-1]
