import unittest

from priority_queue import PriorityQueueArray, PriorityQueueSortedArray, PriorityQueueHeap

unsorted_list = [5, 3, 1, 7, 0, 8, 2, 9, 4, 6]


class TestPriorityQueueArray(unittest.TestCase):
    def test_sort(self):
        self.assertEqual([i for i in range(10)], PriorityQueueArray.sort(unsorted_list))


class TestPriorityQueueSortedArray(unittest.TestCase):
    def test_sort(self):
        self.assertEqual([i for i in range(10)], PriorityQueueSortedArray.sort(unsorted_list))


class TestPriorityQueueHeap(unittest.TestCase):
    def setUp(self) -> None:
        self.q = PriorityQueueHeap([])

    def test_max_build_heap(self):
        self.q.build_max_heap(unsorted_list)
        self.assertEqual([9, 8, 6, 7, 4, 5, 2, 0, 3, 1], self.q.a)

    def test_sort(self):
        self.assertEqual([i for i in range(10)], PriorityQueueHeap.sort(unsorted_list))


if __name__ == '__main__':
    unittest.main()
