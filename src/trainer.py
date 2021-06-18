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

    last_five = Queue()

    for _ in range(degree):
        last_five.add(0)

    notes = readfile(filename)
    if notes is None:
        return

    for primary_note in notes:
        key = Queue()
        for note in last_five:
            key.add(note)
        key.add(primary_note)

        trie.add(key)

        last_five.remove()
        last_five.add(primary_note)

    key = Queue()
    for note in last_five:
        key.add(note)

    key.add(1)
    trie.add(key)
