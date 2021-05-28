import time
from pygame import midi
from datastructs.trie import Trie
from trainer import train, create_sequence


def main():
    """
    At the moment functions as a test function for testing music
    """

    trie = Trie()
    train(trie, "mond_3.mid")
    seq = create_sequence(trie)

    midi.init()

    player = midi.Output(0)
    player.set_instrument(12)

    for note in seq:
        print(note)
        player.note_on(note, 127)
        time.sleep(0.5)
        player.note_off(note, 127)

    midi.quit()

if __name__ == "__main__":
    main()
