from math import sqrt, floor
from random import randint
from collections import deque
from sympy import nextprime, primerange


class OpenHashingHashTable(object):
    """
    use deque as doubly linked list
    support insert, delete and search
    """

    def __init__(self, size: int, hash_func: int = 2):
        """
        According to CPython, the random integer is generate by /dev/urandom, based on the environment noise.
        https://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git/tree/drivers/char/random.c?id=refs/tags/v3.15.6

        from os import urandom as _urandom

        # Generate n random bytes.
        def randbytes(self, n):
            return _urandom(n)

        we will use sympy library to prime computation
        https://github.com/sympy/sympy/blob/master/sympy/ntheory/generate.py
        nextprime() and primerange() search potential primes located at 6 * size + 1 or 6 * size - 1
        """
        self.size = size
        self.t = [deque([]) for _ in range(size)]
        if hash_func == 0:
            self.hash_func = self.division_method_hashing
        elif hash_func == 1:
            # The value of a is determined by researcher.
            self.a = (sqrt(5) - 1) / 2
            self.hash_func = self.multiplication_method_hashing
        else:
            self.p = nextprime(size)
            self.a = randint(1, self.p - 1)
            self.b = randint(0, self.p - 1)
            self.hash_func = self.universal_hashing

    def division_method_hashing(self, k):
        return k % self.size

    def multiplication_method_hashing(self, k):
        """
        The multiplication method is better than division method (k % size) because the size of hash table is not
        critical.
        """
        # size or local list size
        return floor(self.size * (k * self.a % 1))

    def universal_hashing(self, k):
        return ((self.a * k + self.b) % self.p) % self.size

    def chained_hash_insert(self, x):
        hash_val = self.hash_func(x)
        self.t[hash_val].appendleft(x)

    def chained_hash_search(self, x):
        hash_val = self.hash_func(x)
        return self.t[hash_val].count(x) > 0

    def chained_hash_delete(self, x):
        hash_val = self.hash_func(x)
        for _ in range(self.t[hash_val].count(x)):
            self.t[hash_val].remove(x)
