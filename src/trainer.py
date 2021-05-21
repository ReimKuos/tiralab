from collections import deque
from midireader import get_sequence
from trie_updater import update_trie


def train(trie, filename):

    last_six = deque()

    for _ in range(6):
        last_six.append("S")

    sequnce = get_sequence(filename)
    sequnce.append("P")

    for note in sequnce:

        last_six.popleft()
        last_six.append(note)

        current_sequence = ""

        for string in last_six:
            current_sequence.join(string)

        update_trie(trie, current_sequence)
