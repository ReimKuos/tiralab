"""
'Trains' the trie by using data created by midireader
"""
from midireader import readfile
from datastructs.queue import Queue


def train(trie, filename, degree):
    """
    Adds sequnce instances found in a selected file to the trie to train it

    Args:
        trie: the trie the sequnces will be added to
        filename: name of the file used for training
    """

    key = Queue()

    for _ in range(degree):
        key.add(0)

    notes = readfile(filename)
    if notes is None:
        return

    for primary_note in notes:
        key.add(primary_note)
        trie.add(key)
        key.remove()

    key.add(1)
    trie.add(key)
