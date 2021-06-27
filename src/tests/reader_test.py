import unittest
from midireader import readfile


class TestReader(unittest.TestCase):

    def test_normal_reading_returns_current_notes(self):
        notes = readfile("../testfile/testFile.mid")
        list_notes = [note for note in notes]
        self.assertEqual(
            list_notes,
            [18, 19, 21, 23, 24, 26, 28, 29]
        )

    def test_time_reading_returns_coreect_times(self):
        notes = readfile("../testfile/testFile.mid", True)
        list_notes = [note for note in notes]
        self.assertEqual(
            list_notes,
            [1, 1, 1, 1, 1, 1, 1, 1]
        )