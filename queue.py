# queue implemented by circular array
class QueueArray:

    def __init__(self, length):
        self.queue = [None] * length
        self.head = self.tail = 0  # tail is next available slot

    # time O(1)
    # space O(1)
    def enqueue(self, element):
        # if full, resize
        if self.head == self.tail + 1:
            raise IndexError('queue is full')
        # enqueue
        self.queue[self.tail] = element
        if self.tail == len(self.queue):
            self.tail = 0
        else:
            self.tail += 1

    # time O(1)
    # space O(1)
    def dequeue(self):
        if self.size() == 0:
            raise IndexError('empty queue')
        element = self.queue[self.head]
        if self.head == len(self.queue):
            self.head = 0
        else:
            self.head += 1
        return element

    def peek(self):
        if self.size() == 0:
            raise IndexError('empty queue')
        return self.queue[self.head]

    def size(self):
        return abs(self.tail - self.head) % len(self.queue)


# queue implemented by linked list
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class QueueList(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # time O(1)
    # space O(1)
    def enqueue(self, data):
        node = Node(data)
        self.size += 1
        # case 1: empty list
        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
        # case 2: non empty list
        else:
            self.tail.next = node
            self.tail = node

    # time O(1)
    # space O(1)
    def dequeue(self):
        # case 0: empty list
        if self.size == 0:
            return None
        # case 1: non empty list
        data = self.head.data
        self.size -= 1
        # case 1.1: one element only
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # case 1.2: more than one element
        else:
            self.head = self.head.next
        return data
