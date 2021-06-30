# time O(n*lg(n))
# space O(n)

class MergeSort(object):
    def sort(self, data):
        return self._sort(data)

    def _sort(self, data):
        # base case
        if len(data) <= 1:
            return data

        # recursive step
        mid = len(data) // 2
        # divide
        left = data[:mid]
        right = data[mid:]
        # conquer
        left = self._sort(left)
        right = self._sort(right)
        # merge
        return self._merge(left, right)

    def _merge(self, left, right):
        l = 0
        r = 0
        result = []
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
        # copy remaining elements
        while l < len(left):
            result.append(left[l])
            l += 1
        while r < len(right):
            result.append(right[r])
            r += 1
        return result
