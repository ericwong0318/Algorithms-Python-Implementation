class MergeSort:
    def merge_sort(self, arr: list, a=0, b=None) -> None:
        """
        Time complexity is ϴ(n * lg(n)).
        Space complexity is O(n).

        :param arr: unsorted list
        :param a: starting index of arr
        :param b: ending index + 1 or len of arr
        :return: None
        """
        if b is None:
            b = len(arr)

        # divide
        if b - a > 1:
            c = (a + b + 1) // 2  # c is middle index
            self.merge_sort(arr, 0, c)
            self.merge_sort(arr, c, b)

            # combine
            l_arr, r_arr = arr[a:c], arr[c: b]  # slice into left and right array
            i, j = 0, 0  # i and j are index of l_arr and r_arr
            while a < b:
                if (j >= len(r_arr)) or (i < len(l_arr) and l_arr[i] < r_arr[j]):
                    arr[a] = l_arr[i]
                    i += 1
                else:
                    arr[a] = r_arr[j]
                    j += 1
                a += 1
