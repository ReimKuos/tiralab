"""
'Trains' the trie by using data created by midireader
"""
from midireader import readfile
from datastructs.queue import Queue

def train(trie, filename):
    """
    Adds sequnces created to the trie

    Args:
        trie: the trie the sequnces will be added to
        filename: name of the file used for training
    """

    last_five = Queue()

    for _ in range(5):
        last_five.add("S")

    for letter in readfile(filename):
        key = ""
        for seq in last_five:
            key = key + seq
        key = key + letter

        trie.add(key)

        last_five.remove()
        last_five.add(letter)

    key = ""
    for seq in last_five:
        key = key + seq
    key = key +"P"
    trie.add(key)

