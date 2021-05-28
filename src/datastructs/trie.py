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
            key: string
        Returns:
            None if there is no corresponding node
            else it returns the node
        """

        node = self.start_node

        for char in key:
            if char in node.children:
                node = node.children[char]
            else:
                return None

        return node

    def add(self, key):
        """
        Adds 1 to the value for every node in the path made by
        the key

        Args:
            key: string
        """

        node = self.start_node
        node.value = node.value + 1

        for char in key:

            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]
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

        results = ""
        node = self.find(key)

        while node.children != {}:

            change = False

            for symbol in node.children:

                value = node.children[symbol].value

                if limit <= value:
                    node = node.children[symbol]
                    results = results + symbol
                    change = True
                    break

                limit -= value

            if not change:
                return results

        return results
