import unittest
from collections import deque

from close_addressing_hash_table import CloseAddressingHashTable


class TestCloseAddressHashTable(unittest.TestCase):
    def setUp(self) -> None:
        self.DivisionMethodHashTable = CloseAddressingHashTable(10, 0)
        self.MultiplicationMethodHashTable = CloseAddressingHashTable(10, 1)

    def test_division_method_hash_table_insert(self):
        for i in range(10):
            self.DivisionMethodHashTable.chained_hash_insert(i)
        self.assertEqual(
            [deque([0]), deque([1]), deque([2]), deque([3]), deque([4]), deque([5]), deque([6]), deque([7]), deque([8]),
             deque([9])],
            self.DivisionMethodHashTable.ht
        )

    def test_multiplication_method_hash_table_insert(self):
        for i in range(10):
            self.MultiplicationMethodHashTable.chained_hash_insert(i)
        self.assertEqual(
            [deque([5, 0]), deque([]), deque([2]), deque([7]), deque([4]), deque([9]), deque([1]), deque([6]),
             deque([3]), deque([8])],
            self.MultiplicationMethodHashTable.ht
        )

    def test_division_method_hash_table_search_normal_case(self):
        for i in range(3):
            self.DivisionMethodHashTable.chained_hash_insert(1)
        self.assertEqual(3, self.DivisionMethodHashTable.chained_hash_search(1))

    def test_division_method_hash_table_search_no_found_case(self):
        for i in range(3):
            self.DivisionMethodHashTable.chained_hash_insert(1)
        self.assertEqual(0, self.DivisionMethodHashTable.chained_hash_search(-1))

    def test_multiplication_method_hash_table_search_normal_case(self):
        for i in range(3):
            self.MultiplicationMethodHashTable.chained_hash_insert(1)
        self.assertEqual(3, self.MultiplicationMethodHashTable.chained_hash_search(1))

    def test_multiplication_method_hash_table_search_no_found_case(self):
        for i in range(3):
            self.MultiplicationMethodHashTable.chained_hash_insert(1)
        self.assertEqual(0, self.MultiplicationMethodHashTable.chained_hash_search(-1))

    def test_division_method_hash_table_delete(self):
        for i in range(10):
            self.DivisionMethodHashTable.chained_hash_insert(i)
        for i in range(10):
            self.DivisionMethodHashTable.chained_hash_delete(i)
        self.assertEqual([deque([]) for _ in range(10)], self.DivisionMethodHashTable.ht)

    def test_multiplication_method_hash_table_delete(self):
        for i in range(10):
            self.MultiplicationMethodHashTable.chained_hash_insert(i)
        for i in range(10):
            self.MultiplicationMethodHashTable.chained_hash_delete(i)
        self.assertEqual([deque([]) for _ in range(10)], self.MultiplicationMethodHashTable.ht)
