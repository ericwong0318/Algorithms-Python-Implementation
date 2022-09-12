from collections import deque


class ArrayStack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        """time complexity O(1)"""
        return self.items == []

    def size(self):
        """time complexity O(1)"""
        return len(self.items)

    def push(self, item):
        """time complexity O(1)"""
        self.items.append(item)

    def pop(self):
        """time complexity O(1)"""
        return self.items.pop()

    def peek(self):
        """time complexity O(1)"""
        return self.items[-1]


class LinkedStack:
    def __init__(self):
        self.items = deque([])

    def is_empty(self):
        """time complexity O(n)"""
        return self.items == deque([])

    def size(self):
        """time complexity O(1)"""
        return len(self.items)

    def push(self, item):
        """time complexity O(1)"""
        self.items.append(item)

    def pop(self):
        """time complexity O(1)"""
        return self.items.pop()

    def peek(self):
        """
        time complexity O(1).
        self.items[-1] is fine too.
        """
        item = self.items.pop()
        self.items.append(item)
        return item
