from random import randint
from datastructs.queue import Queue


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
    last_five = Queue()
    note = "S"

    for _ in range(5):
        last_five.add("S")

    while note != "P":

        if note != "S":
            notes.append(note)

        key = ""
        for seq in last_five:
            key = key + seq

        limit = trie.find(key).value
        rnd = randint(1, limit)

        note = trie.find_next(key, rnd)

        last_five.remove()
        last_five.add(note)

    return notes
