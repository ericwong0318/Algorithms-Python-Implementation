class MinHeap(object):
    def __init__(self):
        self.arr = []

    def __len__(self):
        return len(self.arr)

    # h = lg(n)
    # time O(1) + heapify O(h)
    # space O(1)
    def extract_min(self):
        # case 1: emtpy array
        if not self.arr:
            return None
        # case 2: array has one element
        if len(self.array) == 1:
            return self.arr.pop(0)
        # case 3: array has more than one element
        min = self.arr[0]  # root is first element
        self.arr[0] = self.arr.pop(-1)  # move last element to the root
        self._bubble_down(index=0)  # heapify_down
        return min

    # time O(1)
    # space O(1)
    def peek_min(self):
        return self.arr[0] if self.arr else None

    def insert(self, key):
        self.arr.append(key)
        self._bubble_up(index=len(self.arr) - 1)

    def _bubble_up(self, index):  # heapify # use while loop???
        if index == 0:
            return
        index_parent = (index - 1) // 2  # the floor division // rounds the result down to the nearest whole number
        if self.arr[index] < self.arr[index_parent]:
            # swap
            self.arr[index], self.arr[index_parent] = self.arr[index_parent], self.arr[index]
            self._bubble_up(index_parent)

    def _bubble_down(self, index):  # heapify # use while loop???
        min_child_index


