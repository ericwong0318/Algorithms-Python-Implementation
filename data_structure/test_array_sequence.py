import unittest

from array_sequence import ArraySequence


class TestArraySequence(unittest.TestCase):
    def setUp(self) -> None:
        self.arr = ArraySequence()
        self.arr.build([i for i in range(10)])

    def test_build(self):
        self.assertEqual([i for i in range(10)], self.arr.a)

    def test_get_at(self):
        for i in range(10):
            self.assertEqual(i, self.arr.get_at(i))

    def test_set_at(self):
        for i in range(10):
            self.arr.set_at(i, 0)
        self.assertEqual([0 for _ in range(10)], self.arr.a)

    def test_insert_at(self):
        self.arr.insert_at(5, 0)
        self.assertEqual([0, 1, 2, 3, 4, 0, 5, 6, 7, 8, 9], self.arr.a)

    def test_delete_at(self):
        self.arr.delete_at(5)
        self.assertEqual([0, 1, 2, 3, 4, 6, 7, 8, 9], self.arr.a)

    def test_insert_first(self):
        self.arr.insert_first(5)
        self.assertEqual([5, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9], self.arr.a)

    def test_delete_first(self):
        self.arr.delete_first()
        self.assertEqual([i for i in range(1, 10)], self.arr.a)

    def test_insert_last(self):
        self.arr.insert_last(5)
        self.assertEqual([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 5], self.arr.a)

    def test_delete_last(self):
        self.arr.delete_last()
        self.assertEqual([i for i in range(9)], self.arr.a)


if __name__ == '__main__':
    unittest.main()
