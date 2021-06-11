import unittest
from datastructs.trie import Trie
from datastructs.queue import Queue


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        self.key = Queue()

    def test_non_existing_key_retruns_none(self):
        self.key.add(100)
        self.assertIsNone(self.trie.find(self.key))

    def test_value_can_be_stored(self):
        for i in range(10):
            self.key.add(i)
        self.trie.add(self.key)
        self.assertEqual(1, self.trie.find(self.key).value)

    def test_interferance_does_not_happen(self):
        self.key.add(1)
        self.trie.add(self.key)
        self.key.add(2)
        self.trie.add(self.key)
        self.key.remove()
        self.key.remove()
        self.key.add(1)
        self.assertEqual(2, self.trie.find(self.key).value)

    def test_find_next_works(self):
        self.key.add(1)
        self.key.add(1)
        self.key.add(1)
        self.trie.add(self.key)
        self.key.remove()
        self.assertEqual(1, self.trie.find_next(self.key, 1))
