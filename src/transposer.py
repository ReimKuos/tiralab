from mido import MidiFile


def find_transposing_value(filename: str):
    """
    Reads the midifile and pastes the infromation of right messages into a list

    Args:
        filename: name of the file read

    Returns:
        a list containing the note data in string form
    """

    data = MidiFile(f"data/training/{filename}")
    notes = [0]*12

    for message in data:
        if message.type == "note_on":
            notes[message.note % 12] += 1

    zeroes = 0

    for number in notes:
        if number == 0:
            zeroes += 1

    for _ in range(5-zeroes):

        minimum_index = -1

        for i in range(12):

            if minimum_index == -1:
                if notes[i] != 0:
                    minimum_index = i

            elif notes[i] < notes[minimum_index] and notes[i] != 0:
                minimum_index = i

        notes[minimum_index] = 0

    first_half_step = None
    second_half_step = None

    for i in range(12):
        if notes[i] != 0 and notes[i-1] != 0:
            if first_half_step is None:
                first_half_step = i
            else:
                second_half_step = i
                break

    if second_half_step - first_half_step == 5:
        return first_half_step

    return second_half_step


if __name__ == "__main__":
    print(find_transposing_value("savelma20210612001741.mid"))
