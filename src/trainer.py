from random import randint
from datastructs.trie import Trie
from midireader import get_sequence, get_notes

def train(trie, filename):

    note_1 = "S"
    note_2 = "S"

    for letter in get_sequence(filename):
        trie.add(note_1 + note_2 + letter)
        note_1 = note_2
        note_2 = letter

    trie.add(note_1 + note_2 + "P")

def create_sequence(trie):

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
