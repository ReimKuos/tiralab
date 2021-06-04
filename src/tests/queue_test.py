import unittest
from datastructs.queue import Queue

class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_sum_of_values_in_empty_queue_is_zero(self):
        self.assertEqual(sum(self.queue), 0)

    def test_removing_all_makes_start_node_None(self):
        for _ in range(10):
            self.queue.add(1)
        for _ in range(10):
            self.queue.remove()
        self.assertIsNone(self.queue.start_node)

    def test_first_stays_the_same(self):
        for i in range(1, 10):
            self.queue.add(i)
        self.assertEqual(self.queue.start_node.value, 1)

    def test_removing_does_not_change_empty_queue(self):
        self.queue.remove()
        self.assertIsNone(self.queue.start_node)

    def test_remove_remoces_the_first_value(self):
        self.queue.add(1)
        self.queue.add(2)
        self.queue.remove()
        self.assertEqual(self.queue.start_node.value, 2)

    def test_values_are_in_correct_order(self):
        array = [1,2,4,4,5,6,1,12]
        for number in array:
            self.queue.add(number)
        index = 0
        for number in self.queue:
            self.assertEqual(number, array[index])
            index += 1
        

