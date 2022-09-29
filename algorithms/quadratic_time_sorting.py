class QuadraticTimeSorting(object):

    @staticmethod
    def insertion_sort(a: list) -> None:
        """
        Average and worst time complexities are O(n**2).
        Space complexity is O(1).

        :param a: unsorted list
        :return: None
        """
        for j in range(1, len(a)):
            key = a[j]  # hold value

            # find and swap correct location i in first half sorted array
            i = j - 1
            while i > 0 and a[i] > key:
                a[i + 1] = a[i]  # shift to next slot
                i -= 1
            a[i + 1] = key

    @staticmethod
    def bubble_sort(a: list) -> None:
        """
        Average and worst time complexities are O(n**2).
        Space complexity is O(1).

        :param a: unsorted list
        :return: None
        """
        for i in range(len(a) - 1, 0, -1):
            for j in range(i):  # bubble max to the tail of the list
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]

    @staticmethod
    def selection_sort(a: list) -> None:
        """
        Average and worst time complexities are O(n**2).
        Space complexity is O(1).

        :param a: unsorted list
        :return: None
        """
        if len(a) <= 1:
            return

        # find first (n - 1)th minimum element's index
        for i in range(len(a) - 1):
            min_index = i  # minimum element's index

            for j in range(i + 1, len(a)):
                if a[j] < a[min_index]:
                    min_index = j

            # if data[min_index] < data[i], swap them, so minimum element can go to end of sorted array
            if a[min_index] < a[i]:
                a[i], a[min_index] = a[min_index], a[i]
