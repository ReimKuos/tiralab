"""
This module contains the Queue and it's supporting class
"""


class QueueNode:
    """
    A simple class used to store a value and the location of the next node
    """

    def __init__(self, value):
        """
        Constructor for the node

        Args:
            value: the value that will be held by the node
        """

        self.value = value
        self.next = None


class Queue:
    """
    A class that has fast adding to the end and fast removing from the front,
    also comes with an iterator for easy use
    """

    def __init__(self):
        """
        Sets up the c and and start points of the list
        """

        self.start_node = None
        self.end_node = None
        self.node = None

    def add(self, value):
        """
        method for adding a node with a spesific value to the end of the queue

        Args:
            value: the value attached to the added ode
        """

        node = QueueNode(value)

        if self.start_node is None:
            self.start_node = node
            self.end_node = node
            return

        self.end_node.next = node
        self.end_node = node

    def remove(self):
        """
        method used for removing the first node of the queue
        """
        if self.start_node is not None:
            if self.start_node == self.end_node:
                self.end_node = None
            node = self.start_node
            self.start_node = self.start_node.next
            del node

    def __iter__(self):
        """
        A method needed for iteration sets up the starting point for
        the iteration

        Returns:
            self: the class itself
        """

        self.node = self.start_node
        return self

    def __next__(self):
        """
        A methdod used for iteration, iterates over all nodes in the linked list

        Returns:
            the value of the current node in the iteration
        """

        if self.node is not None:
            value = self.node.value
            self.node = self.node.next
            return value
        raise StopIteration
