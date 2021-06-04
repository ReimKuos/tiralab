"""
This module contains the functions that can be used to tranform
the data of a midi file so it can be stored in the trie
"""
from mido import MidiFile


def convert(identifier):
    """
    A function that converts the string of messagetype into
    a simpler form

    Args:
        identifier: A string either note_on or note_off

    Return:
        a char either T or F
    """
    if identifier == "note_off":
        return "F"
    return "T"


def readfile(filename: str):
    """
    Reads the midifile and pastes the infromation of right messages into a list

    Args:
        filename: name of the file read

    Returns:
        a list containing the note data in string form
    """

    data = MidiFile(f"data/training/{filename}")
    notes = []

    for message in data:
        if message.time != 0 and message.type == "note_on":
            notes.append(f"{message.note}:184")

    return notes
