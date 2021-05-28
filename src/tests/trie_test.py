import unittest
from datastructs.trie import Trie


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_non_existing_key_retruns_none(self):
        self.assertIsNone(self.trie.find("test"))

    def test_value_can_be_stored(self):
        self.trie.add("test")
        self.assertEqual(1, self.trie.find("test").value)

    def test_interferance_does_not_happen(self):
        self.trie.add("test")
        self.trie.add("tests")
        self.assertEqual(2, self.trie.find("test").value)

    def test_find_next_portions_are_correct(self):
        for _ in range(100):
            self.trie.add("testA")
        for _ in range(200):
            self.trie.add("testB1")
        for _ in range(200):
            self.trie.add("testB2")
        for _ in range(300):
            self.trie.add("test")

        keys = {
            "A": 0,
            "B1": 0,
            "B2": 0,
            "": 0
        }

        for limit in range(1, 801):
            keys[self.trie.find_next("test", limit)] += 1

        self.assertEqual((100, 200, 200, 300),
                         (keys["A"], keys["B1"], keys["B2"], keys[""]))
