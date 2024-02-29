import unittest
from .max_heap import MaxHeap


class TestMaxHeap(unittest.TestCase):


    def test_insert(self):
        test_heap = MaxHeap(5)
        test_heap.insert(4)
        test_heap.insert(5)
        test_heap.insert(1)
        test_heap.insert(10)
        expected_heap = [10,5,1,4]
        self.assertEqual(test_heap, expected_heap)