from random import randint
from datastructs.queue import Queue


def create_sequence(trie, times, degree):
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
    last_time = Queue()

    last_time.add(2)
    last_time.add(2)

    for _ in range(degree):
        last_five.add(0)

    note = 0
    time = 2

    while note != 1:

        if note != 0:
            notes.add((note, min(time*120, 600)))

        key = Queue()
        for value in last_five:
            key.add(value)

        limit = trie.find(key).value
        rnd_note = randint(1, limit)

        limit = times.find(last_time).value
        rnd_time = randint(1, limit)

        note = trie.find_next(key, rnd_note)
        time = times.find_next(last_time, rnd_time)

        last_five.remove()
        last_five.add(note)

        last_time.remove()
        last_time.add(time)

    return notes
