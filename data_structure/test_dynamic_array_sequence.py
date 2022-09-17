import unittest

from dynamic_array_sequence import DynamicArraySequence


class TestDynamicArraySequence(unittest.TestCase):
    def setUp(self) -> None:
        self.arr = DynamicArraySequence()
        self.arr.build([i for i in range(5)])

    def test_build(self):
        self.assertEqual([0, 1, 2, 3, 4, None, None, None], self.arr.a)

    def test_get_at(self):
        for i in range(5):
            self.assertEqual(i, self.arr.get_at(i))
        for i in range(5, 8):
            self.assertEqual(None, self.arr.get_at(i))

    def test_set_at(self):
        for i in range(5):
            self.arr.set_at(i, 0)
        self.assertEqual([0, 0, 0, 0, 0, None, None, None], self.arr.a)

    def test_insert_last(self):
        """Test insert_last() and resize() simultaneously"""
        self.arr = DynamicArraySequence()
        self.assertEqual([None, None], self.arr.a)
        for i in range(5):
            self.arr.insert_last(i)
            if i == 0:
                self.assertEqual([0, None], self.arr.a)
            elif i == 1:
                self.assertEqual([0, 1, None, None], self.arr.a)
            elif i == 2:
                self.assertEqual([0, 1, 2, None], self.arr.a)
            elif i == 3:
                self.assertEqual([0, 1, 2, 3, None, None, None, None], self.arr.a)
            elif i == 4:
                self.assertEqual([0, 1, 2, 3, 4, None, None, None], self.arr.a)

    def test_delete_last(self):
        """Test insert_last() and resize() simultaneously"""
        for i in range(5):
            self.arr.delete_last()
            if i == 0:
                self.assertEqual([0, 1, 2, 3, None, None, None, None], self.arr.a)
            elif i == 1:
                self.assertEqual([0, 1, 2, None, None, None, None, None], self.arr.a)
            elif i == 2:
                self.assertEqual([0, 1, None, None], self.arr.a)
            elif i == 3:
                self.assertEqual([0, None], self.arr.a)
            elif i == 4:
                self.assertEqual([None, None], self.arr.a)
                self.assertEqual(0, len(self.arr))

    def test_insert_at(self):
        self.arr.insert_at(2, 5)
        self.assertEqual([0, 1, 5, 2, 3, 4, None, None], self.arr.a)

    def test_delete_at(self):
        self.arr.delete_at(2)
        self.assertEqual([0, 1, 3, 4, None, None, None, None], self.arr.a)

    def test_insert_first(self):
        self.arr.insert_first(5)
        self.assertEqual([5, 0, 1, 2, 3, 4, None, None], self.arr.a)

    def test_delete_first(self):
        self.arr.delete_first()
        self.assertEqual([1, 2, 3, 4, None, None, None, None], self.arr.a)


if __name__ == '__main__':
    unittest.main()
