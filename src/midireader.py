"""
This module contains the functions that can be used to tranform
the data of a midi file so it can be stored in the trie
"""
from mido import MidiFile
from transposer import find_transposing_value
from datastructs.queue import Queue


def readfile(filename: str, time=False):
    """
    Reads the midifile and pastes the infromation of right messages into a list

    Args:
        filename: name of the file read

    Returns:
        a list containing the note data in string form
    """

    data = MidiFile(f"data/training/{filename}")
    notes = Queue()

    offset = find_transposing_value(filename)
    tracks = data.tracks

    if offset is None:
        return None
    for track in tracks:
        for message in track:
            if message.type == "note_on":
                if time and message.time != 0:
                    notes.add(message.time)
                else:
                    notes.add(message.note - offset)
    return notes
    