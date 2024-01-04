from collections import OrderedDict
 
 
class LRUCache:
    """
    This is alternative implementation of LRU cache based on OrderedDict
    """
    capacity: int
    cache_map: OrderedDict
 
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache_map = OrderedDict()
 
    def get(self, key: int) -> int:
        if key not in self.cache_map:
            return -1
 
        value = self.cache_map[key]
        self.cache_map.move_to_end(key)
 
        return value
 
    def put(self, key: int, value: int) -> None:
        if key in self.cache_map:
            self.cache_map[key] = value
            self.cache_map.move_to_end(key)
            return
 
        if len(self.cache_map) >= self.capacity:
            lru_key = next(iter(self.cache_map))
            del self.cache_map[lru_key]
 
        self.cache_map[key] = value


LRUCache  = LRUCache(2)
LRUCache.put(1, 1) # cache is {1=1}
LRUCache.put(2, 2) # cache is {1=1, 2=2}
LRUCache.get(1)    # return 1
LRUCache.put(3, 3) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
LRUCache.get(2)    # returns -1 (not found)
LRUCache.put(4, 4) # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
LRUCache.get(1)    # return -1 (not found)
LRUCache.get(3)    # return 3
LRUCache.get(4)    # return 4

print(LRUCache.cache_map)