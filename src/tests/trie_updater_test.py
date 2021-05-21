import unittest
from datastructs.trie import Trie
from trie_updater import update_trie


class TestTrieUpdater(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_no_value_is_turned_to_one(self):
        update_trie(self.trie, "test")
        self.assertEqual(self.trie.find("test"), 1)

    def test_existing_value_is_increased_by_one(self):
        self.trie.add("test", 10)
        update_trie(self.trie, "test")
        self.assertEqual(self.trie.find("test"), 11)
