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

        self.children = {}
        self.value = None


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
        Finds the value stored in trie for a given key

        Args:
            key: string
        Returns:
            None if there is no corresponding value for a given key
            value stored for the key otherwise
        """

        node = self.start_node

        for char in key:
            if char in node.children:
                node = node.children[char]
            else:
                return None

        return node.value

    def add(self, key, value):
        """
        Adds a value for a given key to the Trie

        Args:
            key: string
            value: the value stored for the given key
        """

        node = self.start_node

        for char in key:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.value = value
