class Item(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable(object):
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]  # 2-D array, we append element at different rows

    def _hash_function(self, key):  # overwrite???
        return key % self.size

    def set(self, key, value):
        hash_index = self._hash_function(key)
        for item in self.table[hash_index]:
            # if key exist, update value
            if item.key == key:
                item.value = value
                return
            # else append as new value
        self.table[hash_index].append(Item(key, value))

    def get(self, key):
        hash_index = self._hash_function(key)
        for item in self.table[hash_index]:
            if item.key == key:
                return item.value
        raise KeyError('key not found')

    def remove(self, key):
        hash_index = self._hash_function(key)
        for index, item in self.table[hash_index]:
            if item.key == key:
                del self.table[hash_index][index]
                return
        raise KeyError('key not found')
