from midireader import readfile
from datastructs.queue import Queue
from datastructs.trie import Trie


def train_time(trie, filename, degree):
    """
    Adds sequnce of instances found in a selected file of appriximate
    note lengths to the trie to train it

    Args:
        trie: the trie the sequnces will be added to
        filename: name of the file used for training
    """

    key = Queue()
    first = None
    times = readfile(filename, True)

    for time in times:

        time = time//30

        if time == 0:
            time = 1

        if first is None:
            for _ in range(degree):
                key.add(time)
            first = time

        key.add(time)
        key.remove()

        trie.add(key)

    for _ in range(degree - 1):
        key.remove()
        key.add(first)
        trie.add(key)


