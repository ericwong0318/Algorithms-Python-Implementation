import math


class MergeSort(object):
    def merge_sort(self, a: list, left: int, right: int):
        """
        merge sort

        time O(n*lg(n))
        space O(n)

        :param a: unsorted array
        :param left: left index
        :param right: right index
        :return a: sorted array
        """
        if left < right:
            mid = math.floor((left + right) / 2)
            self.merge_sort(a, left, mid)
            self.merge_sort(a, mid + 1, right)
            self.merge(a, left, mid, right)
        return a

    def merge(self, a: list, left: int, mid: int, right: int):
        # len of 2 sub arrays
        l_arr_len = mid - left + 1
        r_arr_len = right - mid

        # create 2 sub arrays
        l_arr = []
        r_arr = []
        for i in range(0, l_arr_len):
            l_arr[i] = a[left + i - 1]
        for j in range(0, r_arr_len):
            r_arr[j] = a[mid + j]

        # put sentinels at the end of 2 sub arrays
        # avoid have to check whether either pile is empty in for loop below, so it simplify the code
        l_arr[l_arr_len + 1] = math.inf
        r_arr[r_arr_len + 1] = math.inf

        # merge with 2 pointer
        i = 1
        j = 1
        for k in range(left, right):
            if l_arr[i] <= r_arr[j]:
                a[k] = l_arr[i]
                i += 1
            else:
                a[k] = r_arr[j]
                j += 1

        return a
