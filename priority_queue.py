# abstract data type???
# how many ADT are there?
# do ADT useful?
import sys


class Node(object):
    def __init__(self, data, key):
        self.data = data
        self.key = key


class PriorityQueue(object):
    def __init__(self):
        self.arr = []

    # time O(1), because Python store len in the field
    def __len__(self):
        return len(self.arr)

    # time O(1), Python store len in the field, so we can get last available slot in O(1)
    def insert(self, node):
        self.arr.append(node)  # node???
        return self.arr[-1]

    # O(n), heap is O(1)+heapify O(lg(n))
    # O(1)
    def extract_min(self):
        if not self.arr:  # self arr is None???
            return None
        min = sys.maxsize  # max number of sys
        for index, node in enumerate(self.arr):
            if node.key < min:  # find min in arr[]
                min = node.key
                min_index = index
        return self.arr.pop(min_index)

    # time O(n), heap is O(lg(n))
    # space O(1)
    def decrease_key(self, obj, new_key):
        for node in self.arr:
            if node.obj is obj:
                node.key = new_key
                return node
        return None
