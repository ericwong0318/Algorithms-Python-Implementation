from array_sequence import ArraySequence


class DynamicArraySequence(ArraySequence):
    """
    Inheritance from array sequence

    The Python list has resizing factor 1.125 in CPython, but the factor is 2 in this class for simplicity
    """

    def __init__(self, r=2):
        super().__init__()
        self._size = 0
        self.r = r
        self._compute_bounds()
        self._resize(0)

    def __len__(self):
        return self._size

    def __iter__(self):
        for i in range(len(self)):
            yield self.a[i]

    def build(self, input_list: list):
        self._compute_bounds()
        for item in input_list:
            self.insert_last(item)

    def _compute_bounds(self):
        self.upper_bound = len(self.a)
        self.lower_bound = len(self.a) // (self.r * self.r)

    def _resize(self, n):
        if self.lower_bound < n < self.upper_bound:
            return
        a = [None] * max(n, 1) * self.r

        # copy to new array
        for i in range(self._size):
            a[i] = self.a[i]

        self.a = a
        self._compute_bounds()

    """
    Amortized time complexity is O(1) for insert_last() and delete_last(). It is better than static array's O(n)
    """

    def insert_last(self, val):
        self._resize(self._size + 1)
        self.a[self._size] = val
        self._size += 1

    def delete_last(self):
        self.a[self._size - 1] = None
        self._size -= 1
        self._resize(self._size)

    """The below methods' time complexity are O(n)"""

    def insert_at(self, i, val):
        self.insert_last(None)

        # move items backward
        for j in range(self._size, i, -1):
            self.a[j] = self.a[j - 1]

        self.a[i] = val

    def delete_at(self, i):
        # move items forward
        for j in range(i, self._size, 1):
            self.a[j] = self.a[j + 1]

        self.delete_last()

    def insert_first(self, val):
        self.insert_at(0, val)

    def delete_first(self):
        self.delete_at(0)
