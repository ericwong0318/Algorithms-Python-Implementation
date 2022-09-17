from random import randint


class QuickSort:
    def quick_sort(self, a: list) -> None:
        """
        Average and worst time complexities are O(n * lg(n)) and O(n^2).
        Space complexity is O(lg(n)).

        :param a: unsorted list
        :return: None
        """
        self._quick_sort(a, 0, len(a) - 1)

    def _quick_sort(self, a: list, left: int, right: int) -> None:
        if left < right:
            mid = self.partition(a, left, right)
            self._quick_sort(a, left, mid - 1)
            self._quick_sort(a, mid + 1, right)

    @staticmethod
    def partition(a: list, left: int, right: int) -> int:
        pivot = a[right]  # select pivot
        i = left - 1  # i start at -1
        for j in range(left, right):  # right is pivot, so end point is right - 1
            if a[j] <= pivot:
                i += 1
                a[i], a[j] = a[j], a[i]  # swap i, j
        a[i + 1], a[right] = a[right], a[i + 1]  # swap i + 1, pivot
        return i + 1

    def randomized_quicksort(self, a: list) -> None:
        """
        Worst case expected time complexity is O(n * lg (n)).
        Space complexity is O(lg(n)).

        :param a: unsorted list
        :return: None
        """
        self._randomized_quicksort(a, 0, len(a) - 1)

    def _randomized_quicksort(self, a: list, left, right) -> None:
        if left < right:
            rand_num = self.randomized_partition(a, left, right)
            self._randomized_quicksort(a, left, rand_num - 1)
            self._randomized_quicksort(a, rand_num + 1, right)

    def randomized_partition(self, a: list, left, right) -> int:
        pivot = randint(left, right)
        a[right], a[pivot] = a[pivot], a[right]
        return self.partition(a, left, right)
