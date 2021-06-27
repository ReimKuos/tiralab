import unittest
from transposer import find_transposing_value

class TestReader(unittest.TestCase):

    def test_transposer_finds_the_correct_value(self):
        value = find_transposing_value("../testfile/testFile.mid")
        self.assertEqual(value, 5)
