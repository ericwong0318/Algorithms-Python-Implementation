# stack implemented by dynamic array ????
class ArrayStack:
    def __init__(self):
        self.stack = None

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size() == 0

    # time O(1)
    # space O(1)
    def push(self, data):
        self.stack.append(data)

    # time O(1)
    # space O(1)
    def pop(self):
        if self.is_empty():  # otherwise stack underflow
            return None
        else:
            return self.stack.pop()

    # time O(1)
    # space O(1)
    def peek(self):
        if self.is_empty():  # empty stack
            return None
        else:
            return self.stack[-1]


# stack implemented by linked list
class Node(object):
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node


class LinkedStack(object):
    def __init__(self, top=None):
        self.top = top
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def size(self):
        return self.size

    # time O(1)
    # space O(1)
    def push(self, data):
        self.top = Node(data, self.top)
        self.size += 1

    # time O(1)
    # space O(1)
    def pop(self):
        if self.top is None:
            return None
        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return data

    # time O(1)
    # space O(1)
    def peek(self):
        return self.top if self.top is not None else None
