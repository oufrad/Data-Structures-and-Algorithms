class HashTable():
    def __init__(self, length):
        self.length = length
        self.data = [0] * length

    def _hash(self, key):   # O(1) even though we loop over the key (hash functions are very fast)
        hash_value = 0
        for i in range(len(key)):
            hash_value = (hash_value + ord(key[i]) * i) % len(self.data)
        return hash_value
    
    def get(self, key):     # O(1) most of the time. but rarely O(n) if we have hash collision
        bucket_index = self._hash(key)
        if len(self.data[bucket_index]) <= 1:
            return self.data[bucket_index]
        else : 
            for elem in self.data[bucket_index]:
                if elem[0] == key:
                    return elem
        return []

    def set(self, key, value):      # O(1)
        bucket = [key, value]
        bucket_index = self._hash(key)
        if self.data[bucket_index] == 0:
            self.data[bucket_index] = [bucket]
        else:
            self.data[bucket_index].append(bucket)

    def keys(self):     # iteration is one of the downside of using hash tables. 
        keys = []
        for elem in self.data:      # it loops over 10 elements even though we only has 3 elements in our Hash Table (array are way more good in iterations)
            if elem == 0:
                continue
            elif len(elem) == 1:
                keys.append(elem[0][0])
            else:
                for item in elem: 
                    keys.append(item[0])
        return keys



hash_table = HashTable(10)

hash_table.set("name", "Mohamed Oufrad")
hash_table.set("age", 23)
hash_table.set("power", "never giving up!")

print(hash_table.data)

print(hash_table.get("power"))

print(f"the keys of our Hash Table is : {hash_table.keys()}")