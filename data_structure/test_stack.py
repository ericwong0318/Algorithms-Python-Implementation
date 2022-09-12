from collections import deque
from unittest import TestCase

from stack import ArrayStack, LinkedStack


class TestArrayStack(TestCase):
    def setUp(self) -> None:
        self.arrStack = ArrayStack()

    def test_push(self):
        for i in range(10):
            self.arrStack.push(i)
        self.assertEqual([i for i in range(10)], self.arrStack.items)

    def test_pop(self):
        # pop an empty stack
        self.assertRaises(IndexError, self.arrStack.pop)

        # pop a non-empty stack
        for i in range(10):
            self.arrStack.push(i)
        for i in range(9, 4, -1):
            self.assertEqual(i, self.arrStack.pop())
        self.assertEqual([i for i in range(5)], self.arrStack.items)

    def test_peek(self):
        # peek an empty stack
        self.assertRaises(IndexError, self.arrStack.peek)

        # peek a non-empty stack
        self.arrStack.push(0)
        self.assertEqual(0, self.arrStack.peek())

    def test_is_empty(self):
        self.assertTrue(self.arrStack.is_empty())
        self.arrStack.push(0)
        self.assertFalse(self.arrStack.is_empty())

    def test_size(self):
        self.assertEqual(0, self.arrStack.size())
        for i in range(10):
            self.arrStack.push(i)
        self.assertEqual(10, self.arrStack.size())


class TestLinkedStack(TestCase):
    def setUp(self) -> None:
        self.linkedStack = LinkedStack()

    def test_push(self):
        for i in range(10):
            self.linkedStack.push(i)
        self.assertEqual(deque([i for i in range(10)]), self.linkedStack.items)

    def test_pop(self):
        # pop an empty stack
        self.assertRaises(IndexError, self.linkedStack.pop)

        # pop a non-empty stack
        for i in range(10):
            self.linkedStack.push(i)
        for i in range(9, 4, -1):
            self.assertEqual(i, self.linkedStack.pop())
        self.assertEqual(deque(i for i in range(5)), self.linkedStack.items)

    def test_peek(self):
        # peek an empty stack
        self.assertRaises(IndexError, self.linkedStack.peek)

        # peek a non-empty stack
        self.linkedStack.push(0)
        self.assertEqual(0, self.linkedStack.peek())

    def test_is_empty(self):
        self.assertTrue(self.linkedStack.is_empty())
        self.linkedStack.push(0)
        self.assertFalse(self.linkedStack.is_empty())

    def test_size(self):
        self.assertEqual(0, self.linkedStack.size())
        for i in range(10):
            self.linkedStack.push(i)
        self.assertEqual(10, self.linkedStack.size())
