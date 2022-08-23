class Node:
    def __init__(self, value = 0, prev = None, next = None):
        self.value = value
        self.prev = prev
        self.next = next
        
class LRUCache:

    def __init__(self, capacity: int):
        self.map1 = {}
        self.map2 = {}
        self.capacity = capacity
        self.size = 0
        self.head = Node()
        self.tail = Node(prev=self.head)
        self.head.next = self.tail

    def get(self, key: int) -> int:
        if key in self.map1:
            self.put(key,self.map1[key].value)
            return self.map1[key].value
        return -1
        

    def put(self, key: int, value: int) -> None:
        current = self.map1.get(key, Node(value))
        if key in self.map1:
            current.value = value
            current.prev.next = current.next
            current.next.prev = current.prev
        else:
            if self.size == self.capacity:
                deleted = self.head.next
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
                deleted_key = self.map2[deleted]
                self.map1.pop(deleted_key)
                self.map2.pop(deleted)
            else:
                self.size += 1
        self.map1[key] = current
        self.map2[current] = key
        
        current.prev = self.tail.prev
        current.next = self.tail
        self.tail.prev.next = current
        self.tail.prev = current
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)