from mido import MidiFile


def readfile(filename: str):

    notes = []

    for track in MidiFile(f"data/training/{filename}").tracks:
        for message in track:
            if message.type == "note_on":
                notes.append(message.note)

    return notes


def get_notes():
    """
    Function that generates a dictionary containing all the
    notes having the numbers used in midi as their keys
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

    notes = readfile(filename)
    keys = get_notes()

    return [keys[note] for note in notes]


if __name__ == "__main__":
    print(get_sequence("mond_3.mid"))
    print(get_notes())
