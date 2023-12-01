#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """
    Add elements of two tuples and return a new tuple.

    Args:
    - tuple_a (tuple): First tuple (default is an empty tuple)
    - tuple_b (tuple): Second tuple (default is an empty tuple)

    Returns:
    - tuple: A new tuple containing the element-wise sum of the input tuples
    """

    # Ensure tuple_a has at least two elements by padding with zeros if necessary
    if len(tuple_a) < 2:
        if len(tuple_a) == 0:  # If tuple_a is empty
            tuple_a = 0, 0
        else:  # If tuple_a has only one element
            tuple_a = tuple_a[0], 0

    # Ensure tuple_b has at least two elements by padding with zeros if necessary
    if len(tuple_b) < 2:
        if len(tuple_b) == 0:  # If tuple_b is empty
            tuple_b = 0, 0
        else:  # If tuple_b has only one element
            tuple_b = tuple_b[0], 0

    # Calculate the sum of elements at corresponding indices and return a new tuple
    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
