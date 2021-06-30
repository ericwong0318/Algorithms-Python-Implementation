# time O(n^2)
# Worst-case time complexity 	О(n^2) comparisons, О(n) swaps
# Average performance	О(n^2) comparisons, О(n) swaps
# Best-case performance	О(n^2) comparisons, O(1) swaps
# Worst-case space complexity O(1)

class SelectionSort(object):
    def sort(self, data):
        # one data only
        if len(data) <= 1:
            return data
        for i in range(len(data) - 1):
            min_index = i  # minimum element's index
            # find minimum element and update min_index
            for j in range(i + 1, len(data)):
                if data[j] < data[min_index]:
                    min_index = j
            # if data[min_index] < data[i], swap them, so minimum element can go to front of array
            if data[min_index] < data[i]:
                data[i], data[min_index] = data[min_index], data[i]
        return data
