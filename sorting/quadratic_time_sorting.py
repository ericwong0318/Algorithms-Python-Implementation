class QuadraticTimeSorting(object):
    """
    time complexity:
        average O(n**2)
        worst O(n**2)
    space complexity O(1)
    """

    @staticmethod
    def insertion_sort(a: list) -> None:
        for j in range(1, len(a)):
            key = a[j]  # hold value
            # find correct location i in first half sorted array
            i = j - 1
            while i > 0 and a[i] > key:
                a[i + 1] = a[i]  # shift to next slot
                i -= 1
            a[i + 1] = key

    @staticmethod
    def bubble_sort(a: list) -> None:
        for i in range(0, len(a)):
            for j in range(len(a), i + 1, -1):
                # if previous element < current element, swap them
                if a[j] < a[j - 1]:
                    a[j] = a[j - 1], a[j - 1] = a[j]

    @staticmethod
    def selection_sort(a: list) -> None:
        if len(a) <= 1:
            return
        for i in range(len(a) - 1):
            min_index = i  # minimum element's index
            # find first (n - 1)th minimum element
            for j in range(i + 1, len(a)):
                if a[j] < a[min_index]:
                    min_index = j
            # if data[min_index] < data[i], swap them, so minimum element can go to front of array
            if a[min_index] < a[i]:
                a[i], a[min_index] = a[min_index], a[i]
