import unittest
from data_structure.rolling_hash import *


class TestRollingHash(unittest.TestCase):

    def test_match_substring(self):
        text = "THIS IS A TEST TEXT"
        string = "TEXT"
        self.assertTrue(match_substring(list(string), list(text)))

    def test_string_exist_in_text(self):
        text = "THIS IS A TEST TEXT"
        string = "TEXT"
        RollingHash(len(string))
        self.assertTrue(RollingHash.karp_rabin_search(list(string), list(text)))


if __name__ == '__main__':
    unittest.main()
