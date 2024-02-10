#!/usr/bin/python3
"""Creation of singly linked list"""


class Node:
    """defines a node of singly linked list"""

    def __init__(self, data, next_node=None):
        """ calss instantiation"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getter, to retrieve the data"""
        return self.__data

    @data.setter
    def data(self, value):
        """ setter to set value"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """retrieve the nextnode"""
        self.__next_node

    @next_node.setter
    def next_node(self, value):
        """pass value if fullfill the condition"""
        if (value is not None and not isinstance(value, Node)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """ defines singly linked lis"""

    def __init__(self):
        """ simple instantation"""
        self.head = None

    def sorted_insert(self, value):
        """ inserts a new node into correct sorted
            position in the list
        """
        new_node = Node(value)

        if not self.head:
            self.head = new_node
            return
        if value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return

        loc = self.head

        while loc.next_node and loc.next_node.data < value:
            loc = loc.next_node
        if loc.next_node:
            new_node.next_node = loc.next_node
        loc.next_node = new_node

    def __str__(self):
        """check head"""

        res = ""
        loc = self.head
        while loc:
            res += str(loc.data) + "\n"
            loc = loc.next_node
        return res[:-1]
