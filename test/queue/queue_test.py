import unittest
from queue.queue import Queue

class TestQueue(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()

    def test_map_is_empty(self):
        self.assertTrue(self.queue.is_empty())

    def test_to_get_queue_size(self):
        self.assertEqual(self.queue.size(), 0)

    def test_to_enqueue(self):
        self.queue.enqueue(1)
        self.assertEqual(self.queue.size(), 1)


if __name__ == '__main__':
    unittest.main()
