from math import sqrt, floor
from collections import deque
from sympy import nextprime, primerange


class CloseHashingHashTable(object):
    """
    support insert, delete and search
    table doubling
    """

    def __init__(self, size: int, hash_func: int = 2):
        self.size = size
        self.t = [[] for _ in range(size)]
        if hash_func == 0:
            self.hash_func = self.division_method_hashing
        elif hash_func == 1:
            # The value of a is determined by researcher.
            self.A = (sqrt(5) - 1) / 2
            self.hash_func = self.multiplication_method_hashing
        else:
            self.p = nextprime(size)
            self.a = primerange(1, size)
            self.b = primerange(0, size)
            self.hash_func = self.universal_hashing

    def division_method_hashing(self, k):
        return k % self.size

    def multiplication_method_hashing(self, k):
        """
        The multiplication method is better than division method (k % size) because the size of hash table is not
        critical.
        """
        # size or local list size
        return floor(self.size * (k * self.A % 1))

    def universal_hashing(self, k):
        return ((self.a * k + self.b) % self.p) % self.size

    def hash_insert(self, x):
        hash_value = self.hash_function(x)
        self.t[hash_value].append(x)

    def chained_hash_search(self, x):
        hash_value = self.hash_function(x)
        return self.t[hash_value].count(x) > 0

    def chained_hash_delete(self, x):
        hash_value = self.hash_function(x)
        for _ in range(self.t[hash_value].count(x)):
            self.t[hash_value].remove(x)
