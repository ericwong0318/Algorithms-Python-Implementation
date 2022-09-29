class _PriorityQueue:
    def __init__(self, a):
        self.n, self.a = 0, a

    def __len__(self):
        return len(self.a)

    def insert(self):
        if not self.n < len(self.a):
            raise IndexError('Priority queue is overflow')
        self.n += 1

    def delete_max(self):
        if self.n < 1:
            raise IndexError('Priority queue is underflow')
        self.n -= 1

    @classmethod
    def sort(cls, a):
        """
        Sort is selection, insertion, or heap sort when inheritance class is PriorityQueueArray,
        PriorityQueueSortedArray, or PriorityQueueHeap respectively.
        """
        # build priority queue
        pq = cls(a)
        for i in range(len(a)):
            pq.insert()

        # sort by delete_max()
        for i in range(len(a)):
            pq.delete_max()
        return pq.a


class PriorityQueueArray(_PriorityQueue):
    def delete_max(self):
        """find max, similar to selection sort"""
        n, a, max_val_index = self.n, self.a, 0

        # find max and swap to array end
        for i in range(1, n):
            if a[max_val_index] < a[i]:
                max_val_index = i
        a[max_val_index], a[n - 1] = a[n - 1], a[max_val_index]

        return super().delete_max()


class PriorityQueueSortedArray(_PriorityQueue):
    def insert(self):
        """maintain a sorted array, similar to the insertion sort"""
        super().insert()
        i, a = self.n - 1, self.a
        while 0 < i and a[i] < a[i - 1]:
            a[i], a[i - 1] = a[i - 1], a[i]
            i -= 1


class PriorityQueueHeap(_PriorityQueue):
    @staticmethod
    def parent(i):
        parent = (i - 1) // 2
        return parent if 0 < i else i  # check bound

    @staticmethod
    def left(i, n):
        left = 2 * i + 1
        return left if left < n else i  # check bound

    @staticmethod
    def right(i, n):
        right = 2 * i + 2
        return right if right < n else i  # check bound

    def insert(self):
        super().insert()
        n, a = self.n, self.a
        self.max_heapify_up(a, n, n - 1)

    def delete_max(self):
        n, a = self.n, self.a
        a[0], a[n - 1] = a[n - 1], a[0]
        super().delete_max()
        self.max_heapify_down(a, self.n, 0)
        return

    def max_heapify_up(self, a, n, c):
        """swap with parent"""
        p = self.parent(c)
        if a[p] < a[c]:
            a[c], a[p] = a[p], a[c]
            self.max_heapify_up(a, n, p)

    def max_heapify_down(self, a, n, parent):
        """swap root with larger child"""
        left, right = self.left(parent, n), self.right(parent, n)

        # find and swap max between parent, left, and right
        curr = left if a[right] < a[left] else right
        if a[parent] < a[curr]:
            a[curr], a[parent] = a[parent], a[curr]
            self.max_heapify_down(a, n, curr)

    def build_max_heap(self, a):
        """Time complexity = O(n)"""
        n = len(a)
        for i in range(n // 2, -1, -1):
            self.max_heapify_down(a, n, i)
        self.a = a
