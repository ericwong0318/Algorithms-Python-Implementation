# time complexity
# best O(n)
# average O(n**2)
# worst O(n**2)
# space O(1)

class InsertionSort(object):
    def insertion_sort(self, arr):
        for j in range(1, len(arr)):
            key = arr[j]  # hold value
            # find correct location i in first half sorted array
            i = j - 1
            while i > 0 and arr[i] > key:
                arr[i + 1] = arr[i]  # shift to next slot
                i -= 1
            arr[i + 1] = key
        return arr
