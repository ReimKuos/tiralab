"""
This module contains the functions that can be used to tranform
the data of a midi file so it can be stored in the trie
"""
from mido import MidiFile


def readfile(filename: str):
    """
    Function that reads all the note_on massages in a midi file
    and saves them into an array in their integer form

    Args:
        filename: name of the file read
    Returns:
        A array containing the note values
    """

    notes = []

    for track in MidiFile(f"data/training/{filename}").tracks:
        for message in track:
            if message.type == "note_on" and message.time != 0:
                notes.append(message.note)

    return notes


def get_notes():
    """
    Function that generates a dictionary containing all the
    notes having the numbers used in midi as their keys

    Returns:
        A dictionary containing note integer forms as keys and
        notes in string form as corresponding values
    """

    notes = {}
    letters = ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]
    number = 0
    index = 0

    for key_number in range(21, 109):
        letter = letters[index]
        index = (index + 1) % 12
        if letter == "C":
            number += 1
        notes[key_number] = f"{letter}{number}"

    return notes


def get_sequence(filename: str):
    """
    Reads tranforms the array containing the integer form notes
    into a one only containing the note representations in
    string form

    Args:
        filename: the name of the file read

    Retruns:
        an array containing notes in a string form
    """

    notes = readfile(filename)
    keys = get_notes()

    return [keys[note] for note in notes]


if __name__ == "__main__":
    print(get_sequence("mond_3.mid"))
