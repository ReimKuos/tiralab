"""
this module contains the function used for updating trie class,
will probabily be implemented as part of the Trie class later
"""


def update_trie(trie, key):
    """
    Args:
        trie: Trie that will be updated
        key: location for the value to be updated
    """

    current = trie.find(key)

    if current is not None:
        trie.add(key, current + 1)
    else:
        trie.add(key, 1)
