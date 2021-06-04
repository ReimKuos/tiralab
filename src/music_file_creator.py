from mido import MidiFile, MidiTrack, Message


def convert_back(value):
    """
    Converts simplifications T and F into hey corresponcif message types

    Args:
        value: charecter either T or F

    Retruns:
        either note_on or note_off
    """

    if value == "T":
        return "note_on"
    return "note_off"


def create_music(seq):
    """
    creates a midi-file based on the sequnce given as input

    Args:
        seq: list of notes in string form in order
    """

    midi = MidiFile()
    track = MidiTrack()

    midi.tracks.append(track)
    track.append(
        Message("program_change", program=0, time=0)
    )
    for note in seq:
        data = note.split(":")
        track.append(
            Message("note_on", note=int(data[0]), velocity=63, time=0
                    ))
        track.append(
            Message("note_off", note=int(data[0]), velocity=63, time=int(data[1])
                    ))

    midi.save("data/new_song.mid")
