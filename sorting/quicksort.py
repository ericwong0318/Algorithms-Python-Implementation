import random


class QuickSort:
    def quick_sort(self, a: list, left: int, right: int) -> None:
        if left < right:
            mid = self.partition(a, left, right)
            self.quick_sort(a, left, mid - 1)
            self.quick_sort(a, mid + 1, right)

    @staticmethod
    def partition(a: list, left: int, right: int):
        """
        running time depends on partitioning is balanced or not
        O(n)
        :param a:
        :param left:
        :param right:
        :return:
        """
        pivot = a[right]
        i = left - 1  # i start at -1
        for j in range(left, right - 1):  # right is pivot, so end point is right - 1
            if a[j] <= pivot:
                i += 1
                a[i] = a[j], a[j] = a[i]  # swap i, j
        a[i + 1] = a[right], a[right] = a[i + 1]  # swap i + 1, pivot
        return i + 1

    def randomized_quicksort(self, a: list, left, right):
        if left < right:
            rand_num = self.randomized_partition(a, left, right)
            self.randomized_quicksort(a, left, rand_num - 1)
            self.randomized_partition(a, rand_num + 1, right + 1)

    def randomized_partition(self, a: list, left, right):
        """
        set random element as pivot
        :param a:
        :param left:
        :param right:
        :return:
        """
        pivot = random.randint(left, right)
        a[right] = a[pivot], a[pivot] = a[right]
        return self.partition(a, left, right)
