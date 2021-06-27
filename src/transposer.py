from mido import MidiFile


def find_transposing_value(filename: str):
    """
    Reads the midifile and creates an offset value based on the frecvensies
    of different notes which is then used to shift all training music into
    the key of C

    Args:
        filename: name of the file read

    Returns:
        An Integer value that will be used to shift the data,
        None is returned if one cannot be found
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
    if second_half_step - first_half_step == 7:
        return second_half_step
        
    return None
