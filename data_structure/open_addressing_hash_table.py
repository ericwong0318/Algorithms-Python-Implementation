class OpenAddressingHashTable(object):
    """
    This class uses double hashing to support insert, delete and search.
    Uniform hashing is difficult to implement. But in reality double hashing is
     good enough.

    +----------------------------+----------------+
    | Probe sequence computation | Probe sequence |
    +----------------------------+----------------+
    | Universal hashing          | O(m!)          |
    | Linear probing             | O(m)           |
    | Quadratic probing          | O(m)           |
    | Double hashing             | O(m**2)        |
    +----------------------------+----------------+

    """

    def __init__(self):
        self.capacity = 2
        self.size = 0
        self.ht = [None] * self.capacity

        self.h = self.double_hashing

    """2 probing methods: double_hashing and perfect_hashing, not finished"""

    def double_hashing(self, k, i) -> int:
        h1 = k % self.capacity
        h2 = 1 + (k % (self.capacity - 1))
        return (h1 + i * h2) % self.capacity

    """hash table's functions"""

    # noinspection PyTypeChecker
    def hash_insert(self, k: int) -> None:
        # i = 0
        # while i != self.size:
        #     j = self.h(x, i)
        #     if self.ht[j] is None or self.ht[j] == 'deleted':
        #         self.ht[j] = x
        #         return j
        #     else:
        #         i += 1
        # print("full")
        for i in range(self.capacity):
            j = self.h(k, i)
            if self.ht[j] is None:
                self.ht[j] = k
                self.size += 1
                return
        self.table_doubling()  # table is full

    def hash_search(self, k) -> int or None:
        """find item until find None or have searched equal to size time"""
        # i = 0
        # j = self.h(k, i)
        # while self.ht[j] is not None or i == self.size:
        #     j = self.h(k, i)
        #     if self.ht[j] == k:
        #         return j
        #     i += 1
        # return None
        for i in range(self.capacity):
            j = self.h(k, i)
            if self.ht[j] is None:
                return None
            elif self.ht[j] == k:
                return j
        return None  # exhausted table

    # noinspection PyTypeChecker
    def hash_delete(self, k) -> int or None:
        for i in range(self.capacity):
            j = self.h(k, i)
            if self.ht[j] is None:
                return None
            elif self.ht[j] == k:
                self.ht[j] = "deleted"
                if self.size == self.capacity / 4:
                    self.table_shrink()
                return j
        return None  # exhausted table

    def table_doubling(self) -> None:
        old_ht = self.ht

        self.capacity *= 2
        self.ht = [None] * self.capacity

        for item in old_ht:
            if item is not None:
                # noinspection PyTypeChecker
                self.hash_insert(item)

    def table_shrink(self) -> None:
        old_ht = self.ht

        self.capacity /= 2
        self.ht = [None] * self.capacity

        for item in old_ht:
            # noinspection PyTypeChecker
            self.hash_insert(item)
