from sympy import nextprime
from Lib.queue import SimpleQueue


def match_substring(s: list, t: list) -> bool:
    """
    if found substring s in string t, return true
    O(len(s)) for each comparison
    O(len(t)-len(s)) = O(len(t)) times comparison
    worst time complexity = O(len(s)*len(t))
    """
    for i in range(len(t) - len(s) + 1):  # i is head of comparing string, increase from 0 to len(t)-len(s)+1
        if s == t[i: i + len(s)]:
            return True
    return False


class RollingHash:
    """
    maintain a hashed substring, then compare it to hashed string
    if hash value is the same, two strings are the same
    """

    def __init__(self, min_size: int):
        self.hash_val = 0
        self.size = 0
        self.base = nextprime(min_size)  # use next prime, so that less collision
        self.q = SimpleQueue()  # hash value is enough?

    def append(self, c: str) -> None:
        self.hash_val *= 256  # shift one digit
        self.hash_val += ord(c) % self.base
        self.size += 1
        self.q.put(c)

    def pop_left(self) -> None:
        self.hash_val %= 256 ** self.size
        self.size -= 1
        self.q.get()

    @staticmethod
    def karp_rabin_search(s: list, t: list):
        """"""
        rh_s = RollingHash(len(s))
        rh_t = RollingHash(len(s))
        """preprocessing"""
        for c in s:
            rh_s.append(c)
        for c in t[:len(s)]:
            rh_t.append(c)
        if rh_s.hash_val == rh_t.hash_val:
            return True
        """"move rolling hash"""
        for i in range(len(s), len(t)):
            rh_t.pop_left()
            rh_t.append(t[i])  # store c as list?
            if rh_s.hash_val == rh_t.hash_val:
                """
                although the hash value is the same, it may means collision
                check every character
                """
                #     if rh_t.q. == rh_s.q:
                return True
        return False
