from mido import MidiFile, MidiTrack, Message
from random import choice


def create_music(seq, name):
    """
    creates a midi-file based on the sequnce given as input

    Args:
        seq: list of notes in string form in order
    """

    midi = MidiFile()
    track = MidiTrack()

    count = 8
    base = 0

    midi.tracks.append(track)
    track.append(
        Message("program_change", program=0, time=0)
    )
    for note in seq:

        if count == 8:
            count = 0
            track.append(
                Message("note_off", note=base, velocity=63, time=0
                        ))
            track.append(
                Message("note_on", note=note, velocity=63, time=0
                        ))
            base = note

        track.append(
            Message("note_on", note=note, velocity=63, time=0
                    ))
        track.append(
            Message("note_off", note=note, velocity=63, time=184
                    ))

    midi.save(f"data/created/{name}.mid")
