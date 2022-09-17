class ArraySequence:
    """
    This class implements an array using basic operations, so no append() etc.
    """

    def __init__(self):
        self.a = []
        self._size = 0

    def __len__(self):
        return self._size

    def __iter__(self):
        yield from self.a

    def build(self, input_list: list):
        """Although Python's list is not static array, pretend it is and build a static array from input array"""
        self.a = [item for item in input_list]
        self._size = len(input_list)

    def get_at(self, i):
        return self.a[i]

    def set_at(self, i, val):
        self.a[i] = val

    """The below methods have time complexity O(n)."""

    def insert_at(self, i, val):
        """
        Build a new array with new inserted value, having length n + 1
        """
        n = len(self)
        a = [None for _ in range(n + 1)]
        for j in range(i):
            a[j] = self.a[j]
        a[i] = val
        for j in range(i, n):
            a[j + 1] = self.a[j]
        self.build(a)

    def delete_at(self, i):
        """Build a new array with new inserted value, having length n - 1"""
        n = len(self)
        a = [None for _ in range(n - 1)]

        # 2 pointers
        stub = "skipped"
        self.a[i] = stub
        runner, walker = 0, 0
        while runner < n:
            if self.a[runner] == stub:
                runner += 1
                continue
            a[walker] = self.a[runner]
            runner += 1
            walker += 1
        self.build(a)

    def insert_first(self, val):
        self.insert_at(0, val)

    def delete_first(self):
        self.delete_at(0)

    def insert_last(self, val):
        self.insert_at(len(self.a), val)

    def delete_last(self):
        self.delete_at(len(self.a) - 1)
