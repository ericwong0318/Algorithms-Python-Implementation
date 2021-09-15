import unittest
from sorting import linear_time_sorting, merge_sort, quadratic_time_sorting, quicksort
from random import randint


class TestSorting(unittest.TestCase):
    def setUp(self) -> None:
        # self.unsorted_list = [randint(0, 9) for _ in range(10)] for test random list
        self.radix_sort = linear_time_sorting.LinearTimeSorting().radix_sort
        self.bubble_sort = quadratic_time_sorting.QuadraticTimeSorting().bubble_sort
        self.insertion_sort = quadratic_time_sorting.QuadraticTimeSorting().insertion_sort
        self.selection_sort = quadratic_time_sorting.QuadraticTimeSorting().selection_sort
        self.quicksort = quicksort.QuickSort().quick_sort
        self.randomized_quicksort = quicksort.QuickSort().randomized_quicksort

    def test_normal_list(self):
        unsorted_list = [5, 0, 7, 4, 8, 6, 3, 9, 1, 2]
        sorted_list = [i for i in range(10)]

        result = self.radix_sort(unsorted_list, 1, 9)
        self.assertEqual(sorted_list, result)
        # bubble sort
        unsorted_list_copy = unsorted_list
        self.bubble_sort(unsorted_list_copy)
        self.assertEqual(sorted_list, unsorted_list_copy)
        # insertion sort
        unsorted_list_copy = unsorted_list
        self.insertion_sort(unsorted_list_copy)
        self.assertEqual(sorted_list, unsorted_list_copy)
        # selection sort
        unsorted_list_copy = unsorted_list
        self.selection_sort(unsorted_list_copy)
        self.assertEqual(sorted_list, unsorted_list_copy)
        # quicksort
        unsorted_list_copy = unsorted_list
        self.quicksort(unsorted_list_copy, 0, len(unsorted_list_copy) - 1)
        self.assertEqual(sorted_list, unsorted_list_copy)
        # randomized quicksort
        unsorted_list_copy = unsorted_list
        self.randomized_quicksort(unsorted_list_copy, 0, len(unsorted_list_copy) - 1)
        self.assertEqual(sorted_list, unsorted_list_copy)

    def test_empty_list(self):
        # self.assertEqual([], self.radix_sort([], 0, 0))
        empty_list = []
        self.bubble_sort(empty_list)
        self.assertEqual([], empty_list)

        # def test_merge_sort(self):
    #     unsorted_arr = [5, 0, 7, 4, 8, 6, 3, 9, 1, 2]
    #     sorted_arr = [i for i in range(10)]
    #     ms = merge_sort.MergeSort()
    #     result = ms.merge_sort(unsorted_arr, 0, len(unsorted_arr))  # ???
    #     self.assertEqual(sorted_arr, result)

    #
    # def test_reversed_list:
    #
    # def test_sorted_list:
    #
    # def test_negative_number_list:
    #     unsorted_arr = [5, 0, 7, 4, 8, 6, 3, 9, 1, 2] * -1
    #     sorted_arr = [-i for i in range(10)]


if __name__ == '__main__':
    unittest.main()
