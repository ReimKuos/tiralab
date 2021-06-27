from mido import MidiFile, MidiTrack, Message


def create_music(seq, name):
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

        track.append(
            Message("note_on", note=note[0], velocity=63, time=note[1]
                    ))

    midi.save(f"data/created/{name}.mid")
