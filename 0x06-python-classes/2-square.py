#!/usr/bin/python3




class Square:
    """
    Class Square that defines a square.

    Attributes:
        size (int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a square instance with a given size.

        Args:
            size (int): The size of the square (default is 0).
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """

        if type(size) != int:
            raise TypeError("size must be an integer")

        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
