from pygame import time
from pygame import midi
from datastructs.trie import Trie
from trainer import train, create_sequence


def main():
    """
    Is supposed to call the algorithm and play music, but at thi moment just
    reads a one file and saves the results in the trie, this function will be moved
    elsewhere later.
    """
    trie = Trie()
    train(trie, "mond_3.mid")
    seq = create_sequence(trie)

    clock = time.Clock()
    clock.tick(6)

    midi.init()

    player = midi.Output(0)
    player.set_instrument(12)

    for note in seq:
        print(note)
        player.note_on(note, 127)
        clock.tick(6)
        player.note_off(note, 127)

    midi.quit()

if __name__ == "__main__":
    main()
