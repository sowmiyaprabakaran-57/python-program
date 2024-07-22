class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.order = []
    def get(self, key: int) -> int:
        if key in self.cache:
            self.order.remove(key)
            self.order.append(key)
            return self.cache[key]
        return -1
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.order.remove(key)
        elif len(self.cache) >= self.capacity:
            oldest = self.order.pop(0)
            del self.cache[oldest]
        self.cache[key] = value
        self.order.append(key)
lru = LRUCache(2)
lru.put(1, 1)
lru.put(2, 2)
print(lru.get(1))  
lru.put(3, 3)
print(lru.get(2))  
lru.put(4, 4)
print(lru.get(1)) 
print(lru.get(3))  
print(lru.get(4))  
