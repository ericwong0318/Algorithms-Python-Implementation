class LinearTimeSorting(object):

    @staticmethod
    def counting_sort(a: list, k: int) -> list:
        """
        Time and space complexity are O(n + k).

        :param a: unsorted list
        :param k: max possible value of element in a
        """
        count = [0 for _ in range(k + 1)]  # index is from 0 to k
        for element in a:
            count[element] += 1
        for i in range(1, k + 1):
            count[i] += count[i - 1]

        out = [0 for _ in range(len(a))]
        for element in reversed(a):
            # out[] starts at 0, but counting starts at 1
            # for example, a[] = {3}, c = {0, 0, 0, 1}, out[0] = 3
            count[element] -= 1
            out[count[element]] = element

        return out

    def radix_sort(self, a: list, d: int, k: int):
        """
        Sort information that has multiple field, like date.
        Worst time complexity O(n * k).
        Worst space complexity O(n), because we use counting sort. O(n + 9) = O(n) when n >> 9.

        :param a: unsorted list
        :param d: max digit that elements have
        :param k: possible value of digit. k = 9 in Decimal
        :return:
        """
        for i in range(d):
            # use stable sort to sort the list by digit i
            return self.counting_sort(a, k)
