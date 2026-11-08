#!/usr/bin/python3
"""Defines a Node and a sorted SinglyLinkedList of integers."""


class Node:
    """Represents one node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize the node.

        Args:
            data (int): The value stored in the node.
            next_node (Node): The following node, or None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get or set the integer stored in the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data after checking it is an integer."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get or set the node that follows this one."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node after checking it is a Node or None."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked list kept in increasing order."""

    def __init__(self):
        """Initialize an empty list."""
        self.__head = None

    def __str__(self):
        """Return the list values, one per line."""
        values = []
        node = self.__head
        while node is not None:
            values.append(str(node.data))
            node = node.next_node
        return "\n".join(values)

    def sorted_insert(self, value):
        """Insert a new Node holding value at its sorted position.

        Args:
            value (int): The value to insert.
        """
        new = Node(value)
        if self.__head is None or value < self.__head.data:
            new.next_node = self.__head
            self.__head = new
            return
        node = self.__head
        while node.next_node is not None and node.next_node.data < value:
            node = node.next_node
        new.next_node = node.next_node
        node.next_node = new
