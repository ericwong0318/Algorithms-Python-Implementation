import unittest

from string_matching import simple_match, rabin_karp, rabin_karp_2


class TestStringMatching(unittest.TestCase):
    def setUp(self) -> None:
        self.text = "this is a text"
        self.substring = "text"
        self.non_substring = "abc"

    def test_simple_match(self):
        self.assertEqual(10, simple_match(self.substring, self.text))
        self.assertEqual(-1, simple_match(self.non_substring, self.text))

    def test_rabin_karp(self):
        self.assertEqual(10, rabin_karp(self.substring, self.text))
        self.assertEqual(-1, rabin_karp(self.non_substring, self.text))

    def test_rabin_karp_2(self):
        self.assertEqual(10, rabin_karp_2(self.substring, self.text))
        self.assertEqual(-1, rabin_karp_2(self.non_substring, self.text))


if __name__ == '__main__':
    unittest.main()
