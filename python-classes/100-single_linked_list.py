#!/usr/bin/python3
""" This module defines class Node of a SLL"""


class Node:
    """Singly Linked List with private instance data, next_node"""


    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        self.__data

    @data.setter
    def data(self, data):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        else:
            self.__data =data
    
    @property
    def next_node(self):
        self.__next_node 

    @next_node.setter
    def next_node(self, next_node):
        if next_node is not None or not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = next_node


class SinglyLinkedList:
    """Class defines a singly linked list by head"""

    def __init__(self):
        self.__head = None
        pass

    
    def sorted_insert(self, Node):
        new_node = Node(Node)
        if self.__head is None or self.__head.data >= value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while (current.next_node is not None and 
            current.next_node.data < value):
                current = current.next_node
            next = current.next_node
            current.next_node = new_node
            new_node.next_node = next

    def __str__(self):
        """Return a string representation of the list, one node per line"""
        values = []
        current = self.__head
        while current is not None:
            values.append(str(current.data))
            current = current.next_node
        return "\n".join(values)
