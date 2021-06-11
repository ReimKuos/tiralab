from random import randint
from datastructs.queue import Queue


def create_sequence(trie, degree):
    """
    Function that creates a note sequence using the trie

    Args:
        trie: trie that has the data that will be used to create
        the sequence

    Returns:
        The sequnce in a list form
    """

    notes = Queue()
    last_five = Queue()
    note = 0

    for _ in range(degree):
        last_five.add(0)

    while note != 1:

        if note != 0:
            notes.add(note)

        key = Queue()
        for value in last_five:
            key.add(value)

        limit = trie.find(key).value
        rnd = randint(1, limit)

        note = trie.find_next(key, rnd)

        last_five.remove()
        last_five.add(note)

    return notes
