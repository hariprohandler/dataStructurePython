class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] in range(self.MAX)]
    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char) #ASCII value
        return h % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        #self.arr[h] = val
        found = False
        for inx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
                break
        if not found:
            self.arr[h].append(key, val)

    def __getitem__(self, key):
        return self.arr[key]

    def __delitem__(self,key):
        h = self.get_hash(key)
        self.arr[h] = None

t = HashTable()

t.get_hash("march 6")