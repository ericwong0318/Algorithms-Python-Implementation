from data_structure import open_hashing_hash_table as ht

if __name__ == '__main__':
    HT = ht.OpenHashingHashTable(20, 3)
    HT.chained_hash_insert(1)
    HT.chained_hash_insert(1)
    HT.chained_hash_insert(1)
    HT.chained_hash_insert(2)
    print(HT.chained_hash_search(3))
    HT.chained_hash_delete(1)
    for val in HT.t:
        print(val)
