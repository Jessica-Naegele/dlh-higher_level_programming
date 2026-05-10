#!/usr/bin/python3
""" This module defines class Node of a SLL"""


class Node:
    """Defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data with integer validation"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next_node with Node validation"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list"""

    def __init__(self):
        """Initialize the head to None"""
        self.__head = None

    def __str__(self):
        """Return a string representation of the list, one node per line"""
        values = []
        current = self.__head
        while current is not None:
            values.append(str(current.data))
            current = current.next_node
        return "\n".join(values)

    def sorted_insert(self, value):
        new_node = Node(value)

        # Case 1: Insert at the beginning (empty list or smallest value)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            # Case 2: Walk the list to find the insertion point
            current = self.__head
            while (current.next_node is not None and
                   current.next_node.data < value):
                current = current.next_node

            new_node.next_node = current.next_node
            current.next_node = new_node
