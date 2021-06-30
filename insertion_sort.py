# Worst-case performance	О(n^2) comparisons and swaps
# Average performance	О(n^2) comparisons and swaps
# Best-case performance	O(n) comparisons, O(1) swaps
# Worst-case space complexity О(n) total, O(1) auxiliary
# a: array
class InsertionSort(object):
    # https://github.com/DCtheTall/mit6.006/blob/master/lecture03/insertionsort.py
    # CULS
    def insertion_sort(self, a):
        for j in range(1, len(a)):
            key = a[j]
            i = j - 1
            while i > 0 and a[i] > key:
                a[i + 1] = a[i]
                i -= 1
            a[i + 1] = key
