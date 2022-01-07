class MergeSort:
    def merge_sort(self, a: list) -> None:
        """
        Time complexity is ϴ(n * lg(n)).
        Space complexity is O(n).

        :param a: unsorted list
        :return: None
        """

        # divide
        if len(a) > 1:
            mid = len(a) // 2

            l_arr = a[:mid]
            r_arr = a[mid:]

            self.merge_sort(l_arr)
            self.merge_sort(r_arr)

            # merge
            i = j = k = 0
            while i < len(l_arr) and j < len(r_arr):
                if l_arr[i] < r_arr[j]:
                    a[k] = l_arr[i]
                    i += 1
                else:
                    a[k] = r_arr[j]
                    j += 1
                k += 1

            while i < len(l_arr):
                a[k] = l_arr[i]
                i += 1
                k += 1

            while j < len(r_arr):
                a[k] = r_arr[j]
                j += 1
                k += 1
