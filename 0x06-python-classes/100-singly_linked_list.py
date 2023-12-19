#!/usr/bin/python3

class Node:
    """Class Node that defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize the Node instance with data and next_node."""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data of the Node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the Node."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next_node of the Node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next_node of the Node."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Class SinglyLinkedList that defines a singly linked list."""

    def __init__(self):
        """Initialize the SinglyLinkedList with head as None."""
        self.head = None

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position in the list."""
        new_node = Node(value)

        if self.head is None or self.head.data >= value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node

            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Print the entire list in stdout, one node number by line."""
        elements = []
        current = self.head
        while current is not None:
            elements.append(str(current.data))
            current = current.next_node
        return '\n'.join(elements)
