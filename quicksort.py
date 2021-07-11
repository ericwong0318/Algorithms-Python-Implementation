import random


class QuickSort:
    def __init__(self):
        self.a = []

    def quick_sort(self, left: int, right: int):
        if left < right:
            mid = self.partition(left, right)
            self.quick_sort(left, mid - 1)  # ?
            self.quick_sort(mid + 1, right)

    def partition(self, left: int, right: int):
        """
        running time depends on partitioning is balanced or not
        O(n)
        :param left:
        :param right:
        :return:
        """
        pivot = self.a[right]
        i = left - 1  # i start at -1
        for j in range(left, right - 1):  # right is pivot, so end point is right - 1
            if self.a[j] <= pivot:
                i += 1
                self.a[i] = self.a[j], self.a[j] = self.a[i]  # swap i, j
        self.a[i + 1] = self.a[right], self.a[right] = self.a[i + 1]  # swap i + 1, pivot
        return i + 1

    def randomized_quicksort(self, left, right):
        if left < right:
            rand_num = self.randomized_partition(left, right)
            self.randomized_quicksort(left, rand_num - 1)
            self.randomized_partition(rand_num + 1, right + 1)

    def randomized_partition(self, left, right):
        """
        set random element as pivot
        :param left:
        :param right:
        :return:
        """
        pivot = random.randint(left, right)
        self.a[right] = self.a[pivot], self.a[pivot] = self.a[right]
        return self.partition(left, right)
