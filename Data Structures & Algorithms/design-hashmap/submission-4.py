class ListHash:
    def __init__(self,key = -1, val = -1, next = None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        self.MyHash = [ListHash() for _ in range(10000)]
    
    def hash(self, key: int):
        return key % len(self.MyHash)

    def put(self, key: int, value: int) -> None:
        c = self.MyHash[self.hash(key)]
        while c.next:
            if c.next.key == key:
                c.next.val = value
                return
            c = c.next
        c.next = ListHash(key, value)

    def get(self, key: int) -> int:
        c = self.MyHash[self.hash(key)].next
        while c:
            if c.key == key:
                return c.val
            c = c.next
        return -1

    def remove(self, key: int) -> None:
        c = self.MyHash[self.hash(key)]
        while c.next:
            if c.next.key == key:
                c.next = c.next.next
                return
            c = c.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)