"""
rename this file from queue.py to _queue.py to avoid import the standard library
"""
from collections import deque


class ArrayQueue:
    """Simple array queue"""

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]


class LinkedQueue:
    def __init__(self):
        self.items = deque([])

    def is_empty(self):
        return self.items == deque([])

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.appendleft(item)

    def dequeue(self):
        return self.items.pop()

    def peek(self):
        item = self.items.pop()
        self.items.append(item)
        return item
