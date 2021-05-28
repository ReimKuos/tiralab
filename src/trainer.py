"""
'Trains' the trie by using data created by midireader
"""
from random import randint
from midireader import get_sequence, get_notes

def train(trie, filename):
    """
    Adds sequnces created to the trie

    Args:
        trie: the trie the sequnces will be added to
        filename: name of the file used for training
    """

    note_1 = "S"
    note_2 = "S"

    for letter in get_sequence(filename):
        trie.add(note_1 + note_2 + letter)
        note_1 = note_2
        note_2 = letter

    trie.add(note_1 + note_2 + "P")

def create_sequence(trie):
    """
    Function that creates a note sequence using the trie

    Args:
        trie: trie that has the data that will be used to create
        the sequence

    Returns:
        The sequnce in a list form
    """

    notes = []
    cors1 = get_notes()
    cors_rev = {}

    for key in cors1:
        cors_rev[cors1[key]] = key

    note = "S"

    note_1 = "S"
    note_2 = "S"

    while note != "P":

        if note in cors_rev:
            notes.append(cors_rev[note])
        limit = trie.find(note_1 + note_2).value

        rnd = randint(1, limit)
        note = trie.find_next(note_1 + note_2, rnd)

        note_1 = note_2
        note_2 = note

    return notes
