import unittest

from algorithms import linear_time_sorting, merge_sort, quadratic_time_sorting, quicksort


class TestSorting(unittest.TestCase):
    def setUp(self) -> None:
        self.bubble_sort = quadratic_time_sorting.QuadraticTimeSorting().bubble_sort
        self.insertion_sort = quadratic_time_sorting.QuadraticTimeSorting().insertion_sort
        self.selection_sort = quadratic_time_sorting.QuadraticTimeSorting().selection_sort
        self.merge_sort = merge_sort.MergeSort().merge_sort
        self.quicksort = quicksort.QuickSort().quick_sort
        self.randomized_quicksort = quicksort.QuickSort().randomized_quicksort
        self.radix_sort = linear_time_sorting.LinearTimeSorting().radix_sort

    def call_insert_bubble_select_merge_quick_sorts(self, unsorted_list, sorted_list):
        # bubble sort
        unsorted_list_copy = unsorted_list
        self.bubble_sort(unsorted_list_copy)
        self.assertEqual(unsorted_list_copy, sorted_list)
        # insertion sort
        unsorted_list_copy = unsorted_list
        self.insertion_sort(unsorted_list_copy)
        self.assertEqual(unsorted_list_copy, sorted_list)
        # selection sort
        unsorted_list_copy = unsorted_list
        self.selection_sort(unsorted_list_copy)
        self.assertEqual(unsorted_list_copy, sorted_list)
        # merge sort
        unsorted_list_copy = unsorted_list
        self.merge_sort(unsorted_list_copy)
        self.assertEqual(unsorted_list_copy, sorted_list)
        # quicksort
        unsorted_list_copy = unsorted_list
        self.quicksort(unsorted_list_copy)
        self.assertEqual(unsorted_list_copy, sorted_list)
        # randomized quicksort
        unsorted_list_copy = unsorted_list
        self.randomized_quicksort(unsorted_list_copy)
        self.assertEqual(unsorted_list_copy, sorted_list)

    def call_radix_sort(self, unsorted_list, sorted_list):
        # radix sort
        unsorted_list_copy = unsorted_list
        result = self.radix_sort(unsorted_list_copy, 1, 9)
        self.assertEqual(result, sorted_list)

    def test_normal_list(self):
        unsorted_list = [5, 0, 7, 4, 8, 6, 3, 9, 1, 2]
        sorted_list = [i for i in range(10)]
        self.call_insert_bubble_select_merge_quick_sorts(unsorted_list, sorted_list)
        self.call_radix_sort(unsorted_list, sorted_list)

    def test_empty_list(self):
        unsorted_list = []
        sorted_list = []
        self.call_insert_bubble_select_merge_quick_sorts(unsorted_list, sorted_list)
        self.call_radix_sort(unsorted_list, sorted_list)

    def test_negative_number(self):
        unsorted_list = [-5, 0, -7, -4, -8, -6, -3, -9, -1, -2]
        sorted_list = [-i for i in reversed(range(10))]
        self.call_insert_bubble_select_merge_quick_sorts(unsorted_list, sorted_list)

    def test_repeating_item(self):
        unsorted_list = [5, 5, 0, 0, 7, 7, 4, 4, 8, 8, 6, 6, 3, 3, 9, 9, 1, 1, 2, 2]
        sorted_list = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]
        self.call_insert_bubble_select_merge_quick_sorts(unsorted_list, sorted_list)
        self.call_radix_sort(unsorted_list, sorted_list)


if __name__ == '__main__':
    unittest.main()
