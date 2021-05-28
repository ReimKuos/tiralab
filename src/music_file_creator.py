from mido import MidiFile, MidiTrack, Message


def create_music(seq):
    """
    creates a midi-file based on the sequnce given as input

    Args:
        seq: list of notes in order
    """

    midi = MidiFile()
    track = MidiTrack()

    midi.tracks.append(track)
    track.append(
        Message("program_change", program=0, time=0)
    )
    for note in seq:
        track.append(
            Message("note_on", note=note, velocity=63, time=0
                    ))
        track.append(
            Message("note_off", note=note, velocity=63, time=192
                    ))

    midi.save("data/new_song.mid")
