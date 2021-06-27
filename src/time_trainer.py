from midireader import readfile
from datastructs.queue import Queue
from datastructs.trie import Trie


def train_time(trie, filename):
    """
    Adds sequnce of instances found in a selected file of appriximate
    note lengths to the trie to train it

    Args:
        trie: the trie the sequnces will be added to
        filename: name of the file used for training
    """

    key = Queue()
    first = None
    last1 = None
    last2 = None

    times = readfile(filename, True)

    for time in times:

        time = time//30

        if time == 0:
            time = 1

        if first is None:
            first = time
            last1 = time
            last2 = time
            continue

        key = Queue()

        key.add(last1)
        key.add(last2)
        key.add(time)

        trie.add(key)

        last1 = last2
        last2 = time

    key = Queue()

    key.add(last1)
    key.add(last2)
    key.add(first)

    trie.add(key)

    key = Queue()

    key.add(last2)
    key.add(first)
    key.add(first)

    trie.add(key)


if __name__ == "__main__":
    train_time(Trie(), "chpn-p1.mid")
