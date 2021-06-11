"""
A module that contains the Trie structure and it's supporting class
"""


class TrieNode:
    """
    A data structure used in the Trie, stores the next nodes in the tree
    and an value
    """

    def __init__(self):
        """
        Initializes the node whith no children and 'None' foe value
        """

        self.children = [None]*129
        self.value = 0


class Trie:
    """
    A memory efficent storage structure that uses strings as keys
    """

    def __init__(self):
        """
        initializes the structure by creating a base node
        """

        self.start_node = TrieNode()

    def find(self, key):
        """
        Finds the node located in trie for a given key

        Args:
            key: a queue data structure containing a sequnce
        Returns:
            None if there is no corresponding node
            else it returns the node
        """

        node = self.start_node

        for note in key:
            if node.children[note] is not None:
                node = node.children[note]
            else:
                return None

        return node

    def add(self, key):
        """
        Adds 1 to the value for every node in the path made by
        the key

        Args:
            key: a queue data structure containing a sequnce, that points to the value wanted
        """

        node = self.start_node
        node.value = node.value + 1

        for note in key:

            if node.children[note] is None:
                node.children[note] = TrieNode()

            node = node.children[note]
            node.value = node.value + 1

    def find_next(self, key, limit):
        """
        Is used to find the next value of the markov chain,
        the limit parameter is generated as a random number in the algorithm

        Args:
            key: key for the starting node of the search
            limit: limiting value of the search

        Return:
            Note in a string form
        """

        running_total = 0
        node = self.find(key)

        for index in range(129):
            child = node.children[index]
            if child is None:
                continue
            running_total += child.value
            if limit <= running_total:
                return index

        return None
