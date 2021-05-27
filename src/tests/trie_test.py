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