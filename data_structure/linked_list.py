"""
The reason why the interpreter tells you that node is an unknown type is because node must be defined before you can use
 it in an annotation.

from __future__ import annotations, which will store annotations as strings automatically.

ref: https://stackoverflow.com/questions/53695453/python-type-hints-self-referential-type-checking
"""
from __future__ import annotations


class SinglyNode:

    def __init__(self, data=0, next: SinglyNode = None):
        self.item = data
        self.next = next

    def __str__(self):
        return self.item


class SinglyLinkedList:
    def __init__(self, head: SinglyNode = None):
        self.head = head
        self.size = 0

    def __len__(self):
        return self.size

    # time O(n)
    # space O(n)
    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def to_array(self):
        return [item for item in iter(self)]

    # time O(1)
    # space O(1)
    def insert_first(self, data) -> SinglyNode:
        node = SinglyNode(data, self.head)
        self.head = node
        return node

    # insert to rear
    # time O(n) if we have rear pointer, we can achieve O(1)
    # space O(1)
    def append(self, data) -> SinglyNode:
        node = SinglyNode(data, None)
        # case 1: empty list
        if self.head is None:
            self.head = node
            return node
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = node
        return node

    # time O(n)
    # space O(1)
    def search_list(self, key) -> SinglyNode:
        curr = self.head
        while curr and curr.item != key:
            curr = curr.next
        return curr

    def delete_node(self, data) -> any:
        # case 0: empty list
        if self.head is None:
            return None
        # case 1: has 1 element
        curr = self.head
        if curr.item == data:
            self.head = curr.next
            return curr
        # case 2: has more than 1 elements
        while curr.next is not None:
            if curr.next.item == data:
                curr.next = curr.next.next
                return curr
            curr = curr.next
        return None


class DoublyNode:
    def __init__(self, data=0, prev_node=None, next_node=None):
        self.item = data
        self.prev = prev_node
        self.next = next_node

    def __str__(self):
        return self.item


class DoublyLinkedList:
    def __init__(self, head):
        self.head = head

    # get length
    # time O(1)
    # space O(1)
    def __len__(self):
        curr = self.head
        length: int = 0
        while curr is not None:
            length += 1
            curr = curr.next
        return length

    # time O(n)
    # space O(n)
    def to_array(self):
        return_arr = []
        curr = self.head
        while curr is not None:
            return_arr.append(curr.item)
            curr = curr.next
        return return_arr

    # time O(1)
    # space O(1)
    def insert_to_front(self, data):
        node = DoublyNode(data, None, self.head)
        if self.head is not None:
            self.head.prev = node
        self.head = node
        return node

    # insert to rear
    # time O(n) if we have rear pointer, we can achieve O(1)
    # space O(1)
    def append(self, data):
        # case 1: empty list
        if self.head is None:
            node = DoublyNode(data, None, self.head)
            self.head = node
            return node
        # case 2: non-empty list
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        node = DoublyNode(data, curr_node, None)
        curr_node.next = node
        return node

    # time O(n)
    # space O(1)
    def search_list(self, key):
        curr = self.head
        while curr is not None and curr.item != key:
            curr = curr.next
        return curr

    # time O(n)
    # space O(1) not ok
    def delete_node(self, data) -> any:
        # case 0: empty list
        if self.head is None:
            return None
        # case 1: has 1 element

        if self.head.item == data:
            self.head = self.head.next
            self.head.prev = None
            return self.head
        # case 2: has more than 1 elements
        curr = self.head.next
        while curr is not None:
            if curr.item == data:
                curr.prev.next = curr.next
                if curr.next is not None:  # curr is not the last element
                    curr.next.prev = curr.prev
                return curr
            curr = curr.next
