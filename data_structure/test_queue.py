import unittest
from collections import deque

from _queue import ArrayQueue, LinkedQueue


class TestArrayQueue(unittest.TestCase):
    def setUp(self) -> None:
        self.arrayQueue = ArrayQueue()

    def test_enqueue(self):
        for i in reversed(range(10)):
            self.arrayQueue.enqueue(i)
        self.assertEqual([i for i in range(10)], self.arrayQueue.items)

    def test_dequeue(self):
        # dequeue an empty queue
        self.assertRaises(IndexError, self.arrayQueue.dequeue)

        # dequeue a non-empty queue
        for i in range(10):
            self.arrayQueue.enqueue(i)
        for i in range(5):
            self.assertEqual(i, self.arrayQueue.dequeue())
        self.assertEqual([i for i in reversed(range(5, 10))], self.arrayQueue.items)

    def test_peek(self):
        # dequeue an empty queue
        self.assertRaises(IndexError, self.arrayQueue.peek)

        # dequeue a non-empty queue
        for i in range(10):
            self.arrayQueue.enqueue(i)
        self.assertEqual(0, self.arrayQueue.peek())
        self.assertEqual([i for i in reversed(range(0, 10))], self.arrayQueue.items)

    def test_is_empty(self):
        self.assertTrue(self.arrayQueue.is_empty())
        self.arrayQueue.enqueue(0)
        self.assertFalse(self.arrayQueue.is_empty())

    def test_size(self):
        self.assertEqual(0, self.arrayQueue.size())
        for i in range(10):
            self.arrayQueue.enqueue(i)
        self.assertEqual(10, self.arrayQueue.size())


class TestLinkedQueue(unittest.TestCase):
    def setUp(self) -> None:
        self.q = LinkedQueue()

    def test_enqueue(self):
        for i in reversed(range(10)):
            self.q.enqueue(i)
        self.assertEqual(deque([i for i in range(10)]), self.q.items)

    def test_dequeue(self):
        # dequeue an empty queue
        self.assertRaises(IndexError, self.q.dequeue)

        # dequeue a non-empty queue
        for i in range(10):
            self.q.enqueue(i)
        for i in range(5):
            self.assertEqual(i, self.q.dequeue())
        self.assertEqual(deque([i for i in reversed(range(5, 10))]), self.q.items)

    def test_peek(self):
        # dequeue an empty queue
        self.assertRaises(IndexError, self.q.peek)

        # dequeue a non-empty queue
        for i in range(10):
            self.q.enqueue(i)
        self.assertEqual(0, self.q.peek())
        self.assertEqual(deque(i for i in reversed(range(0, 10))), self.q.items)

    def test_is_empty(self):
        self.assertTrue(self.q.is_empty())
        self.q.enqueue(0)
        self.assertFalse(self.q.is_empty())

    def test_size(self):
        self.assertEqual(0, self.q.size())
        for i in range(10):
            self.q.enqueue(i)
        self.assertEqual(10, self.q.size())
