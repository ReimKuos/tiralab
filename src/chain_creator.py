from random import randint
from midireader import get_notes


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

    notechain = ["S"]*5

    while note != "P":

        if note in cors_rev:
            notes.append(cors_rev[note])
        limit = trie.find(notechain[0] + notechain[1] +
                          notechain[2] + notechain[3] +
                          notechain[4]).value

        rnd = randint(1, limit)
        note = trie.find_next(
            notechain[0] + notechain[1] + notechain[2] + notechain[3] + notechain[4], rnd)

        for index in range(4):
            notechain[index] = notechain[index + 1]
        notechain[4] = note

    return notes
