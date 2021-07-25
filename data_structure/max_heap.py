import math


class MaxHeap:
    def __init__(self):
        self.a = []
        self.size = 0

    def __len__(self):
        return self.size

    def parent(self, i):
        return math.floor(i / 2)

    def left(self, i):
        return 2 * i + 1

    def right(self, i):
        return 2 * i + 2

    def max_heapify(self, i: int):
        """
        let a[i] float down into max-heap
        :param i: index of element
        :return a:
        """
        left = self.left(i)
        right = self.right(i)

        # find largest: index of largest element
        # the element may not have right child, so we compare left the root first
        if left <= len(self.a) and self.a[left] > self.a[right]:
            largest = left
        else:
            largest = i
        if right <= len(self.a) and self.a[right] > self.a[left]:
            largest = right

        # swap with largest
        if largest != i:
            self.a[i] = self.a[largest], self.a[largest] = self.a[i]
            self.max_heapify(largest)

    def build_max_heap(self):
        """
        convert array into max heap
        time complexity O(n*lg(n))
        """
        self.size = len(self.a)
        for i in range(math.floor(len(self.a) / 2), 0):
            self.max_heapify(i)

    def heapsort(self):
        """
        extreact max each time to sort the element
        time: O(n*lg(n))
        """
        self.build_max_heap()
        for i in range(len(self.a), 1):
            self.a[0] = self.a[i], self.a[i] = self.a[0]
            self.size -= 1
            self.max_heapify(0)

    def max(self):
        return self.a[0]

    def extract_max(self):
        """
        time: O(lg(n))
        """
        if self.size <= 0:
            raise IndexError('heap underflow')
        max = self.a[0]
        self.a[0] = self.a[self.size]
        self.size -= 1
        self.max_heapify(0)
        return max

    def increase_key(self, i, key):
        """
        increase element i's priority to key
        time O(lg(n))
        :param i: index
        :param key: priority
        """
        if key < self.a[i]:
            raise KeyError('new key is smaller than current key')
        self.a[i] = key
        # swap with parents
        while i > 0 and self.a[i] > self.a[self.parent(i)]:
            self.a[i] = self.a[self.parent(i)], self.a[self.parent(i)] = self.a[i]
            i = self.parent(i)

    def insert(self, key):
        """
        create new element at the end of the array a and increase it to priority key
        time O(lg(n))
        :param key: priority key
        """
        self.size += 1
        self.a[self.size] = -math.inf
        self.increase_key(self.size, key)
