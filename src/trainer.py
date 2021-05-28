"""
'Trains' the trie by using data created by midireader
"""
from midireader import get_sequence


def train(trie, filename):
    """
    Adds sequnces created to the trie

    Args:
        trie: the trie the sequnces will be added to
        filename: name of the file used for training
    """

    notechain = ["S"]*5

    for letter in get_sequence(filename):
        trie.add(notechain[0] + notechain[1] +
                 notechain[2] + notechain[3] + notechain[4] + letter)
        for index in range(4):
            notechain[index] = notechain[index + 1]
        notechain[4] = letter

    trie.add(notechain[0] + notechain[1] + notechain[2] +
             notechain[3] + notechain[4] + "P")
